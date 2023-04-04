from django import forms
from .models import Topic, BoardPost
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
#from django.forms import Textarea


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class NewBoardPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewBoardPostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'message',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

    class Meta:
        model = BoardPost
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
