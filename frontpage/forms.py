from .models import MembershipForm
from django import forms

class MembershipForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(label = 'E-Mail')
    category = forms.ChoiceField(choices=[('question','Question',),('member','Membership'),('other', 'Other')])
    subject = forms.CharField(required = True)
    body = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = MembershipForm
        fields = ('name','body','email','category','subject')
