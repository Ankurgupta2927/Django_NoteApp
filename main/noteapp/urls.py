from django.urls import path
from .views import register, user_login, home, add_note, edit_note, delete_note
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:note_id>/', edit_note, name='edit_note'),
    path('delete/<int:note_id>/', delete_note, name='delete_note'),
]
