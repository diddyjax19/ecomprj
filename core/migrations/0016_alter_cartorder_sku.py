# Generated by Django 3.2.7 on 2022-11-16 19:08

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_pid_cartorder_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='sku',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', blank=True, length=5, max_length=20, null=True, prefix='SKU'),
        ),
    ]
