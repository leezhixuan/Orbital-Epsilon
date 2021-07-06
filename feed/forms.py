from django import forms
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'picture', 'body', 'tags']

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']
