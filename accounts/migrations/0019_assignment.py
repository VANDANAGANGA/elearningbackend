# Generated by Django 4.2.6 on 2023-12-05 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_module_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_no', models.IntegerField()),
                ('assignment_title', models.CharField()),
                ('pdf', models.FileField(upload_to='assignments/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
            ],
        ),
    ]
