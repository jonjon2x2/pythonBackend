from django.test import Client, TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model
from ..models import Customer

class CustomerViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        customerList = Customer.objects.create(first_name='Big', last_name='Bob', email='sd@gmail.com', phone_no='0133355342',
                                address='Wwqdasd', postcode='23456', state='Uzsa')
        customerList.save()
        self.user = User.objects.create_user(username='user', password='12345')

    def forceAuthenticate(self):
        user = User.objects.get(username='user')
        client = APIClient()
        client.force_authenticate(user=user)
        return client


    def test_view_get_all(self):
        client = self.forceAuthenticate()
        res = client.get('')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_view_get_specific(self):
        client = self.forceAuthenticate()
        res = client.get('/1')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_view_get_specific_fail(self):
        client = self.forceAuthenticate()
        res = client.get('/1000')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_view_post(self):
        client = self.forceAuthenticate()
        body = {
                'first_name': 'Jon Shen',
                'last_name': 'Ong',
                'email': 'ongjonshen@gmail.com',
                'phone_no': '0133755620',
                'address': 'No. 6 JALAN SS17/1E',
                'postcode': '47500',
                'state': 'Selangor'
        }
        res = client.post('', body, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_view_post_fail_invalid_phone_no(self):
        client = self.forceAuthenticate()
        body = {
                'first_name': 'Jon Shen',
                'last_name': 'Ong',
                'email': 'ongjonshen@gmail.com',
                'phone_no': '+90133755620',
                'address': 'No. 6 JALAN SS17/1E',
                'postcode': '47500',
                'state': 'Selangor'
        }
        res = client.post('', body, format='json')
        messages = res.data['message']
        self.assertEqual(str(messages), 'Phone number is invalid')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_post_fail_invalid_email(self):
        client = self.forceAuthenticate()
        body = {
                'first_name': 'Jon Shen',
                'last_name': 'Ong',
                'email': 'ongjonshengmail.com',
                'phone_no': '+60133755620',
                'address': 'No. 6 JALAN SS17/1E',
                'postcode': '47500',
                'state': 'Selangor'
        }
        res = client.post('', body, format='json')
        messages = res.data['message']
        self.assertEqual(str(messages), 'Email format is invalid')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_put(self):
        client = self.forceAuthenticate()
        body = {
                'first_name': 'Jon Shen',
                'last_name': 'Ong',
                'email': 'testest@gmail.com',
                'phone_no': '+60133755620',
                'address': 'No. 6 JALAN SS17/1E',
                'postcode': '47500',
                'state': 'Selangor'
        }
        res = client.put('/1', body, format='json')
        messages = res.data['message']
        self.assertEqual(str(messages), 'Customer with Id: 1 updated successfully')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_view_put_fail(self):
        client = self.forceAuthenticate()
        body = {
                'first_name': 'Jon Shen',
                'last_name': 'Ong',
                'email': 'testest@gmail.com',
                'phone_no': '+60133755620',
                'address': 'No. 6 JALAN SS17/1E',
                'postcode': '47500',
                'state': 'Selangor'
        }
        res = client.put('/100', body, format='json')
        messages = res.data['message']
        self.assertEqual(str(messages), 'Customer with Id: 100 not found')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_view_delete(self):
        client = self.forceAuthenticate()
        res = client.delete('/1')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_view_delete_fail(self):
        client = self.forceAuthenticate()
        res = client.delete('/100')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

