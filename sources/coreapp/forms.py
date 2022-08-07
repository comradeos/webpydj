from django import forms
from coreapp.views import Categories, Languages
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].label = 'Logo'
        self.fields['cat'].label = 'Category'
        self.fields['cat'].empty_label = 'Please select'
    class Meta:
        model = Languages
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10,}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if  len(title)>200:
            raise ValidationError('Error: title has length over 200 chars.')
        return title
    

from django.contrib.auth.models import User
class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    