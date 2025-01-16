from django.db import models
import uuid
from django.db import models
from django.utils import timezone
 
# Create your models here.

# Create your models here.
class contactus(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=500 ,blank=True, null=True,)
    phone = models.CharField( max_length=500 ,blank=True, null=True,)
    email = models.CharField( max_length=500 ,blank=True, null=True,)
    body = models.CharField( max_length=500 ,blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.name}'
class donatetor(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=500 ,blank=True, null=True,)
    phone = models.CharField( max_length=500 ,blank=True, null=True,)
    email = models.CharField( max_length=500 ,blank=True, null=True,)
    body = models.CharField( max_length=500 ,blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.name}'
# Create your models here.
class stayupdated(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField( max_length=500 ,blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.email}'
 
    
class homepage(models.Model):
    h1 = models.CharField( max_length=500 ,blank=True, null=True,)
    h2 = models.CharField( max_length=500 ,blank=True, null=True,)
    h3 = models.CharField( max_length=500 ,blank=True, null=True,)
    h4 = models.CharField( max_length=500 ,blank=True, null=True,)
    h5 = models.CharField( max_length=500 ,blank=True, null=True,)
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slide1 = models.TextField( max_length=500 ,blank=True, null=True,)
    slide2 = models.TextField( max_length=500 ,blank=True, null=True,)
    slide3 = models.TextField( max_length=500 ,blank=True, null=True,)
    slide5 = models.TextField( max_length=500 ,blank=True, null=True,)
    slide4 = models.TextField( max_length=500 ,blank=True, null=True,)
    h1image = models.TextField( max_length=500 ,blank=True, null=True,)
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    idx = models.IntegerField( default=1) 
    
    def __str__(self):
        return f'the userid {self.h1}-{self.uuids}'
    
class aboutuse(models.Model):
    h1 = models.CharField( max_length=500 ,blank=True, null=True,)
    slideh1 = models.TextField(  blank=True, null=True,)
    h2 = models.CharField( max_length=500 ,blank=True, null=True,)
    slideh2 = models.TextField(  blank=True, null=True,)
    h3 = models.CharField(  max_length=500 , blank=True, null=True,)
    slideh3 = models.TextField(  blank=True, null=True,)
    h4 = models.CharField( max_length=500 ,blank=True, null=True,)
    slideh4 = models.TextField(  blank=True, null=True,)
    h5 = models.CharField( max_length=500 ,blank=True, null=True,)
    slideH5 = models.TextField(  blank=True, null=True,)
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ourmission = models.TextField(  blank=True, null=True,)
    ourvision = models.TextField(  blank=True, null=True,)
    body = models.TextField( blank=True, null=True,)
    Association  = models.TextField(blank=True, null=True,)
    Associationimage  = models.TextField( blank=True, null=True,)
    building  = models.TextField(  blank=True, null=True,)
    buildingimage  = models.TextField(  blank=True, null=True,)
    body2  = models.TextField(  blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    
    def __str__(self):
        return f'the userid {self.uuids} '


STATUS_CHOICES = [
    ('Position open', 'Position open'),
    ('Position Closed', 'Position Closed'),
     
] 


TYPE_STATUS_CHOICES = [
    ('part time', 'Parttime'),
    ('full-time', 'Fulltime'),
     
]
    
class reportx(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=500 ,blank=True, null=True,)
    body = models.TextField(  blank=True, null=True,)
    image = models.TextField(  blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.title}'
class teams(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=500 ,blank=True, null=True,)
    position = models.TextField(  blank=True, null=True,)
    image = models.TextField( max_length=500 ,blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.name} '
class bankdetail(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField( max_length=500 ,blank=True, null=True,)
    name = models.CharField( max_length=500 ,blank=True, null=True,)
    bankdetailnumber = models.TextField(  blank=True, null=True,)
    additional = models.CharField( max_length=500 ,blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.name} '
class job(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=500 ,blank=True, null=True,)
    state = models.CharField(  max_length=500 , blank=True, null=True,)
    Status = models.CharField(choices=STATUS_CHOICES,  max_length=500 , blank=True, null=True,)
    TYPE = models.CharField( choices=TYPE_STATUS_CHOICES, max_length=500 , blank=True, null=True,)
    
    body = models.TextField( blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, auto_created=False)
    closedate = models.DateTimeField( default=timezone.now, auto_created=False)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.title}'
class projectx(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=500 ,blank=True, null=True,)
    state = models.CharField(  max_length=500 , blank=True, null=True,)
    Status = models.CharField(   max_length=500 , blank=True, null=True,)
    header = models.CharField(  max_length=500 , blank=True, null=True,)
    author = models.CharField(  max_length=500 , blank=True, null=True,)
    email = models.TextField(    blank=True, null=True,)
    image1 = models.TextField(    blank=True, null=True,)
    image2 = models.TextField(    blank=True, null=True,)
    body = models.TextField( blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.title}'
class Press(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.CharField( max_length=500 ,blank=True, null=True,)
    title = models.CharField( max_length=500 ,blank=True, null=True,)
    
    body = models.TextField( blank=True, null=True,)
    image = models.TextField( blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, blank=True, null=True,)
    cdatex = models.DateTimeField( default=timezone.now,  blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.title}'
class publicationsx(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=500 ,blank=True, null=True,)
    email = models.CharField( max_length=500 ,blank=True, null=True,)
    header = models.TextField( blank=True, null=True,)
    body = models.TextField( blank=True, null=True,)
    Author = models.TextField( blank=True, null=True,)
    url = models.TextField( blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, blank=True, null=True,)
    
    def __str__(self):
        return f'the userid {self.uuids}-{self.title}'
    
    
    
    
class news(models.Model):
    uuids = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=500 ,blank=True, null=True,)
    label = models.CharField(  max_length=500 , blank=True, null=True,)
    type = models.CharField(  max_length=500 , blank=True, null=True,)
    
    header = models.CharField( max_length=500 ,blank=True, null=True,)
    body = models.TextField(  blank=True, null=True,)
    date = models.DateTimeField( default=timezone.now, blank=True, null=True,)
    imagex = models.TextField( max_length=500 ,blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    
    imagex1 = models.TextField( max_length=500 ,blank=True, null=True,)
    imagex2 = models.TextField( max_length=500 ,blank=True, null=True,)
    def __str__(self):
        return f'the userid {self.uuids}-{self.title}'


class siteedit(models.Model):
    name = models.CharField( max_length=500 ,blank=True, null=True,)
    email = models.CharField( max_length=500 ,blank=True, null=True,)
    domain = models.CharField( max_length=500 ,default=name, blank=True, null=True,)
    headOffice = models.CharField( max_length=500 ,blank=True, null=True,) 
    dis = models.TextField( blank=True, null=True,)
    phone = models.CharField( max_length=500 ,blank=True, null=True,)
    facebooklink = models.CharField( max_length=500 ,blank=True, null=True,)
    twiiterlink = models.CharField( max_length=500 ,blank=True, null=True,)
    instergram = models.CharField( max_length=500 ,blank=True, null=True,)
    youtubelink = models.CharField( max_length=500 ,blank=True, null=True,)
    logo = models.TextField( blank=True, null=True,)
    image1 = models.TextField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    

   
    def __str__(self):
        return self.name