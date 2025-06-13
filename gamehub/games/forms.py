from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'review_text']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
