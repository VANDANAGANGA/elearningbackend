# Generated by Django 4.2.6 on 2023-11-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_rename_experience_teacherprofile_comapany_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='comapany_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='Job_role',
            new_name='job_role',
        ),
    ]
