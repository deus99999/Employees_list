# Generated by Django 4.2.2 on 2023-06-29 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_role_role_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='manager',
            new_name='parent',
        ),
    ]