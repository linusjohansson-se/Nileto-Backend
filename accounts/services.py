from django.db import transaction
from accounts.models import User
from business.models import Staff
from customers.models import Contact

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
            staff.save()

            user.is_active = True
            user.save()

        return user.pk

    user = User.objects.create_user(email, password, **user_fields)

    staff = Staff.objects.get(pk=staff_id)

    if staff.user_id not in (None, user.pk):
        raise ValueError("Staff record already has a different user login connected")

    staff.user = user
    staff.save()

    return user.pk

@transaction.atomic
def create_contact_user(email, password, contact_id, **user_fields) -> int:
    """
    Creates a user login for a contact. Does not create the contact.
    """
    user = User.objects.select_related("contact").filter(email__iexact=email).first()
    
    if user is not None:
        try:
            contact = user.contact
        except Contact.DoesNotExist:
            contact = None

        if contact is not None and contact.pk != contact_id:
            raise ValueError("Contact login for the email provided already exists")
        elif contact is None:
            contact = Contact.objects.get(pk=contact_id)
            
            if contact.user_id not in (None, user.pk):
                raise ValueError("Contact record already has a different user login connected")

            contact.user = user
            contact.save()

            user.is_active = True
            user.save()

        return user.pk

    user = User.objects.create_user(email, password, **user_fields)

    contact = Contact.objects.get(pk=contact_id)

    if contact.user_id not in (None, user.pk):
        raise ValueError("Contact record already has a different user login connected")

    contact.user = user
    contact.save()

    return user.pk

@transaction.atomic
def remove_user_for_staff(staff_id) -> bool:
    """
    Removes the user account relationship for the staff memeber.
    If the user account does not have any relationsships left, it will be deactivated.
    """
    staff = Staff.objects.select_related("user").get(pk = staff_id)
    
    user = staff.user

    if user is None:
        return True

    staff.user = None
    staff.save()
    
    contact_exist = Contact.objects.filter(user=user).exists()
    
    if not contact_exist:
        user.is_active = False
        user.save()

    return True

@transaction.atomic
def remove_contact_user(contact_id) -> bool:
    """
    Removes the user account relationship for the contact.
    If the user account does not have any relationsships left, it will be deactivated.
    """
    contact = Contact.objects.select_related("user").get(pk = contact_id)
    
    user = contact.user

    if user is None:
        return True

    contact.user = None
    contact.save()
    
    staff_exist = Staff.objects.filter(user=user).exists()
    
    if not staff_exist:
        user.is_active = False
        user.save()

    return True
