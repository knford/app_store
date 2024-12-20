# Generated by Django 5.1.3 on 2024-11-20 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_due_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('obtained', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(4, 0)),
        ),
        migrations.AddField(
            model_name='task',
            name='items_needed',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='tasks.item'),
        ),
    ]
