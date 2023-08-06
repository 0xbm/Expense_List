from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Expense


class ExpenseList(ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'expense/expense_list.html'


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('expenses')
