from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserForm(UserCreationForm):
    referral_parent = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        label="Indicado por",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'referral_parent',
            'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UserUpdateForm(UserChangeForm):
    password = None  # esconde campo de senha
    referral_parent = UserForm.base_fields['referral_parent']

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'referral_parent'
        ]
        widgets = UserForm.Meta.widgets