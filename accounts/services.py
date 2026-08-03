from django.db import transaction
from accounts.models import User
from business.models import Staff

@transaction.atomic
def create_user_for_staff(email, password, staff_id, **user_fields) -> int:
    """
    Creates a user login for a staff member. Does not create the staff entry.
    """
    user = User.objects.select_related("staff").filter(email__iexact=email).first()
    
    if user is not None:
        try:
            staff = user.staff
        except Staff.DoesNotExist:
            staff = None

        if staff is not None and staff.pk != staff_id:
            raise ValueError("Staff login for the email provided already exists")
        elif staff is None:
            staff = Staff.objects.get(pk=staff_id)
            
            if staff.user_id not in (None, user.pk):
                raise ValueError("Staff record already has a different user login connected")

            staff.user = user
            staff.save(update_fields=["user"])

        return user.pk

    user = User.objects.create_user(email, password, **user_fields)

    staff = Staff.objects.get(pk=staff_id)

    if staff.user_id not in (None, user.pk):
        raise ValueError("Staff record already has a different user login connected")

    staff.user = user
    staff.save(update_fields=["user"])

    return user.pk

def create_contact_user():
    return

def remove_staff_user():
    return

def remove_contact_user():
    return
