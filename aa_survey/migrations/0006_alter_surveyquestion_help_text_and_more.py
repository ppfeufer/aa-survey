# Generated by Django 4.0.10 on 2023-09-14 19:23

# Django
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aa_survey", "0005_surveyquestion_mandatory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="surveyquestion",
            name="help_text",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="aa_survey.surveyquestion",
            ),
        ),
    ]
