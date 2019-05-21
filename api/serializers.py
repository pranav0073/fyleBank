from rest_framework import serializers
from .models import Bank, Branch


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ( 'name','id')
        
class BranchSerializer(serializers.HyperlinkedModelSerializer):
    bank = BankSerializer(source= "bank_id")
    class Meta:
        model = Branch
        depth =1
        
        fields = ('id', 'branch','ifsc','address','city','state', 'bank')