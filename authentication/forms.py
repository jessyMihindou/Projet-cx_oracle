from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.helper = FormHelper()
         self.helper.form_method = 'post'
         self.helper.add_input(Submit('submit', 'Submit'))
         print("thank")