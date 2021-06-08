from django.conf.urls import url
from authentication import views

urlpatterns = [
    url('users/$', views.UserListView.as_view()),
]