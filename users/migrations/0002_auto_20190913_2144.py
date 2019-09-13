# Generated by Django 2.2.5 on 2019-09-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]