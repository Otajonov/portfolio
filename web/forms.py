from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'telegram', 'phone', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'data-form-input':'', 'placeholder':'Ismingiz'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'data-form-input':'', 'placeholder':'Familiyangiz'}),
            'telegram': forms.TextInput(attrs={'class': 'form-input', 'data-form-input':'', 'placeholder':'Telegramingiz'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'data-form-input':'', 'placeholder':'Tel. raqamingiz'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'data-form-input':'', 'placeholder':'Sarlavha'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'data-form-input':'', 'placeholder':'Kaminaga xabaringiz mazmuni ...'}),
        }

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     # Add your validation for phone number
    #     return phone

    # def clean_telegram(self):
    #     telegram = self.cleaned_data.get('telegram')
    #     # Add your validation for telegram username
    #     return telegram
