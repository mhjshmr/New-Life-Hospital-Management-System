from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from new_life.constants import PERMISSIONS, GROUPS

class Command(BaseCommand):
    help = 'Create the groups required in the system'

    def handle(self, *args, **options):
        permissions = Permission.objects.all()
        for group in GROUPS:
            group_obj, created = Group.objects.get_or_create(name=group)
            # True if created, False if it is fetched
            if created:
                for permission in permissions:
                    if permission.codename in PERMISSIONS[group]:
                        group_obj.permissions.add(permission)
