# Generated by Django 2.2.6 on 2019-10-23 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entryitem',
            options={'ordering': ['-date']},
        ),
    ]