from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

from .models import user_dashboard


class OnboardingForm(forms.ModelForm):
    TEMPLATE_STYLE_NAME = [('OFF','Official'), ('NUD', 'Nude Tones'), ("FLOW", "Flowery")]
    
    template_style=forms.CharField(label='Select a template style', widget=forms.RadioSelect(choices=TEMPLATE_STYLE_NAME))
    website_type=forms.CharField(label='What type of website to do wish to build?', 
                                        widget=forms.RadioSelect(choices=user_dashboard.WEBSITE_TYPES))
    user = forms.CharField(required=False, widget=forms.HiddenInput)
    
    class Meta:
        model = user_dashboard
        exclude = ('user',)
        fields = (
            'template_style',
            'website_type',
        )
        
        
            

    