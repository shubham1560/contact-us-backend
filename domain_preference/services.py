from .models import DomainPreference


def change_domain_preference(request):
    obj, created = DomainPreference.objects.update_or_create(
        user=request.user,
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
        }
    )
