# Generated by Django 4.0.10 on 2023-09-14 19:25

# Django
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aa_survey", "0008_rename_surveychoice_choice"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SurveyForm",
            new_name="Form",
        ),
    ]
