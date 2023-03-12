# Model forms help to reduce redundancy

from django import forms
from stripe import Review 
from core.models import ProductReview

# Convert a model into a django form
class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write review"}))

    # Inner class of the model class, used to change the behaviour of model fields like verbose_name
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']