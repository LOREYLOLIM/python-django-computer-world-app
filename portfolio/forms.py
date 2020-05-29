from django import forms
from .models import Testimonial, Ask

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["Name", "Testimonial", "Date"]

class AskForm(forms.ModelForm):
    class Meta:
        model = Ask
        fields = ["Subject", "Statement"]   

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))