# Generated by Django 4.2.11 on 2024-08-08 19:52

import ansible_base.resource_registry.models.service_identifier
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dab_resource_registry', '0004_remove_resourcetype_migrated'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='is_partially_migrated',
            field=models.BooleanField(default=False, help_text="This gets set to True when a resource has been copied into the resource server, but the service_id hasn't been updated yet."),
        ),
        migrations.AlterField(
            model_name='resource',
            name='service_id',
            field=models.UUIDField(default=ansible_base.resource_registry.models.service_identifier.service_id, help_text='ID of the service responsible for managing this resource.'),
        ),
    ]
