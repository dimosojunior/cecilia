# Generated by Django 3.2.5 on 2022-03-12 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0007_auto_20220311_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='sub1',
            field=models.CharField(blank=True, default='Mathematics', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='sub2',
            field=models.CharField(blank=True, default='English', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='sub3',
            field=models.CharField(blank=True, default='Kiswahili', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='sub4',
            field=models.CharField(blank=True, default='Physics', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='sub5',
            field=models.CharField(blank=True, default='Biology', max_length=200, null=True),
        ),
    ]