# Generated by Django 4.2 on 2023-04-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='rawtweet',
            field=models.CharField(max_length=300, null=True),
        ),
    ]