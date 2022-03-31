from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
	email = EmailField(required=True, label='Email')

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	