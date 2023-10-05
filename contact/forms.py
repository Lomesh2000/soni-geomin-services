from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.EmailField(required=False, initial='lomeshsoni1234@gmail.com')

