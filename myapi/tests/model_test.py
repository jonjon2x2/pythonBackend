from django.test import TestCase
from ..models import Customer

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(first_name='Big', last_name='Bob', email='sd@gmail.com', phone_no='0133355342',
                                address='Wwqdasd', postcode='23456', state='Uzsa')

    def test_first_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.first_name
        self.assertEqual(field_value, 'Big')
    
    def test_first_name_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('first_name').max_length
        self.assertEqual(field_value, 60)

    def test_last_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.last_name
        self.assertEqual(field_value, 'Bob')
    
    def test_last_name_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('last_name').max_length
        self.assertEqual(field_value, 60)

    def test_email_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_email_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.email
        self.assertEqual(field_value, 'sd@gmail.com')
    
    def test_email_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('email').max_length
        self.assertEqual(field_value, 320)

    def test_phone_no_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')

    def test_phone_no_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.phone_no
        self.assertEqual(field_value, '0133355342')
    
    def test_phone_no_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('phone_no').max_length
        self.assertEqual(field_value, 12)
    
    def test_address_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_address_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.address
        self.assertEqual(field_value, 'Wwqdasd')
    
    def test_address_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('address').max_length
        self.assertEqual(field_value, 30)

    def test_postcode_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('postcode').verbose_name
        self.assertEqual(field_label, 'postcode')

    def test_postcode_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.postcode
        self.assertEqual(field_value, '23456')
    
    def test_postcode_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('postcode').max_length
        self.assertEqual(field_value, 5)
        
    def test_state_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_state_value(self):
        customer = Customer.objects.get(id=1)
        field_value = customer.state
        self.assertEqual(field_value, 'Uzsa')
    
    def test_state_max_length(self):
        customer = Customer.objects.get(id=1)
        field_value = customer._meta.get_field('state').max_length
        self.assertEqual(field_value, 30)