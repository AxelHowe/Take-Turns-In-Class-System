from django import forms
from user.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    #fullName = forms.CharField(label='姓名', max_length=128)
    #website = forms.URLField(label='個人網址', max_length=128)
    #address = forms.CharField(label='住址', max_length=128)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self):
        user = super().save(commit=False)
        user.set_password(user.password)
        user.save()
        return user