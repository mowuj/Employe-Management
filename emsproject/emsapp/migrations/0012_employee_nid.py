# Generated by Django 3.2.9 on 2021-12-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0011_rename_user_id_employee_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='nid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
