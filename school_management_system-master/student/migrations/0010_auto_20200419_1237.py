# Generated by Django 3.0.3 on 2020-04-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20200419_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=252109, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='enrolledstudent',
            unique_together={('student', 'date')},
        ),
    ]