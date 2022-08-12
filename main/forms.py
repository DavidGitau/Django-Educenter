from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from back.forms import ButtonLayout

# class HomeForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1']
# class HomeForm(forms.Form):
#     method = 'post'
#     username = forms.CharField(max_length=20)
#     password1 = forms.CharField(max_length=20)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper

#         self.helper.layout = Layout(
#             'username',
#             'password1',
#             ButtonLayout()
#         )

