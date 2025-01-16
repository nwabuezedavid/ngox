from django.shortcuts import render
from .models import * 
from .serili import * 
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .req import *
# Create your views here.
def home(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all() ,
     
     "home": homepage.objects.get(idx=1)   ,
     
    }
    return render(request, "home.html", conx)
def about(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "about": aboutuse.objects.get(idx=1)   ,
        
    }
    return render(request, "about.html", conx)
def service(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "about": aboutuse.objects.get(idx=1)   ,
    
        
    }
    return render(request, "service.html", conx)
def contact(request):
    if request.method == "POST":
        tel = request.POST['tel']
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        if not contactus.objects.filter(    name = name,    phone = tel,    email = email,     body = message,).exists():
            contactus.objects.create(    name = name,    phone = tel,    email = email,     body = message)
            messages.info(request, "MESSAGE SENT SUCCESSFULLY ")
            return redirect('contact')
            
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "contact.html", conx)
def donate(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "bank": bankdetail.objects.all()   ,
        
    }
    return render(request, "donate.html", conx)
def partner(request):
    if request.method == "POST":
        tel = request.POST['tel']
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        if not donatetor.objects.filter(    name = name,    phone = tel,    email = email,     body = message,).exists():
            donatetor.objects.create(    name = name,    phone = tel,    email = email,     body = message)
            messages.info(request, "MESSAGE SENT SUCCESSFULLY ")
            return redirect('partner')
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "bk": bankdetail.objects.all()   ,
        
    }
    return render(request, "partner.html", conx)
def pastjob(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "job": job.objects.all()   ,
        
    }
    return render(request, "pastjob.html", conx)
def press(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "Press": Press.objects.all()   ,
        
    }
    return render(request, "press.html", conx)
def siteclinic(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "about": aboutuse.objects.get(idx=1)   ,

    }
    return render(request, "siteclinic.html", conx)
def ourteam(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "teams": teams.objects.all()   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "ourteam.html", conx)
def newdetail(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "item": news.objects.get(uuids=pk),
        
    }
    return render(request, "newdetail.html", conx)
def Pressdetail(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": Press.objects.all()   ,
    "item": Press.objects.get(uuids=pk),
        
    }
    return render(request, "pressdetail.html", conx)
def pubdetail(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": publicationsx.objects.all()   ,
    "item": publicationsx.objects.get(uuids=pk),
        
    }
    return render(request, "pub.html", conx)
def prodetail(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": projectx.objects.all()   ,
    "item": projectx.objects.get(uuids=pk),
        
    }
    return render(request, "pro.html", conx)
def pubdetail(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": publicationsx.objects.all()   ,
    "item": publicationsx.objects.get(uuids=pk),
        
    }
    return render(request, "pub.html", conx)
 
def newstory(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all(),
    "news": news.objects.all(),
        
    }
    return render(request, "newstory.html", conx)
def project(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "pro": projectx.objects.all()   ,
        
    }
    return render(request, "projects.html", conx)
def projectupdate(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "pro": projectx.objects.all()   ,
        
    }
    return render(request, "projects.html", conx)
def jobdetail(request,pk):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "item": job.objects.get(uuids = pk)   ,
        
    }
    return render(request, "jobdetail.html", conx)
 
def publications(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "pub": publicationsx.objects.all()   ,
        
    }
    return render(request, "publications.html", conx)
def report(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "report": reportx.objects.all()   ,
        
    }
    return render(request, "report.html", conx)
def traning(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "traning.html", conx)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
def logoutuser(request):
    logout(request)
    
    return redirect('Loginuser')
 
 
 
#  admink________?

from django.http import HttpResponse

@superuser_required
def dashboard(request,pk):
    user = User.objects.get(username=request.user.username)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": User.objects.all().exclude(id=pk),
    "user": user,
        
    }
    return render(request, "user/home.html", conx)
# account = get_object_or_404(benfitx, uuid=pk)
# benefitForm(request.POST, instance=account)

@superuser_required
def usercreate(request,pk):
    form = userFrom()
    if request.method == 'POST':
        form = userFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'created successfully')
            return redirect('usercreate', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": User.objects.all(),
    "form": form,
        
    }
    return render(request, "user/screateuser.html", conx)
