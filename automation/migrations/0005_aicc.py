# Generated by Django 2.2.3 on 2019-10-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_auto_20190914_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='AICC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_Name', models.CharField(max_length=25)),
                ('Service_Owner', models.CharField(max_length=25)),
                ('Idea_Date', models.CharField(max_length=25)),
                ('Use_Case', models.TextField(max_length=250)),
                ('Automation_Status', models.CharField(max_length=250)),
                ('Opportunity_charter', models.FileField(blank=True, upload_to='Opportunity_charter')),
            ],
        ),
    ]