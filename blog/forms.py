from django import forms
from .models import Post, Comment

#validator function define
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상입력하세요')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    text = forms.CharField(widget=forms.Textarea)

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        #입력받는 필드명을 기술
        fields = ['title','text']
        # fields='__all__' #all fileds include

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)