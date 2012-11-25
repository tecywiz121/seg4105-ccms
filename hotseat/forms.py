from django import forms

class TerminalForm(forms.Form):
    terminalId = forms.CharField(max_length=255)
    timestamp = forms.IntegerField()

class LoginForm(TerminalForm):
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)

class KeepaliveForm(TerminalForm):
    token = forms.CharField(max_length=10)
