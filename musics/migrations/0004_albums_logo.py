# Generated by Django 3.2.5 on 2021-08-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_auto_20210811_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='logo',
            field=models.CharField(default=1, max_length=99999),
            preserve_default=False,
        ),
    ]
