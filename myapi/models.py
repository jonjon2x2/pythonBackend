import uuid
from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=320)
    phone_no = models.CharField(max_length=12)
    address = models.CharField(max_length=30)
    postcode = models.CharField(max_length=5)
    state = models.CharField(max_length=30)

    class Meta:
        db_table = "customers"

        def __str__(self) -> str:
            return self.title