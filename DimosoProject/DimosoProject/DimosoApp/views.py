from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator

import os
from django.conf import settings
from django.http import HttpResponse

import calendar
from calendar import HTMLCalendar
from DimosoApp.models import *
from DimosoApp.forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout





# Create your views here.
def user_login(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        messages.success(request,"username or password is incorrect")
        return redirect('user_login')
        
   
        
    
        
    return render(request,'DimosoApp/user_login.html')

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        

#HIZI AUTHENTICATIONS SIO ZA LAZIMA
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                
                messages.success(request,"username Already exit")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                   
                    messages.success(request,"email Already exit")
                    return redirect('user_register')

                else:
                    #ONGEWEZA KUJA MOJA KWA MOJA HAPA
                     user = User.objects.create_user(username=username,email=email,password=password)
                     user.save()
                     

                     our_user = authenticate(username=username,password=password)
                     if our_user is not None:
                         login(request,user)
                         
                         return redirect('home')
                         #MPKA HAPA THEN UKAMALIZA
        else:
            messages.success(request,"Passwords did not match")
            return redirect('user_register')
  
          

           
    return render(request,'DimosoApp/user_register.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')
    return render(request,'DimosoApp/logout.html')

def base(response):
    return render(response, 'DimosoApp/base.html')
def home(request):
	form = ReportForm(request.POST or None)

	report = Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = Report.objects.filter( name__icontains=form['name'].value())

	context = {
	    "report":report,
	    "form":form

	}


	
	return render(request, 'DimosoApp/home.html', context)
class view_report(DetailView):
    model = Report
    template_name = 'DimosoApp/view_report.html'
    
    

class update_report(SuccessMessageMixin, UpdateView):
    model = Report
    template_name = 'DimosoApp/send_email.html'
    form_class = ReportForm
    success_url = reverse_lazy('home')
    success_message = "Report Updated Successfully"  

def delete_report(request, pk):
    report = get_object_or_404(Report, id=pk)
    report.delete()
    messages.success(request, "Report Updated Successfully")
    return redirect('home')



def search_autoco_report(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)   
def add_student_report(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            
            send_mail(
            	subject = request.POST['name'],
	            message = request.POST['body'],
	            from_email = settings.EMAIL_HOST_USER,
	            recipient_list = [request.POST['email']],
	            fail_silently=True,

            	)
            return redirect('home')
            


        messages.info(request, "Data Uploading failed!!!")
        return redirect('home')

    context={
        "form":form
    }
    return render(request, 'DimosoApp/add_student_report.html', context)
def sending_email(request):
	form = ReportForm()
	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			form.save()
			to = request.POST['email']
			name = request.POST['name']
			title = request.POST['title']
			#post_date = request.POST['post_date']
			sub1 = request.POST['sub1']
			sub2 = request.POST['sub2']
			sub3 = request.POST['sub3']
			sub4 = request.POST['sub4']
			sub5 = request.POST['sub5']
			sub1_marks = request.POST['sub1_marks']
			sub2_marks = request.POST['sub2_marks']
			sub3_marks = request.POST['sub3_marks']
			sub4_marks = request.POST['sub4_marks']
			sub5_marks = request.POST['sub5_marks']
			total_marks = request.POST['total_marks']
			sub1_obtained = request.POST['sub1_obtained']
			sub2_obtained = request.POST['sub2_obtained']
			sub3_obtained = request.POST['sub3_obtained']
			sub4_obtained = request.POST['sub4_obtained']
			sub5_obtained = request.POST['sub5_obtained']
			total_obtained = request.POST['total_obtained']

			sub1_grade = request.POST['sub1_grade']
			sub2_grade = request.POST['sub2_grade']
			sub3_grade = request.POST['sub3_grade']
			sub4_grade = request.POST['sub4_grade']
			sub5_grade = request.POST['sub5_grade']

			sub1_remaks = request.POST['sub1_remaks']
			sub2_remaks = request.POST['sub2_remaks']
			sub3_remaks = request.POST['sub3_remaks']
			sub4_remaks = request.POST['sub4_remaks']
			sub5_remaks = request.POST['sub5_remaks']

			percentage = request.POST['percentage']
			Overall_grade = request.POST['Overall_grade']
			rank = request.POST['rank']
			result = request.POST['result']
			stu_pos = request.POST['stu_pos']
			all_stu = request.POST['all_stu']
			teacher_sign = request.POST['teacher_sign']
			year = request.POST['year']
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Cecilia School ', 
				'name':name,
				'title':title,
				
				'sub1':sub1,
				'sub2':sub2,
				'sub3':sub3,
				'sub4':sub4,
				'sub5':sub5,
				'sub1_marks':sub1_marks,
				'sub2_marks':sub2_marks,
				'sub3_marks':sub3_marks,
				'sub4_marks':sub4_marks,
				'sub5_marks':sub5_marks,
				'total_marks':total_marks,
				'sub1_obtained':sub1_obtained,
				'sub2_obtained':sub2_obtained,
				'sub3_obtained':sub3_obtained,
				'sub4_obtained':sub4_obtained,
				'sub5_obtained':sub5_obtained,
				'total_obtained':total_obtained,
				'sub1_grade':sub1_grade,
				'sub2_grade':sub2_grade,
				'sub3_grade':sub3_grade,
				'sub4_grade':sub4_grade,
				'sub5_grade':sub5_grade,
				'sub1_remaks':sub1_remaks,
				'sub2_remaks':sub2_remaks,
				'sub3_remaks':sub3_remaks,
				'sub4_remaks':sub4_remaks,
				'sub5_remaks':sub5_remaks,
				'percentage':percentage,
				'Overall_grade':Overall_grade,
				'rank':rank,
				'result':result,
				'stu_pos':stu_pos,
				'all_stu':all_stu,
				'teacher_sign':teacher_sign,
				'year':year
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'DimosoApp/send_email.html', {"form":form})