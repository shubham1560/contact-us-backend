# from .models import Domain
from .services import get_domain_code, get_api_key


def before_insert_domain(current_object):
    # breakpoint()

    if current_object.id:
        """
        If the object already has the id, then the object is being updated, so the logic after updating should
        go here
        """
        pass

    if not current_object.id:
        current_object.domain_code = get_domain_code(3) + '/'
        if current_object.parent:
            current_object.domain_path = current_object.parent.domain_path + current_object.domain_code
        else:
            current_object.domain_path = current_object.domain_code
        current_object.api_key = get_api_key(32)
        """
        If there is not id for the object, then the object is being inserted and new insertion logic should 
        go here to bifurcate the requests
        """
        # current_object.
        pass

    return current_object


def after_insert_domain(current_object):
    """
    If there is any logic that has to run after the object has been saved, maybe based on the object or any
    notification changes, it can be done here
    """
    # breakpoint()
    return


def before_insert_domain_preference(current_object):
    # breakpoint()

    if current_object.id:
        """
        If the object already has the id, then the object is being updated, so the logic after updating should
        go here
        """
        pass

    if not current_object.id:
        """
        If there is not id for the object, then the object is being inserted and new insertion logic should 
        go here to bifurcate the requests
        """
        # current_object.
        pass

    return current_object


def after_insert_domain_preference(current_object):
    """
    If there is any logic that has to run after the object has been saved, maybe based on the object or any
    notification changes, it can be done here
    """
    # breakpoint()
    return
