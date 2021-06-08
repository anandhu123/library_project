from django.conf.urls import url
from library_dept import views

urlpatterns = [
    url('books/$', views.BooksView.as_view()),
    url('books/(?P<pk>[0-9]+)/$', views.BooksDetailView.as_view()),
    url('borrow/$', views.BorrowView.as_view()),
    url('userbookslist/(?P<pk>[0-9]+)/$', views.UserBorrowBooksView.as_view()),

]
