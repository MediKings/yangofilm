from django import forms
from post.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'synopsis', 'realisateur', 'type', 'genre', 'picture', 'large_picture', 'video', 'slide']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Autheur'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Synopsis'}),
            'realisateur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Realisateur'}),
            'type': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'picture': forms.FileInput(),
            'large_picture': forms.FileInput(),
            'video': forms.FileInput(),
            'slide': forms.CheckboxInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control','rows': '5', 'placeholder': 'Commentaire'}),
        }
