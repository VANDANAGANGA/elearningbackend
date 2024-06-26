# Generated by Django 4.2.6 on 2023-12-20 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_at', models.DateTimeField(auto_now=True)),
                ('answer', models.FileField(upload_to='studentassignments/')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile')),
            ],
        ),
    ]
