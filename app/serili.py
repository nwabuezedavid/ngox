
from . models import *
from django.contrib.auth.models import User
from django import forms

class userFrom(forms.ModelForm):
    class Meta:
        model = User
        fields =["username","email","first_name","is_superuser"] 
        
        
class Contactusform(forms.ModelForm):
    class Meta:
        model = contactus
        fields ="__all__"
        
        
class donatetorform(forms.ModelForm):
    class Meta:
        model = donatetor
        fields ="__all__"
        
class stayupdatedform(forms.ModelForm):
    class Meta:
        model = stayupdated
        fields ="__all__"
        
class homepageform(forms.ModelForm):
    class Meta:
        model = homepage
        fields ="__all__"
        
        
class aboutuseform(forms.ModelForm):
    class Meta:
        model = aboutuse
        fields ="__all__"
        
class reportxform(forms.ModelForm):
    class Meta:
        model = reportx
        fields ="__all__"
        
class teamsform(forms.ModelForm):
    class Meta:
        model = teams
        fields ="__all__"
class bankdetailform(forms.ModelForm):
    class Meta:
        model = bankdetail
        fields ="__all__"
class jobform(forms.ModelForm):
    class Meta:
        model = job
        fields ="__all__"
class projectxform(forms.ModelForm):
    class Meta:
        model = projectx
        fields ="__all__"
class Pressform(forms.ModelForm):
    class Meta:
        model = Press
        fields ="__all__"
class publicationsxform(forms.ModelForm):
    class Meta:
        model = publicationsx
        fields ="__all__"
