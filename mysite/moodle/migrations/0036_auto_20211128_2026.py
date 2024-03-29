# Generated by Django 3.2.8 on 2021-11-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0035_grading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(default='', max_length=100)),
                ('uploadag', models.FileField(upload_to='media/uploadag')),
                ('ag_for', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='uploada',
            name='is_ag',
            field=models.IntegerField(default=0),
        ),
    ]
