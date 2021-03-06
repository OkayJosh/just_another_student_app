# Generated by Django 2.1.7 on 2019-05-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absencerecord',
            name='date_of_review',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='appraisal',
            name='date_of_appraisal',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_of_attendance',
            field=models.DateField(auto_now_add=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_of_collection',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date_of_review',
            field=models.DateField(auto_now_add=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='incentive',
            name='date_of_collection_of_incentive',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='literacy',
            name='date_of_accessment',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='outofschool',
            name='date_of_review',
            field=models.DateField(auto_now_add=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_of_posting',
            field=models.DateField(help_text='YYYY-MM-DD', verbose_name='Date of Posting'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_admision',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
    ]
