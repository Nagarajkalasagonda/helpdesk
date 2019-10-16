from django.db import models
from django.contrib.auth.models import User

asset_status=(
('Instock','Instock'),
('Allocate','Allocate'),
('Scarp','Scarp'),    
)
ticket_status=(
('New','New'),
('Allocate','Allocate'),
('Reject','Reject'),    
('Close','Close'),    

)

priority_type=(
    ('High','High'),
    ('Low','Low'),
    ('Medium','Medium'),
)
# Create your models here.
class Location(models.Model):
    locationid = models.IntegerField()
    locationname = models.CharField(max_length=50)
    def __str__(self):
        return self.locationname

class Department(models.Model):
    departmentid = models.IntegerField()
    departmentname = models.CharField(max_length=50)
    def __str__(self):
        return self.departmentname

class EmployeeType(models.Model):
    type=models.CharField(max_length=100)

class Employee(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.PROTECT)
    type=models.ForeignKey(EmployeeType,on_delete=models.PROTECT,null=True)
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    def __str__(self):
        return self.eid

class AssetMaster(models.Model):
    assetnumber = models.CharField(max_length=100)
    assettype = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    status = models.CharField(max_length=20,choices=asset_status,null=True,blank=True)
    owner = models.ForeignKey(Employee, on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return self.assetnumber

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    assetnumber = models.ForeignKey(AssetMaster, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT,null=True)
    priority = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True,null=True)
    lastdate=models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=20,choices=ticket_status,default='New',null=True,blank=True)
    

    
    def __str__(self):
        return self.title