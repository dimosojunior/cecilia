from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.
class Report(models.Model):
	title = RichTextUploadingField(blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	body = RichTextUploadingField(blank=True, null=True)
	post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	image = models.ImageField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)

	sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
	sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
	sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
	sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
	sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
	

	sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
	sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
	sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
	sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
	sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
	total_marks = models.IntegerField(default= 1000, blank=True, null=True)

	sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
	sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
	sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
	sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
	sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
	total_obtained = models.IntegerField(default= 800, blank=True, null=True)

	sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
	sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
	sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
	sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
	sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
	
	sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
	sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
	sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
	sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
	sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

	percentage = models.FloatField(blank=True, null=True)
	Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
	rank = models.CharField(max_length=200, blank=True, null=True)
	result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
	stu_pos = models.IntegerField(blank=True, null=True)
	all_stu = models.IntegerField(blank=True, null=True)
	teacher_sign = models.CharField(max_length=200, blank=True, null=True)
	year = models.CharField(max_length=200, blank=True, null=True)










	





