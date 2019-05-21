
import json
from django.http import HttpResponse
from .models import Bank, Branch

def index(request):
    branch = Branch.objects.first()
    response_data = {}
    response_data['ifsc'] = branch.ifsc
    response_data['branch'] = branch.branch
    response_data['address'] = branch.address
    response_data['city'] = branch.city
    response_data['district'] = branch.district
    response_data['state'] = branch.state
    response_data['bank_name'] = branch.bank_id.name
    response_data['bank_id'] = branch.bank_id.id
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")
# Create your views here.
