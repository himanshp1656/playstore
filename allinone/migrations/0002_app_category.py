# Generated by Django 5.1 on 2024-08-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='category',
            field=models.CharField(default='game', max_length=100),
            preserve_default=False,
        ),
    ]
