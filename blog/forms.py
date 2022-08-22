# import the following
from django import forms
from blog.models import Post,Comment

# creating form dot models
class PostForm(forms.ModelForm):

#    creating a meta class
    class Meta():
        #connecting a model with form
        model = Post
        # the following are the fields that i want a user to be able to fill
        fields = ('author','title','text')
# widgets are used to style the input/title/button of the form.... in this case we ain't using html form but using databate attributes to generate html forms for us
        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})}

class CommentForm(forms.ModelForm):

  class Meta():
    model = Comment
    fields = ('author','text')

    widgets = {
    'author': forms.TextInput(attrs={'class':'textinputclass'}),
    'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})}
