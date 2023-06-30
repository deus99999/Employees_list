from django_seed import Seed
from django.core.management.base import BaseCommand
from faker import Faker
import random


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        # print(fake.name())
        # print(fake.email())
        # print(fake.job())


from django_seed import Seed

seeder = Seed.seeder()

from ...models import Worker
from ...models import Role


# def create_ceo_role():
#     seeder.add_entity(Role, 1, {
#             'role_level': 1,
#             'title': 'CEO',
#         })
#     seeder.execute()





# def create_ceo():
#     seeder.add_entity(Worker, 1, {
#         'level': 1,
#         'name': "Timothy Donald Cook",
#         'position': Role.objects.get(role_level=1),
#         'parent_id': None,
#         'email': lambda x: seeder.faker.email(),
#     })
#     seeder.execute()


#create director's position
def create_ceo_role():
    seeder.add_entity(Role, 1, {
            'role_level': 1,
            'title': 'CEO',
        })
    seeder.execute()


# create director
def create_ceo():
    seeder.add_entity(Worker, 1, {
        'level': 1,
        'name': "Timothy Donald Cook",
        'position': Role.objects.get(role_level=1),
        'parent_id': None,
        'email': lambda x: seeder.faker.email(),
        'tree_id': 1,
    })
    seeder.execute()


def create_second_roles():
    seeder.add_entity(Role, 3, {
            'role_level': 2,
            'title': lambda x: seeder.faker.job(),
            })
    seeder.execute()


def create_roles():
    for i in range(2, 8):
        seeder.add_entity(Role, 3, {
            'role_level': i,
            'title': lambda x: seeder.faker.job(),
            })
        seeder.execute()
        i += 1


# def create_workers_of_second_roles():
#     for i in range(2):
#         seeder.add_entity(Worker, 3, {
#             'level': 2,
#             'name': lambda x: seeder.faker.name(),
#             'position': random.choice([role for role in Role.objects.filter(role_level=2)]),
#             #'parent_id': random.choice([employee.level for employee in Worker.objects.filter(level=1)]),
#             'email': lambda x: seeder.faker.email(),
#             'tree_id': 2,
#             })
#         seeder.execute()

def create_workers():

    for i in range(1, 3):
        employees = Worker.objects.filter(level=i)
        print(employees)
        for employee in employees:
            print(employee.id, employee.name, employee.position, employee.parent)

            roles = Role.objects.filter(role_level=int(employee.level) + 1)
            role = random.choice(roles)

            seeder.add_entity(Worker, 2, {
                'level': int(employee.level) + 1,
                'name': lambda x: seeder.faker.name(),
                #'position': lambda x: seeder.faker.email(),
                'position': role,
                #'parent_id': random.choice([employee.level for employee in Worker.objects.filter(level=1)]),
                'email': lambda x: seeder.faker.email(),
                'tree_id': employee.tree_id + 1,
            })
            seeder.execute()


    # for i in range(2):
    #     seeder.add_entity(Worker, 2, {
    #         'level': 3,
    #         'name': lambda x: seeder.faker.name(),
    #         'position': random.choice([role for role in Role.objects.filter(role_level=2)]),
    #         #'parent_id': random.choice([employee.level for employee in Worker.objects.filter(level=1)]),
    #         'email': lambda x: seeder.faker.email(),
    #         'tree_id': 3,
    #         })
    #     seeder.execute()

create_ceo_role()
create_ceo()
#create_second_roles()
create_roles()

#create_workers_of_second_roles()
#create_workers_of_third_roles()
create_workers()
    # for i in range(2):
    #     seeder.add_entity(Worker, 1, {
    #         'level': lambda x: random.randint(2, 7),
    #         'name': lambda x: seeder.faker.name(),
    #         'position': random.choice([role for role in Role.objects.all()]),
    #         # 'parent_id': lambda x: random.randint(1, 7),
    #         # 'email': lambda x: seeder.faker.email(),
    #         })
    #     seeder.execute()


#create_ceo_role()
#create_ceo()

# create_employees()