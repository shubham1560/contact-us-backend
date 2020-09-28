# from .models import SysUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
# from domain_preference.models import DomainPreference


def before_insert(current_object):
    # breakpoint()

    if current_object.id:
        if current_object.domain:
            current_object.domain_path = current_object.domain.domain_path

        """
        If the object already has the id, then the object is being updated, so the logic after updating should
        go here
        """
        pass

    if not current_object.id:
        # token = Token(user=current_object)
        # token.save()
        if current_object.domain:
            current_object.domain_path = current_object.domain.domain_path
        """
        If there is not id for the object, then the object is being inserted and new insertion logic should 
        go here to bifurcate the requests
        """
        # current_object.
        pass

    return current_object


def after_insert(current_object):
    """
    If there is any logic that has to run after the object has been saved, maybe based on the object or any
    notification changes, it can be done here
    """
    # if not current_object.id:
    # breakpoint()
    # try:
    #     DomainPreference.objects.get(user=current_object, domain_path=current_object.domain_path)
    # except ObjectDoesNotExist:
    #     preference = DomainPreference(user=current_object)
    #     preference.save()

    try:
        Token.objects.get(user=current_object)
        return
    except ObjectDoesNotExist:
        token = Token(user=current_object)
        token.save()
    # breakpoint()
    return
