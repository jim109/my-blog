from django import forms
from .models import Post
from django.core.context_processors import csrf

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)