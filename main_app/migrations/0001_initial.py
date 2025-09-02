
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
