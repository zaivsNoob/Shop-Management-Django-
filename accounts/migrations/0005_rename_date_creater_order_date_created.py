# Generated by Django 4.2 on 2023-04-05 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_creater',
            new_name='date_created',
        ),
    ]