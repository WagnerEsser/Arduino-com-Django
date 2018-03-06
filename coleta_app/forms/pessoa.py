# coding: utf-8
from django import forms
from coleta_app.models.pessoa import PessoaModel


class PessoaCadForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    turma = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = PessoaModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')


class PessoaEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    turma = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = PessoaModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password')


class PessoaPasswordForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    password_checker = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = PessoaModel
        fields = ['password']

    def clean_password_checker(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_checker'):
            raise forms.ValidationError("Senhas diferentes")
        else:
            return self.cleaned_data.get('password_checker')

    def save(self, commit=True):
        user = super(PessoaPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
