# Generated by Django 4.2.16 on 2024-11-21 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.ANSIBLE_BASE_TEAM_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('dab_rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectrole',
            name='provides_teams',
            field=models.ManyToManyField(editable=False, help_text='Users who have this role obtain member access to these teams, and inherit all their permissions.', related_name='member_roles', to=settings.ANSIBLE_BASE_TEAM_MODEL),
        ),
        migrations.AlterField(
            model_name='objectrole',
            name='role_definition',
            field=models.ForeignKey(help_text='The role definition which defines what permissions this object role grants.', on_delete=django.db.models.deletion.CASCADE, related_name='object_roles', to='dab_rbac.roledefinition'),
        ),
        migrations.AlterField(
            model_name='objectrole',
            name='teams',
            field=models.ManyToManyField(help_text='Teams or groups who have access to the permissions defined by this object role.', related_name='has_roles', through='dab_rbac.RoleTeamAssignment', to=settings.ANSIBLE_BASE_TEAM_MODEL),
        ),
        migrations.AlterField(
            model_name='objectrole',
            name='users',
            field=models.ManyToManyField(help_text='Users who have access to the permissions defined by this object role.', related_name='has_roles', through='dab_rbac.RoleUserAssignment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roledefinition',
            name='content_type',
            field=models.ForeignKey(default=None, help_text='Thw type of resource this can apply to; only used for validation and user assistance.', null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='roledefinition',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date/time this resource was created.'),
        ),
        migrations.AlterField(
            model_name='roledefinition',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who created this resource.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roledefinition',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='The date/time this resource was created.'),
        ),
        migrations.AlterField(
            model_name='roledefinition',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who last modified this resource.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roleevaluation',
            name='codename',
            field=models.TextField(help_text='The name of the permission, giving the action and the model, from the Django Permission model.'),
        ),
        migrations.AlterField(
            model_name='roleevaluation',
            name='role',
            field=models.ForeignKey(help_text='The object role that grants this form of permission.', on_delete=django.db.models.deletion.CASCADE, related_name='permission_partials', to='dab_rbac.objectrole'),
        ),
        migrations.AlterField(
            model_name='roleevaluationuuid',
            name='codename',
            field=models.TextField(help_text='The name of the permission, giving the action and the model, from the Django Permission model.'),
        ),
        migrations.AlterField(
            model_name='roleevaluationuuid',
            name='role',
            field=models.ForeignKey(help_text='The object role that grants this form of permission.', on_delete=django.db.models.deletion.CASCADE, related_name='permission_partials_uuid', to='dab_rbac.objectrole'),
        ),
        migrations.AlterField(
            model_name='roleteamassignment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date/time this resource was created.'),
        ),
        migrations.AlterField(
            model_name='roleteamassignment',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who created this resource.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roleteamassignment',
            name='object_id',
            field=models.TextField(blank=True, help_text='The primary key of the object this assignment applies to; null value indicates system-wide assignment.', null=True),
        ),
        migrations.AlterField(
            model_name='roleteamassignment',
            name='role_definition',
            field=models.ForeignKey(help_text='The role definition which defines permissions conveyed by this assignment.', on_delete=django.db.models.deletion.CASCADE, related_name='team_assignments', to='dab_rbac.roledefinition'),
        ),
        migrations.AlterField(
            model_name='roleuserassignment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date/time this resource was created.'),
        ),
        migrations.AlterField(
            model_name='roleuserassignment',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who created this resource.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roleuserassignment',
            name='object_id',
            field=models.TextField(blank=True, help_text='The primary key of the object this assignment applies to; null value indicates system-wide assignment.', null=True),
        ),
        migrations.AlterField(
            model_name='roleuserassignment',
            name='role_definition',
            field=models.ForeignKey(help_text='The role definition which defines permissions conveyed by this assignment.', on_delete=django.db.models.deletion.CASCADE, related_name='user_assignments', to='dab_rbac.roledefinition'),
        ),
        migrations.AlterField(
            model_name='roledefinition',
            name='content_type',
            field=models.ForeignKey(default=None, help_text='The type of resource this can apply to; only used for validation and user assistance.', null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