def userdelete(request,pk):
    dd = User.objects.get(id=pk)
    dd.delete()
    return HttpResponse(status=204)
def userupdate(request,pk):
    ue = "USER"
    account = User.objects.get(id=pk)
    
    form = userFrom(instance=account)
    if request.method == 'POST':
        form = userFrom(request.POST,instance=account)
        if form.is_valid():
                form.save()
                messages.info(request, 'update successfully')
                return redirect('userupdate', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": User.objects.all(),
    "form": form,
    "ue": ue,
        
    }
    return render(request, "user/updateuser.html", conx)
 
 
 
 
 
#  Jobl>>
 
 
 
@superuser_required
def jobclient(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": job.objects.all(),
        
    }
    return render(request, "user/job.html", conx)
# account = get_object_or_404(benfitx, uuid=pk)
# benefitForm(request.POST, instance=account)

@superuser_required
def jobcreate(request,pk):
    ii = "JOB"
    form = jobform()
    if request.method == 'POST':
        form = jobform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'created successfully')
            return redirect('jobcreate', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": User.objects.all(),
    "form": form,
    "ii": ii,
        
    }
    return render(request, "user/screateuser.html", conx)
def jobdeletex(request,pk):
    dd = job.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)
def jobupdate(request,pk):
    account = job.objects.get(uuids=pk)
    ue = "Job"
    
    form = jobform(instance=account)
    if request.method == 'POST':
        form = jobform(request.POST,instance=account)
        if form.is_valid():
                form.save()
                messages.info(request, 'update successfully')
                return redirect('jobupdate', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": User.objects.all(),
    "form": form,
    "ue": ue,
        
    }
    return render(request, "user/updateuser.html", conx)









@superuser_required
def reportdeletex(request,pk):
    dd = reportx.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)


def teamdeletex(request,pk):
    dd = teams.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)

def bankdeletex(request,pk):
    dd = bankdetail.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)

def projectdeletex(request,pk):
    dd = projectx.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)

def pressdeletex(request,pk):
    dd = Press.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)

def publicationsxdeletex(request,pk):
    dd = publicationsx.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)

def newsdeletex(request,pk):
    dd = news.objects.get(uuids=pk)
    dd.delete()
    return HttpResponse(status=204)

# report/






 
@superuser_required
def reportDetail(request,pk):
    i = 'Report'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/report.html", conx)

 
 
