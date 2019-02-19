# polls/management/commands/create_db.py
import os
import sys
import logging
import MySQLdb

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

rds_host = os.getenv('DB_ENDPOINT')
db_name = os.getenv('DB_NAME')
user_name = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'Creates the initial database'

    def handle(self, *args, **options):
        print('Starting db creation')
        try:
            db = MySQLdb.connect(host=rds_host, user=user_name,
                                 password=password, db="mysql", connect_timeout=5)
            c = db.cursor()
            print("connected to db server")
            c.execute(f"""CREATE DATABASE {db_name};""")
            c.execute(
                f"""GRANT ALL PRIVILEGES ON db_name.* TO '{user_name}' IDENTIFIED BY '{password}';""")
            c.close()
            print("closed db connection")
        except:
            logger.error(
                "ERROR: Unexpected error: Could not connect to MySql instance.")
            sys.exit()
