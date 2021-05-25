from django import forms
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
    pic = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['description', 'pic', 'tags']

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']
