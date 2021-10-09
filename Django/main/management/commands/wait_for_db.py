"""
    This file creates a command that sleeps until the database is ready.
"""
import time

from django.db.utils import OperationalError as OpError
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as PsyOpError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database...')
        db_available = False
        while db_available is False:
            try:
                self.check(databases=['default'])
                db_available = True
            except (PsyOpError, OpError):
                self.stdout.write('Database unavailable, waiting...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available!'))
