from django import forms
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password :
			user = authenticate(username=username,password=password)
			if not user :
				raise forms.ValidationError('this user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('wrong password')
			if not user.is_active :
				raise forms.ValidationError('this user is not active ')

		return super(UserLoginForm,self).clean(*args,**kwargs)



class UserRregisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email Adress')
	email2 = forms.EmailField(label='conifrm email')
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta :
		model = User 
		fields = [
		'username',
		'email',
		'email2',
		'password',

		]
	def clean(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')

		if email != email2 :
			raise forms.ValidationError('email not compatible')

		email_qs = User.objects.filter(email=email)
		
		if email_qs.exists():
			raise forms.ValidationError('email already exists')

		
		return	super(UserRregisterForm,self).clean(*args,**kwargs)