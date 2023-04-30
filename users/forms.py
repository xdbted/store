from django.contrib.auth.forms import AuthenticationForm

 
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        field = ['username', 'password',]
