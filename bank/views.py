

import json
from django.http import HttpResponse

def index(request):
    response ={}
    response["title"] = "Fyle Backend Challenge"
    response["author"] = "Pranav Prahsant"
    response["Date"] = "21 - May - 2019"
    response["email"] = "pranav0073@gmail.com"
    response["apis"] = list()
    response["apis"].append({
        
        "title" : "Bank City Branches",
        "api" : "https://fylebankapp.herokuapp.com/api/bank/?name=Bank Name&city=City Name",
        "description": "This api accepts bank name and city name as parameters and returns the list of branches for the same comibnation",
        "Examples": [
            "https://fylebankapp.herokuapp.com/api/bank/?name=ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED&city=THANE",
            "https://fylebankapp.herokuapp.com/api/bank/?name=THE%20ROYAL%20BANK%20OF%20SCOTLAND%20N%20V&city=AGRA",
            "https://fylebankapp.herokuapp.com/api/bank/?name=ALLAHABAD%20BANK&city=KHERI"
            
        ]
    })
    response["apis"].append({
        
        "title" : "Bank",
        "api" : "https://fylebankapp.herokuapp.com/api/bank/",
        "description": "This api returns all the 170 banks in the database"
    })
    response["apis"].append({
        
        "title" : "Branch",
        "api" : "https://fylebankapp.herokuapp.com/api/branch/",
        "description": "This api returns the first 1000 branch records from the database pool of 7K branches"
    })
    dump = json.dumps(response)
    return HttpResponse(dump, content_type='application/json')
    