from django_seed import Seed
from django.core.management.base import BaseCommand
from faker import Faker

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        faker = Faker()
        print(faker.name())

       # print(fake.email())

# correctly initialized with a faker.generator.Generator instance, configured as above
# populator = Faker.getPopulator()
#
# from web.models import Worker
#
# populator.addEntity(Worker, 10, {
#     'score':    lambda x: populator.generator.randomInt(0,1000),
#     'nickname': lambda x: populator.generator.email(),
# })
# populator.execute()
# insertedPks = populator.execute()