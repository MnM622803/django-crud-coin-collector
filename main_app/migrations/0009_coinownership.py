from django.db import migrations

class Migration(migrations.Migration):
	"""Restored no-op placeholder migration 0009.
	Previously created CoinOwnership; model removed so keep as empty.
	"""

	dependencies = [
		('main_app', '0008_coin_owner'),
	]

	operations = []
