from sys_user.models import SysUser
from rest_framework.authtoken.models import Token


def create_root_user(**validated_data) -> SysUser:
    # breakpoint()
    try:
        SysUser.objects.create_user(**validated_data,
                                    email=validated_data['username'],

                                    is_active=False,)
        # try:
        #     send_confirmation_mail(email=validated_data['username'], token=str(token))
        # except ObjectDoesNotExist:
        #     log_random("The mail is not reaching, check if the mail exists or not, the mailing is failing")
        #     return False
        return True
    except Exception as e:
        return False
