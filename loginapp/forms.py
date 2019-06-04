from  django import forms
class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'from-control',
                'placeholder':'Your Name'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Last Name'
            }
        )
    )
    user_name = forms.CharField(
        label="Enter User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'User Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Password",
        widget=forms.TextInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Password'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Your Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Your Email'
            }
        )
    )
class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="Enter User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'User Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Password",
        widget=forms.TextInput(
            attrs={
                'class': 'from-control',
                'placeholder': 'Password'
            }
        )
    )


