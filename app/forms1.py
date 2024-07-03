from django import forms

from app.models import Customer

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not Customer.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not exist')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.data.get('password')
        try:
            user = Customer.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except Customer.DoesNotExist:
            raise forms.ValidationError(f'{email} does not exists')
        return password



class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.data.get('email').lower()
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(f'{email} is already registered')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password didn\'t match')
        return password