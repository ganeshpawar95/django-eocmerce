from django import forms
from .models import Shipping


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
