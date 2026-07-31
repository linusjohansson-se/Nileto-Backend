from django.db import models

from common.models import AuditModel
from django.conf import settings

class Customer(AuditModel):
    name = models.CharField(max_length=255)
    website = models.URLField(null=False, blank=True)
    note = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

class Contact(AuditModel):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            default=None)
    note = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

class CustomerAddress(AuditModel):
    primary = models.BooleanField(default=False, null=False, blank=False)
    nickname = models.CharField(max_length=70, null=False, blank=True)
    street_address = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=True)
    zipcode = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=False, blank=False)
    note = models.TextField(null=False, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")

    class Meta(AuditModel.Meta):
        abstract = False
        constraints = [
                models.UniqueConstraint(
                    fields=["customer"],
                    condition=models.Q(primary=True),
                    name="only_one_primary_address_per_customer"
                    ),
                ]


class CustomerContact(AuditModel):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="customer_links")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="contact_links")
    primary_contact = models.BooleanField(default=False, null=False, blank=False)
    role_description = models.CharField(max_length=255, null=False, blank=True)
    
    class Meta(AuditModel.Meta):
        abstract = False
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "contact"],
                name="unique_customer_contact",
            ),
            models.UniqueConstraint(
                fields=["customer"],
                condition=models.Q(primary_contact=True),
                name="only_one_primary_contact_per_customer",
            ),
        ]

class ContactEmail(AuditModel):
    email = models.EmailField(null=False, blank=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="emails")
    primary = models.BooleanField(null=False, blank=False, default=False)
    
    class Meta(AuditModel.Meta):
        abstract = False
        constraints = [
            models.UniqueConstraint(
                fields=["contact"],
                condition=models.Q(primary=True),
                name="only_one_primary_email_per_contact",
            ),
            models.UniqueConstraint(
                fields=["email"],
                name="email_has_to_be_unique"
            ),
        ]

    def __str__(self) -> str:
        return self.email

class ContactPhone(AuditModel):
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="phone_numbers")
    primary = models.BooleanField(null=False, blank=False, default=False)

    class Meta(AuditModel.Meta):
        abstract = False
        constraints = [
            models.UniqueConstraint(
                fields=["contact"],
                condition=models.Q(primary=True),
                name="only_one_primary_phone_per_contact",
            ),
            models.UniqueConstraint(
                fields=["phone_number"],
                name="phone_number_has_to_be_unique",
            ),
        ]
    
    def __str__(self) -> str:
        return f"({self.phone_number}"
