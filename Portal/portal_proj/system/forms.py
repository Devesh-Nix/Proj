from django import forms
from .models import Admin

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['admin_name', 'email', 'password', 'phone', 'admin_id']
        widgets = {
            'password': forms.PasswordInput()
        }
