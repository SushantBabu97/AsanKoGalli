from django.forms import ModelForm
from .models import ProductHasReview

class ReviewForm(ModelForm):
    class Meta:
         model=ProductHasReview
         fields=['rating','comment']