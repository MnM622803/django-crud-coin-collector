from django import forms
from .models import GlobalRank


class GlobalRankForm(forms.ModelForm):
    class Meta:
        model = GlobalRank
        fields = ['date', 'rank', 'source']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

