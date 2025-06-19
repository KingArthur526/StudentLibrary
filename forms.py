from .models import Book, BookIssue, Lib_Member
from django import forms
class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=('id', 'bookno','booktitle','isbn','edition','barcode','author','publisher','price','frontcover')

class DP(forms.DateInput):
	input_type='date'

class IssueForm(forms.ModelForm):
	class Meta:
		model=BookIssue
		fields=('id','book','borrower','issue_date','return_date')
		widgets={'issue_date':DP(),'return_date':DP()}

class MemberForm(forms.ModelForm):
	class Meta:
		model=Lib_Member
		fields=('id','name','std','member_code','dob','photo')
		widgets={'dob':DP()}

Models.py
from django.db import models

# Create your models here.
class Book(models.Model):
	bookno= models.IntegerField(verbose_name="Book Number")
	booktitle=models.CharField(max_length=255, verbose_name="Book Title", default='Enter Book name')
	isbn=models.CharField(max_length=20, verbose_name="ISBN")
	edition=models.CharField(max_length=20, verbose_name="Book Edition")
	barcode=models.IntegerField(verbose_name="Bar code")
	author=models.CharField(max_length=255, verbose_name="Author(s)" )
	publisher=models.CharField(max_length=255, verbose_name="Publisher" )
	price=models.IntegerField(verbose_name="Book Price")
	frontcover=models.ImageField(upload_to='images/books', verbose_name="Cover Photos",
	null=True)
	def __str__(self):
		return f'''{self.bookno}, {self.booktitle}, {self.author}'''


class Lib_Member(models.Model):
	name=models.CharField(max_length=255)
	std=models.IntegerField(verbose_name='Standard',null=True)
	member_code=models.IntegerField(verbose_name='Member Number', null=True)
	dob=models.DateField(verbose_name='Date of birth',default='2000-01-13', blank=False)
	photo=models.ImageField(upload_to='images/members',verbose_name='Member photo', null=True)
	def __str__(self):
		return f'{self.name},{self.member_code}'

class BookIssue(models.Model):
	book=models.ForeignKey(Book,
	verbose_name='book', on_delete=models.CASCADE, blank=True)
	borrower=models.ForeignKey(Lib_Member,verbose_name='Borrower',
	on_delete=models.CASCADE, blank=True)
	issue_date=models.DateField(verbose_name='date of borrowal',default="2020-01-13", blank=False)
	return_date=models.DateField(verbose_name='date of return',default="2020-01-13", blank=False)
	def __str__(self):
		return f'{self.bookno},{self.issue_date},{self.return_date}'
