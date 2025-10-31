from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    email = forms.EmailField(label="E-mail")
    birthdate = forms.DateField(
        label="Data de Nascimento",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": "Número de DDD inválido."},
    )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{9,15}$",
        error_messages={"invalid": "Número de Telefone inválido."},
    )
    coutry = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email",
            "birthdate",
            "area_code",
            "phone_number",
            "coutry",
            "state",
            "city",
        ]

        widgets = {
            "birthdate": forms.DateInput(attrs={"type": "date"}),
        }
