import csv
import os
from .models import Bank, Branch


def insertBank():
    with open(os.getcwd()+ '/api/bank.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        banks = []
        for row in spamreader:
            if not row == "":
                banks.append(Bank(name=row[0], id=row[1]))
                print(row)
        Bank.objects.bulk_create(banks)
    
    
    banks = Bank.objects.all()
        
    bank_map = {}
    for bank in banks:
        bank_map[bank.id] = bank
    
    #ifsc,bank_id,branch,address,city,district,state,bank_name
   
    with open(os.getcwd()+ '/api/bank_branches.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        branches = []
        for row in spamreader:
            if not row == "":
                print(row[1])
                x = row[1]
                bid = bank_map[int(x)]
                branches.append(Branch(ifsc=row[0], bank_id=bid, branch=row[2],
                                       address=row[3], city=row[4], district = row[5],
                                       state=row[6]))
                
        Branch.objects.bulk_create(branches)
          
        