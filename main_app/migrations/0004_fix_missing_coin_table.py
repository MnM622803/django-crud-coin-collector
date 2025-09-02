from django.db import migrations

def forwards(apps, schema_editor):
    connection = schema_editor.connection
    tables = set(connection.introspection.table_names())
    cursor = connection.cursor()
    if 'main_app_coin' not in tables and 'main_app_cat' in tables:
        cursor.execute('ALTER TABLE main_app_cat RENAME TO main_app_coin;')

def backwards(apps, schema_editor):
    connection = schema_editor.connection
    tables = set(connection.introspection.table_names())
    cursor = connection.cursor()
    if 'main_app_cat' not in tables and 'main_app_coin' in tables:
        cursor.execute('ALTER TABLE main_app_coin RENAME TO main_app_cat;')

class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0003_alter_globalrank_options_alter_globalrank_date'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
