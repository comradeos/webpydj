from django import forms
from coreapp.views import Categories


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Content')
    is_published = forms.BooleanField(label='Published', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Category', empty_label='Please select')
