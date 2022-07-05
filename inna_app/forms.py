from django import forms
from .models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', "name",  "children", "with_children", "other_contacts", "other_qwestion"]



