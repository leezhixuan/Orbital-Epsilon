# Generated by Django 3.2.3 on 2021-05-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210525_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=None, upload_to='path/to/img'),
        ),
    ]
