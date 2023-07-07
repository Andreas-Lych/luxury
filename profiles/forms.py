from django import forms


class ProfilesForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    passport = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=12)
    age = forms.IntegerField(min_value=18, required=False)
    driving_experience = forms.IntegerField(min_value=3, required=False)
