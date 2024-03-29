from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@gmail.com',
            is_superuser=True,
            is_staff=True,
        )
        user.set_password('admin')
        user.save()
