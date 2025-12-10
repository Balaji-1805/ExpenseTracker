from django import forms
from .models import Category,Expense
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# CategoryForm
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"

# ExpenseForm
class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields="__all__"