# Generated by Django 4.2.9 on 2024-02-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="addres1",
            new_name="address1",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="addres2",
            new_name="address2",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="modified_date",
            new_name="date_modified",
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]