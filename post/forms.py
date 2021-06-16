from django import forms
from post.models import Post

from django.forms import ClearableFileInput

class NewPostForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-large'}), required=False)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

	class Meta:
		model = Post
		fields = ('content','text', 'caption', 'tags')