# Generated by Django 2.2.2 on 2019-06-05 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('quantidade_musica', models.IntegerField()),
                ('seconds', models.IntegerField()),
            ],
            options={
                'db_table': 'album',
            },
        ),
    ]