# Generated by Django 2.2.3 on 2019-09-14 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='Opurtunity_charter',
            field=models.FileField(default='', upload_to='Opurtunity_charter'),
            preserve_default=False,
        ),
    ]
