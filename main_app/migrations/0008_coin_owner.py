from django.db import migrations


class Migration(migrations.Migration):
	"""Restored no-op placeholder migration 0008.
	Keeps sequence continuity after prior experimental changes were reverted.
	"""

	dependencies = [
		('main_app', '0007_coin_image'),
	]

	operations = []
