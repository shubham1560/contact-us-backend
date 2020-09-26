from sys_user.models import SysUser
from domain.models import Domain
from rest_framework.authtoken.models import Token


def create_root_user(domain, **validated_data, ) -> SysUser:
    # breakpoint()
    domain_user = Domain()
    domain_user.name = domain
    domain_user.parent = Domain.objects.get_or_create(name="TOP")[0]
    domain_user.save()
    # domain.name = requet.
    try:
        SysUser.objects.create_user(**validated_data,
                                    email=validated_data['username'],
                                    domain=domain_user,
                                    is_active=False,)
        # try:
        #     send_confirmation_mail(email=validated_data['username'], token=str(token))
        # except ObjectDoesNotExist:
        #     log_random("The mail is not reaching, check if the mail exists or not, the mailing is failing")
        #     return False
        return True
    except Exception as e:
        return False
