from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Coin


class AuthorizationTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='tester', password='pass12345')
		self.other = User.objects.create_user(username='other', password='pass12345')
		self.coin = Coin.objects.create(name='Test', year=2000, country='Nowhere', description='Desc', value=1.23, owner=self.user)

	def test_guest_redirected_from_create(self):
		resp = self.client.get(reverse('coin-create'))
		self.assertEqual(resp.status_code, 302)
		self.assertIn('/accounts/login/', resp.headers.get('Location', ''))

	def test_guest_redirected_from_update(self):
		resp = self.client.get(reverse('coin-update', args=[self.coin.id]))
		self.assertEqual(resp.status_code, 302)
		self.assertIn('/accounts/login/', resp.headers.get('Location', ''))

	def test_guest_redirected_from_delete(self):
		resp = self.client.get(reverse('coin-delete', args=[self.coin.id]))
		self.assertEqual(resp.status_code, 302)
		self.assertIn('/accounts/login/', resp.headers.get('Location', ''))

	def test_authenticated_can_access_create(self):
		self.client.login(username='tester', password='pass12345')
		resp = self.client.get(reverse('coin-create'))
		self.assertEqual(resp.status_code, 200)

	def test_authenticated_can_access_update(self):
		self.client.login(username='tester', password='pass12345')
		resp = self.client.get(reverse('coin-update', args=[self.coin.id]))
		self.assertEqual(resp.status_code, 200)

	def test_authenticated_can_access_delete(self):
		self.client.login(username='tester', password='pass12345')
		resp = self.client.get(reverse('coin-delete', args=[self.coin.id]))
		self.assertEqual(resp.status_code, 200)

	def test_cannot_modify_someone_elses_coin(self):
		self.client.login(username='other', password='pass12345')
		resp = self.client.get(reverse('coin-update', args=[self.coin.id]))
		self.assertEqual(resp.status_code, 404)

	def test_non_owner_does_not_see_edit_delete(self):
		self.client.login(username='other', password='pass12345')
		resp = self.client.get(reverse('coin-detail', args=[self.coin.id]))
		self.assertNotContains(resp, 'href="' + reverse('coin-update', args=[self.coin.id]) + '"')
		self.assertNotContains(resp, 'href="' + reverse('coin-delete', args=[self.coin.id]) + '"')
