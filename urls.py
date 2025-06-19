from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
	path('home.html', views.Home, name='Home url' ),
	path('booksform', views.BooksFormData, name='bookform url'),
	path('bookslist', views.booksList, name="Books List URL"),
	path('files.html', views.myFiles, name='image_files'),
	path('bookissue', views.bookIssue, name='Book Issue list'),
	path('member', views.Library_Member, name='becoming member'),
	path('issuelist', views.get_issues, name='member list'),
	path('memberlist', views.MemberList, name='member list'),
]
