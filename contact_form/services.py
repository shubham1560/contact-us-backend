from .models import ContactForm
from api.fetch_record import FetchRecord
from domain.models import Domain
from domain_preference.models import DomainPreference
from rest_framework.exceptions import ValidationError


def insert_contact_data(request):
    # breakpoint()
    domain = get_domain(request.META['HTTP_API_KEY'])
    gr = ContactForm()
    gr.name = request.POST.get('name', '')
    gr.anything_else = request.POST.get('anything_else', '')
    gr.email = request.POST.get('email', '')
    gr.country = request.POST.get('country', '')
    gr.first_name = request.POST.get('first_name', '')
    gr.last_name = request.POST.get('last_name', '')
    gr.message = request.POST.get('message', '')
    gr.subject = request.POST.get('subject', '')
    gr.domain = domain
    gr.save()


def get_related_forms_records(request, start, end, message_type):
    # breakpoint()
    gr = FetchRecord('ContactForm')
    gr.add_active_query()
    gr.add_query('domain_path', 'contains', request.user.domain_path)
    gr.choose_window(start, end)
    gr.order_by_desc("sys_created_on")
    if message_type == "all":
        pass
    elif message_type == "important":
        gr.add_query('important', True)
    elif message_type == "read":
        gr.add_query('read', True)
    elif message_type == "unread":
        gr.add_query('read', False)
    elif message_type == "starred":
        gr.add_query('starred', True)
    result = gr.query()
    return result


def get_domain(api_key):
    gr = FetchRecord('Domain')
    # gr.add_active_query()
    gr.add_query('api_key', api_key)
    domain = gr.query()
    if domain:
        return domain[0]
    else:
        return Domain.objects.filter(default=True)[0]


def get_preference_array(request):
    # breakpoint()
    preference = DomainPreference.objects.filter(domain_path=request.user.domain_path, device_type="DLD")
    return preference


def change_field_value(request):
    # breakpoint()

    value = request.data['value']
    field = request.data['field']
    update_ = {field: value}
    # breakpoint()
    try:
        ContactForm.objects.filter(id=request.data['id'], domain_path=request.user.domain_path).update(**update_)
        return field, value, request.data['id']
    except ValidationError:
        return False


def get_contact_form_count(request, message_type):
    if message_type == "all":
        row_count = ContactForm.objects.filter(domain_path__contains=request.user.domain_path, active=True).count()
    if message_type == "important":
        row_count = ContactForm.objects.filter(domain_path__contains=request.user.domain_path,
                                               active=True, important=True).count()
    if message_type == "read":
        row_count = ContactForm.objects.filter(domain_path__contains=request.user.domain_path,
                                               read=True, active=True).count()

    if message_type == "unread":
        row_count = ContactForm.objects.filter(domain_path__contains=request.user.domain_path, active=True,
                                               read=False).count()

    if message_type == "starred":
        row_count = ContactForm.objects.filter(domain_path__contains=request.user.domain_path, starred=True, active=True
                                               ).count()
    return row_count


def delete_mass_contact_form(request):
    # breakpoint()
    forms = ContactForm.objects.filter(id__in=request.data['ids'], domain_path__contains=request.user.domain_path)
    forms.delete()
    return forms
    pass
