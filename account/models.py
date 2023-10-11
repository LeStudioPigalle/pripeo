from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin, AbstractUser
from django.conf import settings


class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    VIRTUELLE = "VIRTUELLE"
    PHYSIQUE = "PHYSIQUE"
    CARD_CHOICES = [
        (VIRTUELLE, "Virtuelle"),
        (PHYSIQUE, "Physique"),
    ]
    type_of_card = models.CharField(max_length=9,choices=CARD_CHOICES,default=VIRTUELLE)





class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password,**extra_fields):
        if not email:
            raise ValueError("Users must have an email adress")
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username=self.normalize_email(email),
            password=password,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password,first_name,last_name,adresse1,pays,cni_image,justif_dom,selfie):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name  =first_name,
            last_name = last_name,
            adresse1=adresse1,
            pays=pays,
            cni_image=cni_image,
            justif_dom = justif_dom,
            selfie=selfie,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=False)
    societe = models.CharField(max_length=50,blank=True)
    adresse1 = models.CharField(max_length=100,blank=False)
    adresse2 = models.CharField(max_length=100,blank=True)
    pays = models.CharField(max_length=100,blank=False)
    facebook = models.CharField(max_length=200,blank=True)
    linkedin = models.CharField(max_length=200,blank=True)
    cni_image = models.FileField(upload_to='account/files/verification',blank=False)
    justif_dom = models.FileField(upload_to='account/files/verification',blank=False)
    selfie = models.FileField(upload_to='account/files/verification',blank=False)
    is_verified = models.BooleanField(default=False)

    id_compte_wallester = models.UUIDField(blank=True,null=True,primary_key=False)


    VIRTUELLE = "VIRTUELLE"
    PHYSIQUE = "PHYSIQUE"
    CARD_CHOICES = [
        (VIRTUELLE, "Virtuelle"),
        (PHYSIQUE, "Physique"),
    ]
    type_of_card = models.CharField(max_length=9, choices=CARD_CHOICES, default=VIRTUELLE,blank=False)


    MONSIEUR = "MONSIEUR"
    MADAME = "MADAME"
    MADEMOISELLE = "MADEMOISELLE"
    EMPTY = "EMPTY"

    CIVILITY_CHOICES = [
        (MONSIEUR, "Monsieur"),
        (MADAME, "Madame"),
        (MADEMOISELLE, "Mademoiselle"),
        (EMPTY, "---"),
    ]
    civility = models.CharField(max_length=12, choices=CIVILITY_CHOICES, default=EMPTY,blank=False)

    BASEACTV = "BASEACT"
    SALARIE = "SALARIE"
    ENTREPRENEUR = "ENTREPRENEUR"
    INDEPENDANT = "INDEPENDANT"
    SANSEMPLOI = "SANSEMPLOI"
    ETUDIANT = "ETUDIANT"
    FONCTIONNAIRE = "FONCTIONNAIRE"

    ACTIVITEE_CHOICES = [
        (BASEACTV, "Choisir une activité..."),
        (SALARIE, "Salarié"),
        (ENTREPRENEUR, "Entrepreneur"),
        (INDEPENDANT, "Indépendant"),
        (SANSEMPLOI, "Sans emploi"),
        (ETUDIANT, "Etudiant"),
        (FONCTIONNAIRE, "Fonctionnaire"),

    ]
    activitee = models.CharField(max_length=50, choices=ACTIVITEE_CHOICES, default=BASEACTV, blank=False)

    FRANCAIS = "FRANCAIS"
    ANGLAIS = "ANGLAIS"
    MALAGASY = "MALAGASY"

    LANGUAGE_CHOICES = [
        (FRANCAIS, "Français"),
        (ANGLAIS, "Anglais"),
        (MALAGASY, "Malagasy"),
        (EMPTY, "---"),
    ]
    langage = models.CharField(max_length=12, choices=LANGUAGE_CHOICES, default=EMPTY,blank=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','adresse1','pays','cni_image','justif_dom','selfie']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True





