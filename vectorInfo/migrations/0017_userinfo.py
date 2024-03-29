# Generated by Django 5.0 on 2024-01-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectorInfo', '0016_monitorinfo_far'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=64, verbose_name='用户账号')),
                ('password', models.CharField(max_length=64, verbose_name='用户密码')),
                ('phone', models.CharField(max_length=64, verbose_name='手机号')),
                ('role', models.SmallIntegerField(max_length=32, verbose_name='角色')),
            ],
        ),
    ]
