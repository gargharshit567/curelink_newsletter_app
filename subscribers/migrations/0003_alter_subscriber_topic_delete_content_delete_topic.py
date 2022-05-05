# Generated by Django 4.0.4 on 2022-05-05 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('subscribers', '0002_content_content_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='topic',
            field=models.ManyToManyField(to='content.topic'),
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]