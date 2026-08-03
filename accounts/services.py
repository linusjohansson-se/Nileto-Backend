from django.db import transaction
from accounts.models import User
from business.models import Staff

@transaction.atomic
def create_staff_user(email, password, **extra_fields) -> int:
    user = User.objects.select_related("staff").filter(email__iexact=email).first()
    
    if user is not None:
        try:
            staff = user.staff
        except Staff.DoesNotExist:
            staff = None

        if staff is not None:
            return user.pk
        #Create staff record here

    user = User.objects.create_user(email, password, **extra_fields)

    return user.pk

def create_contact_user():
    return

def remove_staff_user():
    return

def remove_contact_user():
    return
