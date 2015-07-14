from django.forms import forms, CharField, BooleanField


class LoginForm(forms.Form):
    username = CharField(
        label="Email or login",
        max_length="80",
        required=True
    )

    password = CharField(
        label="Password",
        max_length="80",
        required=True
    )

    remember = BooleanField(required=False)