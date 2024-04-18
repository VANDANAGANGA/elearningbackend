# Generated by Django 4.2.6 on 2023-10-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_display_pic_useraccount_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Student'), (3, 'Teacher')], default=3, null=True),
        ),
    ]
