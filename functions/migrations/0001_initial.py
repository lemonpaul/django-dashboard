# Generated by Django 2.2.6 on 2019-11-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=200)),
                ('interval', models.IntegerField(default=0)),
                ('step', models.IntegerField(default=0)),
            ],
        ),
    ]