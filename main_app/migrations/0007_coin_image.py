from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_transform_cat_to_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='coin_images/'),
        ),
    ]
