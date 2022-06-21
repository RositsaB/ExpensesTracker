from django.urls import path

from expenses_tracker.web.views import show_index, create_expenses, edit_expenses, delete_expenses, profile_page, \
    edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', show_index, name='show index'),

    path('create', create_expenses, name='create expenses'),
    path('edit/<int:pk>/', edit_expenses, name='edit expenses'),
    path('delete/<int:pk>/', delete_expenses, name='delete expenses'),

    path('profile/', profile_page, name='profile'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
