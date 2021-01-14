# Generated by Django 3.1.2 on 2021-01-14 08:40

from django.db import migrations, models


def populate_end_time_on_next_day(apps, schema_editor):
    TimeSpan = apps.get_model("hours", "TimeSpan")

    for time_span in TimeSpan.objects.all():
        if time_span.start_time and time_span.end_time:
            time_span.end_time_on_next_day = time_span.end_time <= time_span.start_time
            time_span.save(update_fields=["end_time_on_next_day"])


class Migration(migrations.Migration):

    dependencies = [
        ("hours", "0011_add_timezone_to_resource"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicaltimespan",
            name="end_time_on_next_day",
            field=models.BooleanField(
                default=False, verbose_name="Is end time on the next day"
            ),
        ),
        migrations.AddField(
            model_name="timespan",
            name="end_time_on_next_day",
            field=models.BooleanField(
                default=False, verbose_name="Is end time on the next day"
            ),
        ),
        migrations.RunPython(
            populate_end_time_on_next_day, reverse_code=migrations.RunPython.noop
        ),
    ]