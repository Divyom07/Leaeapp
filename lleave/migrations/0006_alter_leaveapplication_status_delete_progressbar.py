# Generated by Django 4.0 on 2022-06-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lleave', '0005_gender_martial_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
        migrations.DeleteModel(
            name='ProgressBar',
        ),
    ]
