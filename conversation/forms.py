from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder' : 'Write message',
            'style': 'width:100%; height:40px; border-radius:10px 0 0 10px;font-size:16px;padding:5px 20px;'
        })
    )

    class Meta:
        model = ConversationMessage
        fields = ('content',)
