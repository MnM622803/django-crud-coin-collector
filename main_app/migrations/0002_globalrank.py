
import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GlobalRank",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("rank", models.IntegerField()),
                ("source", models.CharField(max_length=100, blank=True)),
                (
                    "coin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main_app.coin"
                    ),
                ),
            ],
        ),
    ]
