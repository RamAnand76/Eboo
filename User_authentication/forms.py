# forms.py
from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('reader', 'Reader'),
        ('author', 'Author'),
        ('both', 'Both (Reader & Author)')
    ]
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = Profile
        fields = ['profileimg', 'location']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        profile = kwargs.get('instance')
        if profile:
            if profile.is_reader and profile.is_author:
                self.fields['user_type'].initial = 'both'
            elif profile.is_reader:
                self.fields['user_type'].initial = 'reader'
            elif profile.is_author:
                self.fields['user_type'].initial = 'author'

    def save(self, commit=True):
        profile = super(ProfileUpdateForm, self).save(commit=False)
        user_type = self.cleaned_data['user_type']
        if user_type == 'reader':
            profile.is_reader = True
            profile.is_author = False
        elif user_type == 'author':
            profile.is_reader = False
            profile.is_author = True
        else:  # both
            profile.is_reader = True
            profile.is_author = True
        if commit:
            profile.save()
        return profile
