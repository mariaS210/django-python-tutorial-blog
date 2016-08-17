from django import forms
from .models import Post, Comment, PostImage, PostText

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

class UploadForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('location', 'text')

class TextBlockForm(forms.ModelForm):
    class Meta:
        model = PostText
        fields = ('text', 'index')
