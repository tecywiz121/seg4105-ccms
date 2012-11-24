from django import forms

class TerminalForm(forms.Form):
    terminalId = forms.CharField(max_length=255)

class LoginForm(TerminalForm):
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)

class LogoutForm(TerminalForm):
    pass

class KeepaliveForm(TerminalForm):
    pass
