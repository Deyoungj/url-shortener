from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class': 'form-control'}))