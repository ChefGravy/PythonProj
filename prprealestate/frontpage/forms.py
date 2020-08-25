from .models import ContactForm
from django import forms

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(label = 'E-Mail')
    category = forms.ChoiceField(choices=[('question','Question',),('member','Membership'),('other', 'Other')])
    subject = forms.CharField(required = True)
    body = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = ContactForm
        fields = ('name','body','email','category','subject')
