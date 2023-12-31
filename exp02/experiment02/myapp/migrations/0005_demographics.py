# Generated by Django 3.2.10 on 2023-11-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0004_delete_userresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('education', models.CharField(choices=[('high-school', 'High School'), ('bachelors', 'Bachelors'), ('masters', 'Masters'), ('phd', 'PhD'), ('postdoc', 'Postdoc')], max_length=20)),
                ('occupation', models.CharField(choices=[('student', 'Student'), ('engineer', 'Engineer'), ('teacher', 'Teacher')], max_length=20)),
                ('comments', models.TextField(blank=True)),
                ('questions', models.TextField(blank=True)),
                ('answers', models.TextField(blank=True)),
                ('time_taken', models.FloatField(default=0.0)),
            ],
        ),
    ]
