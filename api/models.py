from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    id = models.BigIntegerField(null=False, db_index=True, primary_key=True)
    pass

class Branch(models.Model):
    ifsc = models.CharField(max_length=255, db_index=True, null=False)
    branch = models.CharField(max_length=255)
    adddress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_id = models.ForeignKey('Bank',on_delete=models.DO_NOTHING,null=True,blank=True)
    pass
