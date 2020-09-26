from .models import ContactForm
from api.fetch_record import FetchRecord
from domain.models import Domain
from domain_preference.models import DomainPreference


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


def get_related_forms_records(request, start, end):
    # breakpoint()
    gr = FetchRecord('ContactForm')
    gr.add_active_query()
    gr.add_query('domain_path', 'contains', request.user.domain_path)
    gr.choose_window(start, end)
    gr.order_by_desc("sys_created_on")
    result = gr.query()
    # breakpoint()
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




