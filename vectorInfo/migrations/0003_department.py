# Generated by Django 5.0 on 2023-12-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectorInfo', '0002_alter_vectorinfo_describe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
        ),
    ]