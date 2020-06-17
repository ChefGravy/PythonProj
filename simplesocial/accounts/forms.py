from django.contrib.auth import get_user_model
#this UserCreationForm is built in. look for documentation
from django.contrib.auth.forms import UserCreationForm

#you can name name it anything just not the same or self reference error
class UserCreateForm(UserCreationForm):

    class Meta:
        #fields are available from contrib.auth
        #when we create our database, the fields is what they will have access to
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
    #labels on the form/template
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #this is a label
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
