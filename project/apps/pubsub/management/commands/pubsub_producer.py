import logging
import uuid

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from project.apps.core.models import Category
from project.apps.pubsub.apps import PubsubConfig
from project.apps.pubsub.services import producer
from project.settings import STOMP_SERVER_HOST
from project.settings import STOMP_SERVER_PORT
from project.settings import TARGET_DESTINATION
from project.support.django_helpers import make_sure_database_is_usable

logger = logging.getLogger(__name__)

connection_params = {"host": STOMP_SERVER_HOST, "port": STOMP_SERVER_PORT, "client_id": PubsubConfig.name}
capitol_publisher = producer.build_publisher(TARGET_DESTINATION, **connection_params)


class Command(BaseCommand):
    help = "Start App producer"

    def handle(self, *args, **options):
        make_sure_database_is_usable()

        logger.info("Getting all categories to publish them...")
        categories = Category.objects.filter(end_at__lt=timezone.now(), distributed_at__isnull=True).values()

        logger.info(f"There are {categories.count()} categories to be sent")

        correlation_id = uuid.uuid4()
        logger.info(f"Correlation ID created: {correlation_id}")
        standard_header = {"correlation-id": correlation_id}

        with transaction.atomic():
            with producer.do_inside_transaction(capitol_publisher):
                for category in categories:
                    capitol_publisher.send(category, standard_header)
                categories.update(distributed_at=timezone.now())

        logger.info(f"Finished!")