def reportcreate(request,pk):
    i = 'Report'
    if request.method == "POST":
        title =  request.POST['title']
        body =  request.POST['body']
        image =  request.POST['imageBytes']
        date =  request.POST['date']
        
        if title and body:
            ss = reportx.objects.create(
            title=title,
            body=body,
            image=image,
            date=date,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('reportcreate', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/createreport.html", conx)

from datetime import datetime
 
def updatereport(request,pk):
    i = 'Report'
    xx = reportx.objects.get(uuids=pk)
    if request.method == "POST":
        title =  request.POST['title']
        body =  request.POST['body']
        image =  request.POST['imageBytes']
        date =  request.POST['date']
        if title and body:
            ss = reportx.objects.filter(uuids=pk).update(
            title=title,
            body=body or xx.body,
            image=image or xx.image,
            date=date  or xx.date,
            )
            messages.info(request, 'create sucessfully')
            return redirect('updatereport', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/updatereport.html", conx)



# team>






 
@superuser_required
def detailteam(request,pk):
    i = 'team'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": teams.objects.all(),
    "i": i,
        
    }
    return render(request, "user/teams.html", conx)
 
 
def createteam(request,pk):
    i = 'Team'
    if request.method == "POST":
        name =  request.POST['title']
        position =  request.POST['body']
        image =  request.POST['imageBytes']
        date =  request.POST['date']
        
        if name and position:
            ss = teams.objects.create(
            name=name,
            position=position,
            image=image,
            date=date,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('createteam', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/createteam.html", conx)



def updateteam(request,pk):
    i = 'Report'
    xx = teams.objects.get(uuids=pk)
    if request.method == "POST":
        name =  request.POST['title']
        position =  request.POST['body']
        image =  request.POST['imageBytes']
        date =  request.POST['date']
        if name and position:
            ss = teams.objects.filter(uuids=pk).update(
            name=name,
            position=position or xx.position,
            image=image or xx.image,
            date=date  or xx.date,
            )
            messages.info(request, 'updated sucessfully')
            return redirect('updateteam', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/updateteam.html", conx)

 
 
 
#  team??






@superuser_required
def bankDetail(request,pk):
    i = 'Bank'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": bankdetail.objects.all(),
    "i": i,
        
    }
    return render(request, "user/bank.html", conx)

 
 
 
def createbank(request,pk):
    i = 'BAnk'
    if request.method == "POST":
        typex =  request.POST['type']
        name =  request.POST['name']
        bankdetailnumber =  request.POST['bankdetailnumber']
        additional =  request.POST['additional']
        
        if typex and name:
            ss = bankdetail.objects.create(
            type=typex,
            name=name,
            bankdetailnumber=bankdetailnumber,
            additional=additional,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('createbank', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/createbank.html", conx)





def updatebank(request,pk):
    i = 'Bank'
    xx = bankdetail.objects.get(uuids=pk)
    if request.method == "POST":
        type =  request.POST['type']
        name =  request.POST['name']
        bankdetailnumber =  request.POST['bankdetailnumber']
        additional =  request.POST['additional']
        if name and bankdetailnumber:
            ss = bankdetail.objects.filter(uuids=pk).update(
            type=type,
            name=name or xx.name,
            bankdetailnumber=bankdetailnumber or xx.bankdetailnumber,
            additional=additional  or xx.additional,
            )
            messages.info(request, 'updated sucessfully')
            return redirect('updatebank', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/updatebank.html", conx)








@superuser_required
def projectdetal(request,pk):
    i = 'Project'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": projectx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/project.html", conx)

 
 
 
 
def createproject(request,pk):
    i = 'Project'
    if request.method == "POST":
        title =  request.POST['title']
        state =  request.POST['state']
        Status =  request.POST['status']
        header =  request.POST['header']
        author =  request.POST['author']
        email =  request.POST['email']
        image1 =  request.POST['imageBytes1']
        image2 =  request.POST['imageBytes2']
        body =  request.POST['body']
        date =  request.POST['date']
        
        if title and state:
            ss = projectx.objects.create(
            title=title,
            state=state,
            Status=Status,
            header=header,
            author=author,
            email=email,
            image1=image1,
            image2=image2,
            body=body,
            date=date,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('createproject', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/projectcreate.html", conx)

def yupdateproject(request,pk):
    i = 'Project'
    xx = projectx.objects.get(uuids=pk)
    
    if request.method == "POST":
        title =  request.POST['title']
        state =  request.POST['state']
        Status =  request.POST['status']
        header =  request.POST['header']
        author =  request.POST['author']
        email =  request.POST['email']
        image1 =  request.POST['imageBytes1']
        image2 =  request.POST['imageBytes2']
        body =  request.POST['body']
        date =  request.POST['date']
        
        if title and state:
            ss = projectx.objects.filter(uuids=pk).update(
            title=title,
            state=state,
            Status=Status,
            header=header,
            author=author,
            email=email,
            image1=image1,
            image2=image2,
            body=body,
            date=date,
            )
            messages.info(request, 'Update sucessfully')
            return redirect('yupdateproject', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/updateproject.html", conx)





# press?


@superuser_required
def pressDetail(request,pk):
    i = 'Press'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": Press.objects.all(),
    "i": i,
        
    }
    return render(request, "user/press.html", conx)

 
def createpress(request,pk):
    i = 'Press'
    if request.method == "POST":
        header =  request.POST['header']
        title =  request.POST['title']
        body =  request.POST['body']
        image =  request.POST['imageBytes']
        date =  request.POST['date']
        cdatex =  request.POST['cdatex']
        if title and header:
            ss = Press.objects.create(
            header=header,
            title=title,
            body=body,
            image=image,
            date=date,
            cdatex=cdatex,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('createpress', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/createpress.html", conx)



def updatepress(request,pk):
    i = 'Press'
    xx = Press.objects.get(uuids=pk)
    
    if request.method == "POST":
        header =  request.POST['header']
        title =  request.POST['title']
        body =  request.POST['body']
        image =  request.POST['imageBytes']
        date =  request.POST['date']
        cdatex =  request.POST['cdatex']
        if title and header:
            ss = Press.objects.filter(uuids=pk).update(
            header=header,
            title=title,
            body=body,
            image=image or xx.image,
            date=date or xx.date,
            cdatex=cdatex or xx.cdatex,
            )
            messages.info(request, 'Update sucessfully')
            return redirect('updatepress', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/updatepress.html", conx)


# publicationsx


@superuser_required
def publicationsxDetail(request,pk):
    i = 'publications'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": publicationsx.objects.all(),
    "i": i,
        
    }
    return render(request, "user/publicationsx.html", conx)





def createpublications(request,pk):
    i = 'publications'
    if request.method == "POST":
        title =  request.POST['title']
        email =  request.POST['email']
        header =  request.POST['header']
        body =  request.POST['body']
        Author =  request.POST['author']
        url =  request.POST['url']
        date =  request.POST['date']
        if title and header:
            ss = publicationsx.objects.create(
            title=title,
            email=email,
            header=header,
            body=body,
            Author=Author,
            url=url,
            date=date,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('createpublications', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    
    "i": i,
        
    }
    return render(request, "user/createpublications.html", conx)




def updatepublications(request,pk):
    i = 'publications'
    xx = publicationsx.objects.get(uuids=pk)
    
    if request.method == "POST":
        title =  request.POST['title']
        email =  request.POST['email']
        header =  request.POST['header']
        body =  request.POST['body']
        Author =  request.POST['author']
        url =  request.POST['url']
        date =  request.POST['date']
        if title and header:
            ss = publicationsx.objects.filter(uuids=pk).update(
            title=title,
            email=email,
            header=header,
            body=body,
            Author=Author,
            url=url,
            date=date,
            )
            ss.save()
            messages.info(request, 'Update sucessfully')
            return redirect('updatepublications', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": reportx.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/updatepublications.html", conx)

# new>?  



@superuser_required
def newdetail(request,pk):
    i = 'News'
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": news.objects.all(),
    "i": i,
        
    }
    return render(request, "user/new.html", conx)





def createnews(request,pk):
    i = 'News'
    if request.method == "POST":
        title =  request.POST['title']
        label =  request.POST['label']
        header =  request.POST['header']
        body =  request.POST['body']
        date =  request.POST['date']
        imagex =  request.POST['imageBytesX']
        imagex1 =  request.POST['imageBytesX1']
        imagex2 =  request.POST['imageBytesX2']
        if title and header :
            ss = news.objects.create(
            title=title,
            label=label,
            header=header,
            body=body,
            date=date,
            imagex=imagex,
            imagex1=imagex1,
            imagex2=imagex2,
            )
            ss.save()
            messages.info(request, 'create sucessfully')
            return redirect('createnews', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    
    "i": i,
        
    }
    return render(request, "user/createnews.html", conx)


def updatenews(request,pk):
    i = 'News'
    xx = news.objects.get(uuids=pk)
    
    if request.method == "POST":
        title =  request.POST['title']
        label =  request.POST['label']
        header =  request.POST['header']
        body =  request.POST['body']
        date =  request.POST['date']
        imagex =  request.POST['imageBytesX']
        imagex1 =  request.POST['imageBytesX1']
        imagex2 =  request.POST['imageBytesX2']
        if title and header :
            ss = news.objects.filter(uuids=pk).update(
            title=title,
            label=label,
            header=header or xx.header,
            body=body or xx.body,
            date=date or xx.date ,
            imagex=imagex or xx.imagex,
            imagex1=imagex1 or xx.imagex1,
            imagex2=imagex2 or xx.imagex2,
            )
            messages.info(request, 'create sucessfully')
            return redirect('updatenews', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    'item':xx,
    "i": i,
        
    }
    return render(request, "user/updatenews.html", conx)

# aboutsite.html

 
 
 
@superuser_required
def aboutsite(request,pk):
    i = 'About us'
    xx = aboutuse.objects.get(idx=1)
    print(xx)
    if request.method == "POST":
        h1 =  request.POST['h1']
        slideh1 =  request.POST['Slideh1Bytes']
        h2 =  request.POST['h2']
        slideh2 =  request.POST['Slideh2Bytes']
        h3 =  request.POST['h3']
        slideh3 =  request.POST['Slideh3Bytes']
        h4 =  request.POST['h4']
        slideh4 =  request.POST['Slideh4Bytes']
        h5 =  request.POST['h5']
        slideH5x =  request.POST['SlideH5Bytes']
        ourmission =  request.POST['ourmission']
        ourvision =  request.POST['ourvision']
        body =  request.POST['body']
        Association =  request.POST['Association']
        Associationimage =  request.POST['AssociationImageBytes']
        building =  request.POST['building']
        buildingimage =  request.POST['BuildingImageBytes']
        body2 =  request.POST['body2'] 
        if h1 and h2 :
            ss   = aboutuse.objects.filter(idx=1).update(
          h1 =h1,
slideh1 =slideh1 or  xx.slideh1,
h2 =h2,

slideh2 =slideh2 or xx.slideh2,
h3 =h3,
slideh3 =slideh3 or xx.slideh3,
h4 =h4,
slideh4 =slideh4 or xx.slideh4,
h5 =h5,
slideH5 =slideH5x or xx.slideH5,
ourmission =ourmission,
ourvision =ourvision,
body =body,
Association =Association,
Associationimage =Associationimage or xx.Associationimage,
building =building,
buildingimage =buildingimage or xx.buildingimage, 
body2 =body2,
            )
            messages.info(request, 'create sucessfully')
            return redirect('aboutsite', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "alluserx": aboutuse.objects.all(),
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/aboutsite.html", conx)

@superuser_required
def site(request,pk):
    i = 'About us'
    xx = siteedit.objects.get(idx=1)
    print(xx)
    if request.method == "POST":
        name =  request.POST['name']
        email =  request.POST['email']
        domain =  request.POST['domain']
        headOffice =  request.POST['headOffice']
        dis =  request.POST['dis']
        phone =  request.POST['phone']
        facebooklink =  request.POST['facebooklink']
        twiiterlink =  request.POST['twiiterlink']
        instergram =  request.POST['instergram']
        youtubelink =  request.POST['youtubelink']
        logo =  request.POST['LogoBytes']
        image1 =  request.POST['Image1Bytes']
          
        if name and email :
            ss   = siteedit.objects.filter(idx=1).update(
          name =name,
email =email,
domain =domain,
headOffice =headOffice,
dis =dis,
phone =phone,
facebooklink =facebooklink,
twiiterlink =twiiterlink,
instergram =instergram,
youtubelink =youtubelink,
logo =logo or xx.logo,
image1 =image1 or xx.image1,
            )
            messages.info(request, 'create sucessfully')
            return redirect('site', pk=pk)
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "i": i,
    "item": xx,
        
    }
    return render(request, "user/site.html", conx)
























def Loginuser(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username, first_name=password).exists():
            user = User.objects.get(username=username, first_name=password)
            if user.is_superuser:
                authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("dashboard", pk=user.id)
            else:
                messages.info(request, 'Wait the admin will approve Your membership account')

                return redirect("Loginuser")
                
        else:
                messages.error(request, 'user does not exist')        
        
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "auth/Login.html",con)



from django.db.models import Q
 

def registeruser(request):
    print(f'{request.get_host()}/verify/')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(Q(username= username) | Q(email=email)  ).exists():
            messages.error(request, 'username and email already taken')
            return redirect('registeruser') 
        else:
            if password == password2:
                
                setuse = User.objects.create(username = username, email=email, first_name =password, password=password)
                                                 
                    
                setuse.save()
                
                con ={
                     'site':siteedit.objects.get(idx=1),
                     'user':setuse,
                    }
                messages.info(request, 'Wait!, The admin will approve Your membership account')
                return redirect('Loginuser') 
                
            else:
                messages.error(request, 'password doest match')
                   
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "auth/register.html",con)
