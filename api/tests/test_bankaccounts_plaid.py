from django.conf import settings
from django.urls import reverse_lazy
from django.test import TestCase, override_settings

from dotenv import parse_dotenv, read_dotenv
from mixer.backend.django import mixer
from mock import patch
import os
import plaid

from api.models import BankAccount


class BankAccountTestSuite(TestCase):
    """
    Endpoint test Plaid
    """

    def setUp(self):
        read_dotenv()
        self.user = mixer.blend('auth.User')
        self.user.set_password('pass1234')
        self.user.save()
        profilekwargs = {
            'user': self.user,
        }
        profile = mixer.blend('api.Profile', **profilekwargs)
        profile.save()

    @patch('plaid.api.item.PublicToken.exchange', return_value={'access_token': '1234'})
    @patch('plaid.api.auth.Auth.get',
           return_value={
               "accounts": [{"name": "Test Bank Account", "account_id": "123123123"}],
               "numbers": {
                   "ach": [
                       {"account": "123412341234", "account_id": "123123123", "routing": "12341234123",
                        "wire_routing": "21341234213"}
                   ]}})
    def test_register_account(self, mocked_plaid_item, mocked_plaid_auth):
        self.client.force_login(self.user)
        data = {
            "public_token": "public-development-397dd0e2-e48d-41c3-b022-9f392cf44bc6",
        }
        url = reverse_lazy('api:api-bank-accounts')
        response = self.client.post(url, data, content_type="application/json")
        accounts_len = BankAccount.objects.all().count()
        self.assertEqual(accounts_len > 0, True, response.content)
