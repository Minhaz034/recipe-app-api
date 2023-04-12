'''
Django command to wait for the database to be available
-Custom django management command
 '''
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


'''
NWtwork connectivity 
set depends_on on app service to start db 
first (see docker_compose.yaml)
Docker compose creates network
This app service can use db hostname

Volumes:
- store persistent data in docker compose
- maps directly in container to local machine


Before connecting to the database django needs to know:
- Engine (type of database)
- Hostname (IP of domain for database)
- Port (default 5432)
- Databse name
- username
- password

THese info are defined in the settings.py file
THese info will be pulled from the environment variables


Environment variables
- Pull config values from environment variables
- easily passed to docker container
- used in local dev of prod
- single place to configure project


Psycopg2 is the package that you need to connect django to the database
- most popular postgres adaptor for python
- supported 
- installation options:
    install psycopg2-binary : not good for prod
    psycopg2 : compiled from source , can be installed using pip,\
     more performance, dependencies need to be installed



'''


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable,waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
