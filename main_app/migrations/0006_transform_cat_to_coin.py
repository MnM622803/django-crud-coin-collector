from django.db import migrations, models

def forwards(apps, schema_editor):
    connection = schema_editor.connection
    cursor = connection.cursor()
    tables = set(connection.introspection.table_names())
    if 'main_app_coin' not in tables:
        return
    cursor.execute('PRAGMA table_info(main_app_coin)')
    cols = {row[1]: row for row in cursor.fetchall()}
    if 'year' in cols and 'value' in cols and 'country' in cols:
        return
    cursor.execute('''
        CREATE TABLE main_app_coin_new (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name varchar(100) NOT NULL,
            year integer NOT NULL DEFAULT 0,
            country varchar(100) NOT NULL DEFAULT 'Unknown',
            description text NOT NULL,
            value decimal(10,2) NOT NULL DEFAULT 0.00
        );
    ''')
    if 'breed' in cols and 'age' in cols:
        cursor.execute('''
            INSERT INTO main_app_coin_new (id, name, year, country, description, value)
            SELECT id, name, age as year, breed as country, description, 0.00 as value FROM main_app_coin;
        ''')
    else:
        cursor.execute('''
            INSERT INTO main_app_coin_new (id, name, year, country, description, value)
            SELECT id, name, 0 as year, 'Unknown' as country, description, 0.00 as value FROM main_app_coin;
        ''')
    cursor.execute('DROP TABLE main_app_coin;')
    cursor.execute('ALTER TABLE main_app_coin_new RENAME TO main_app_coin;')


def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0005_drop_legacy_tables'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
