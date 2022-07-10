from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from links.models import Link


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('register', 'Sign up'))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('enter', 'Sign in'))


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['origin_link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('shorten', 'Shorten'))

