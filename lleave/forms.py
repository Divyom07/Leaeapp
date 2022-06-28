
from django import forms
from .models import *


class LeaveAppForm(forms.ModelForm):
    fdate = forms.DateField(label = 'From Date', widget=forms.DateInput(attrs = {'class': 'form-fdate form-control', 'name': 'fdate', 'id': 'fdate', 'type': 'date'}))
    
    tdate = forms.DateField(label = 'To Date', widget=forms.DateInput(attrs = {'class': 'form-tdate form-control', 'name': 'tdate', 'id': 'tdate', 'type': 'date'}))

    type_of_leave = forms.ModelChoiceField(queryset=type_of_leave.objects.all().distinct(),label ='Type of Leave', widget = forms.Select(attrs = {'class' : 'form-type form-control', 'name': 'ltype', 'id': 'ltype'}))

    reason = forms.CharField(label='Reason', widget=forms.TextInput(attrs={'class': 'form-reason form-control', 'placeholder': 'Type your reason', 'name': 'lreason', 'id': 'lreason'}))
    
    
    class Meta:
        model= LeaveApplication
        fields= ('fdate', 'tdate', 'type_of_leave', 'reason')
        
    
class CreateUserForm(forms.ModelForm):
    
    name = forms.CharField(label ='Name', widget=forms.TextInput(attrs = {'class':'form-name form-user', 'name':'name', 'id': 'name'}))

    designation = forms.CharField(label ='Designation', widget=forms.TextInput(attrs = {'class':'form-desi form-user', 'name':'desig', 'id': 'desig'}))
    
    gender = forms.ModelChoiceField(queryset=gender.objects.all().distinct(),label='Gender', widget=forms.Select(attrs ={'class':'form-opt','name':'gender','id':'gender'}))
    
    
    phoneno = forms.CharField(label ='Contact No', widget=forms.TextInput(attrs = {'class':'form-phone form-user', 'name':'phoneno', 'id': 'phoneno'}))
    
    
    
    Location=forms.CharField(label='Location', widget=forms.TextInput(attrs={'class': 'form-location form-user', 'placeholder': 'Type your location', 'name': 'llocation', 'id': 'llocation'}))

    Marital_status=forms.ModelChoiceField(queryset=Martial_status.objects.all().distinct(),label ='Marital status', widget = forms.Select(attrs = {'class' : 'form-opt form-type', 'name': 'marital-status', 'id': 'marital-status'}))    
    
    
    
    class Meta:
        model = User
        fields = ('name', 'designation', 'gender','email',  'Location', 'Marital_status')
        
    
