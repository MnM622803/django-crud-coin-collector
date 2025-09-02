from django.db import migrations

def forwards(apps, schema_editor):
    connection = schema_editor.connection
    existing = set(connection.introspection.table_names())
    cursor = connection.cursor()
    if 'main_app_feeding' in existing and 'main_app_globalrank' in existing:
        cursor.execute('DROP TABLE main_app_feeding;')



def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0004_fix_missing_coin_table'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
