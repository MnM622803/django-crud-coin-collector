
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_globalrank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalrank',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='globalrank',
            name='date',
            field=models.DateField(verbose_name='Ranking Date'),
        ),
    ]
