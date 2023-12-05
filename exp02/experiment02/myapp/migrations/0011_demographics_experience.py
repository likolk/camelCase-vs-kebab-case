# Generated by Django 3.2.10 on 2023-12-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_demographics_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='experience',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='advanced', max_length=20),
            preserve_default=False,
        ),
    ]