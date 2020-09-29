from django.core.exceptions import ObjectDoesNotExist

from .models import DomainPreference


def change_domain_preference(request, device_type):
    obj, created = DomainPreference.objects.update_or_create(
        user=request.user,
        domain=request.user.domain,
        device_type=device_type,
        defaults={
            "email": request.data["email"],
            'domain': request.user.domain,
            "first_name": request.data["first_name"],
            "last_name": request.data["last_name"],
            "name": request.data["name"],
            "subject": request.data['subject'],
            "message": request.data['message'],
            "anything_else": request.data['anything_else'],
            "phone_number": request.data['phone_number'],
            "device_type": device_type,
            "active": True
        }
    )
    # breakpoint()
    # breakpoint()


def change_domain_preference_field(request):
    value = request.data['value']
    field = request.data['field']
    update_ = {field: value}
    obj, created = DomainPreference.objects.update_or_create(
        user=request.user,
        domain=request.user.domain,
        defaults=update_,
        device_type="DLD"
    )


def get_message_detail_preference(request):
    # breakpoint()
    try:
        preference = DomainPreference.objects.get(
            user=request.user,
            domain=request.user.domain,
            device_type='DFD',
            active=True
        )
    except ObjectDoesNotExist:
        return {
            "first_name": True,
            "last_name": True,
            "name": True,
            "email": True,
            "subject": True,
            "message": True,
            "anything_else": True,
            "phone_number": True,
        }, False
    return preference, True

