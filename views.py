from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Book, BookIssue, Lib_Member
from .forms import BookForm, IssueForm, MemberForm

def Home(request):
	return render(request,'home.html')

def myFiles(request):
	import os
	html='''<h2>In this library,</h2>\n <ol>'''
	folder = os.path.abspath (os.path.dirname(__file__) + '/../media/images/books')
	dirlist = os.listdir (folder)
	for fname in dirlist:
		html += "\n <li>" + fname + "</li>"
	html += "</ol>"
	return HttpResponse(html)

def BooksFormData(request):
	book_id='0'
	if request.method=="GET":
		form = BookForm()
	elif request.method == "POST": #then save the data into table
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/library/home.html")
		else: # create a new form
			book_id = request.POST['hd_id']
			if book_id != '0':
				_data = Book.objects.get(id=book_id)
				form = BookForm(_data)
			else:
				form = BookForm()
	return render(request, "Booksform.html", {"bookformdata":form, })

def booksList(request):
	books=Book.objects.order_by("booktitle")
	return render(request, "book_table.html",{'booksdata': books,})

def bookIssue(request):
	if request.method == "POST": #then save the data into table
		form_b = IssueForm(request.POST, request.FILES)
		if form_b.is_valid():
			form_b.save()
	form_b = IssueForm()
	return render(request, "borrow.html", {"issueformdata":form_b, })

def get_issues(request):
	got_issue=BookIssue.objects.order_by('book')
	return render(request, "issue_table.html",{'issueformdata': got_issue,})

def Library_Member(request):
	if request.method == "POST": #then save the data into table
		form = MemberForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/library/home.html")
	form_c = MemberForm()
	return render(request, "member.html", {"memberformdata":form_c, })

def MemberList(request):
	member=Lib_Member.objects.order_by('id')
	return render(request, "member_table.html",{'memberformdata': member,})
