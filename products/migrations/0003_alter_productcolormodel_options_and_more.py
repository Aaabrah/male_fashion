# Generated by Django 4.1.2 on 2022-11-08 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productbrandmodel_productmodel_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcolormodel',
            options={'verbose_name': 'color', 'verbose_name_plural': 'colors'},
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='colord',
            new_name='colors',
        ),
    ]
