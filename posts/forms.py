from django import forms
from models import Post

class BlogPostForm(fomrs.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')