# Generated by Django 2.2.2 on 2019-06-06 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='seconds',
        ),
        migrations.AddField(
            model_name='album',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
