
from django.http import HttpResponse
from .models import Bank

def index(request):
    bank = Bank.objects.get(id="40")
    return HttpResponse(bank.name)
# Create your views here.
