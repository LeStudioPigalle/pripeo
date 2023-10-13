from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text="Required. Add a valid email adress")

    class Meta:
        model = Account
        fields = ("email","password1","type_of_card","civility","first_name","last_name","phone","societe","adresse1","adresse2","pays","activitee","langage","linkedin","facebook","cni_image","selfie")

    def clean_email(self):
        data_email = self.cleaned_data.get("email")
        if Account.objects.filter(email=data_email):
            raise forms.ValidationError('Cet email est déja affilié à un compte.')
        return data_email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Les deux mots de passes de concordent pas.')
        return password2

    def clean_langage(self):
        data = self.cleaned_data.get("langage")
        if data == "EMPTY":
            raise forms.ValidationError('Merci de choisir un langage.')
        return data

    def clean_activitee(self):
        data = self.cleaned_data.get("activitee")
        if data == "BASEACT":
            raise forms.ValidationError('Merci de choisir une activitée.')
        return data
    #EMPTY @ BASEACT

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')


    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        myuser = Account.objects.get(email=email)

        if not myuser.is_verified  or myuser.id_compte_wallester == None:
            raise forms.ValidationError("Votre compte n'est pas encore vérifié.")

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Email ou mot de passe erroné.")



class PasswordUpdateForm(PasswordChangeForm):

    class Meta:
        model = PasswordChangeForm

    def clean_old_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        old_password = self.cleaned_data.get("old_password")
        raise forms.ValidationError('Votre ancien mot de passe est incorrect.')
        return old_password

    def clean_new_password2(self):
        raise forms.ValidationError('Les deux mots de passes ne correspondent pas.')
    """def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Les deux mots de passes de concordent pas.')
        return password2"""




class NewCardFormAdmin(forms.Form):
    #3d_secure_settings
    secure_mobile = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class':'form-control'}),label='Numéro de téléphone :',help_text="Format : +33606060606")
    secure_password = forms.CharField(max_length=100,required=False,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Mot de passe :')
    #account_id
    account_id = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='ID du compte Wallester :')
    #delivery_address
    delivery_address_address1 = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Adresse :')
    delivery_address_city = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Ville :')
    delivery_address_company_name = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Nom de la société :')
    delivery_address_first_name = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Prénom :')
    delivery_address_last_name = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Nom :')
    delivery_address_phone = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Numéro de téléphone :',help_text="Format : +33606060606")
    delivery_address_postal_code = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Code postal :')

    #embossing_name
    embossing_name_firstname = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Prénom :')
    embossing_name_lastname = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}),label='Nom :')
