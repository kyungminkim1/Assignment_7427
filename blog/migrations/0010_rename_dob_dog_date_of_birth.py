# Generated by Django 3.2.9 on 2021-11-01 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_dog_breed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]
