# Generated by Django 4.2.6 on 2023-11-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='country',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='pin',
            field=models.CharField(),
        ),
    ]
