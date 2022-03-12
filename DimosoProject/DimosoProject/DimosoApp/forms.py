from DimosoApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class ReportForm(forms.ModelForm):

    
    name = forms.CharField(
            #label=True,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Post Name'})
      
       )
    title = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi', 'placeholder' : 'Enter Title'})
      
       )
   
    
    
    sub1_obtained = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub2_obtained = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub3_obtained = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub4_obtained = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub5_obtained = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    total_obtained = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub1_grade = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub2_grade = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub3_grade = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub4_grade = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub5_grade = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub1_remaks = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub2_remaks = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub3_remaks = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub4_remaks = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    sub5_remaks = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    Overall_grade = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    rank = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    
    teacher_sign = forms.CharField(
            #label=True,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    year = forms.CharField(
            #label=True,
            required=False,

            
            widget=forms.TextInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    stu_pos = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )
    all_stu = forms.IntegerField(
            #label=True,
            required=False,
            
            widget=forms.NumberInput(attrs={'id' :'title','class': 'inputi'})
      
       )

    class Meta:
        model = Report
        fields = [
			"name",
			"email",
			"title",
			"sub1",
			"sub2",
			"sub3",
			"sub4",
			"sub5",
			"sub1_marks",
			"sub2_marks",
			"sub3_marks",
			"sub4_marks",
			"sub5_marks",
			"total_marks",

			"sub1_obtained",
			"sub2_obtained",
			"sub3_obtained",
			"sub4_obtained",
			"sub5_obtained",
			"total_obtained",

			"sub1_grade",
			"sub2_grade",
			"sub3_grade",
			"sub4_grade",
			"sub5_grade",

			"sub1_remaks",
			"sub2_remaks",
			"sub3_remaks",
			"sub4_remaks",
			"sub5_remaks",

			"percentage",
			"Overall_grade",
			"rank",
			"result",
			"stu_pos",
			"all_stu",
			"teacher_sign",
			"year"

        ]