# Generated by Django 4.0.10 on 2023-09-14 19:26

# Django
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aa_survey", "0009_rename_surveyform_form"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SurveyResponse",
            new_name="Response",
        ),
    ]
