from random import randint

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker

from petition.models import Petition


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(10):
            f_name = self.fake.first_name()
            l_name = self.fake.last_name()
            email = f"{f_name}.{l_name}@mail.com"
            user = User.objects.create_user(
                username=f"{f_name}_{l_name}".lower(),
                email=email,
                password="A@123456",
                first_name=f_name,
                last_name=l_name,
            )
            user.save()

            for _ in range(10):
                petition = Petition.objects.create(
                    title=self.fake.paragraph(nb_sentences=1),
                    description=self.fake.paragraph(nb_sentences=100),
                    owner=user,
                    goal=randint(100, 1000000),
                )
                petition.save()
