from django import forms
from coreapp.views import Categories, Languages


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Please select'
    class Meta:
        model = Languages
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10,}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10,}),
        }
