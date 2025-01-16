from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'parent_message']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

    # You may want to disable or set a default for 'parent_message' when creating a new message
    def __init__(self, *args, **kwargs):
        parent_message = kwargs.get('initial', {}).get('parent_message', None)
        super().__init__(*args, **kwargs)
        if parent_message:
            self.fields['parent_message'].initial = parent_message
            self.fields['parent_message'].widget = forms.HiddenInput()
