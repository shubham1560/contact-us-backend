from .models import ContactForm
from api.fetch_record import FetchRecord


def insert_contact_data(request):
    gr = ContactForm()
    gr.name = request.POST.get('name', '')
    gr.anything_else = request.POST.get('anything_else', '')
    gr.email = request.POST.get('email', '')
    gr.country = request.POST.get('country', '')
    gr.first_name = request.POST.get('first_name', '')
    gr.last_name = request.POST.get('last_name', '')
    gr.message = request.POST.get('message', '')
    gr.subject = request.POST.get('subject', '')
    gr.save()


def get_related_forms_records(request):
    gr = FetchRecord('ContactForm')
    gr.add_active_query()
    pass