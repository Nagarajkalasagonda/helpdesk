from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

from django.contrib import messages

@login_required(login_url='login')
def createticket(request):
    if request.method=='GET':
        employee=Employee.objects.get(user=request.user)
        assets = AssetMaster.objects.filter(location=employee.location,status='Instock')
        return render(request,"create_ticket_page.html",{'employee':employee,'assets':assets})
    elif request.method=='POST':
        #print('qqqqqqqqq')
        title = request.POST['title']
        description = request.POST['description']
        assetnumber = request.POST['assetnumber']
        priority = request.POST['priority']
        print(title,description,assetnumber,priority)
        date = datetime.datetime.now()
        ticket_db = Ticket.objects.create(title=title,
                    description=description,
                    assetnumber=AssetMaster.objects.get(pk=assetnumber),
                    employee=Employee.objects.get(user=request.user),
                    priority=priority,
                    lastdate=date
                    )
        messages.info(request,'Ticket created succesfully')
        return redirect('/')

@login_required(login_url='login')
def assetlisting(request):
    if request.method=='GET':
        employee=Employee.objects.get(user=request.user)

        if employee.type.pk==2:
            assets = AssetMaster.objects.all().order_by('-pk')
        else:
            assets = AssetMaster.objects.filter(owner =employee)
        return render(request,"assetlisting.html",{'employee':employee,'assets':assets})

@login_required(login_url='login')   
def mytickets(request):
    if request.method=='GET':
        employee=Employee.objects.get(user=request.user)
        #List all tickets 
        if employee.type.pk==2:
            tickets = Ticket.objects.all().order_by('-pk')
        #List my tickets
        else:
            tickets = Ticket.objects.filter(employee__user=request.user)
        return render(request,"mytickets_listing_page.html",{'employee':employee,'tickets':tickets})

    elif request.method == 'POST':
        ticket = request.POST['ticket']
        status = request.POST['status']
        employee=Employee.objects.get(user=request.user)


        
        date = datetime.datetime.now()
        ticket = Ticket.objects.get(pk=ticket)
        """assets=AssetMaster.objects.filter(assetnumber=ticket.assetnumber,status='Instock')

        if assets.exists():
            messages.info(request,str(ticket.assetnumber)+' Asset aleady allocated to '+str(assets[0].owner))
            return redirect('/mytickets')"""


        if status=='Allocate':
            if ticket.assetnumber.status == 'Allocate':
                old_ticket = Ticket.objects.filter(assetnumber__status='Allocate')
                messages.info(request,str(ticket.assetnumber)+' Asset aleady allocated to '+old_ticket[0].employee.ename)
                return redirect('/mytickets')

        ticket.lastdate=date
        ticket.status=status

        if status == 'Allocate':
            ticket.assetnumber.status=status
            ticket.assetnumber.owner=employee
            ticket.assetnumber.save()
        messages.info(request,'Ticket State Change is done Successfully')    
        ticket.save()
        
        
        return redirect('/mytickets')

def login(request):
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['pass']
        #print(username,password)
        user = auth.authenticate(username=username,password=password)
        #for user session 
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or password not matching')
            return redirect('/login')
    else:
        return render(request,"user_loginpage.html")
    

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def index(request):

    if request.method=='GET':
        print('Test user'+request.user.username)

        employee=Employee.objects.get(user=request.user)
        return render(request,"index.html",{'employee':employee})

    