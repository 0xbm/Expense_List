from django.urls import path
from .views import ExpenseList, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ExpenseList.as_view(), name="expenses"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
