from django import forms

class contactform(forms.Form):
	Firstname = forms.CharField(required=True)
	Lastname = forms.CharField(required=True)
	subject = forms.CharField(required=True)
	Email = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea,required=True)
	

