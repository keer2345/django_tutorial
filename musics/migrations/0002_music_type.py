# Generated by Django 2.0.5 on 2018-05-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='type',
            field=models.CharField(choices=[('T1', 'type 1'), ('T2', 'type 2'), ('T3', 'type 3'), ('T4', 'type 4')], default='T1', max_length=2),
        ),
    ]
