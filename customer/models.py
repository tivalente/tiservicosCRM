from django.db import models
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(db_column="first_name", max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    area_code = models.CharField(max_length=3, blank=True, null=True)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    coutry = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Ensure the first_name is stored in uppercase.
        This enforces the requirement that first_name is always saved as
        uppercase letters regardless of how the value was provided.
        """
        if self.first_name:
            # Normalize to string and uppercase (defensive: strip whitespace)
            self.first_name = str(self.first_name).strip().upper()

        if self.last_name:
            self.last_name = str(self.last_name).strip().upper()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    def get_full_phone_number(self):
        if self.area_code and self.phone_number:
            return f"({self.area_code}) {self.phone_number}"
        return None

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "tb_customer"
