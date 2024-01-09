from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from django_countries.fields import CountryField


GENDER=(
    ('Select','Select'),
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
MARITAL_STATUS=(
    ('Select','Select'),
    ('Married','Married'),
    ('Unmarried','Unmarried'),
    ('Others','Others')
)
ROLE=(
    ('Select','Select'),
    ('Manufacture/Seller','Manufacture/Seller'),
    ('Buyer','Buyer'),
    ('Both','Both')
)
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)



class Registration_All(AbstractBaseUser):
    #p_k=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=1000,null=True,blank=True)
    last_name=models.CharField(max_length=1000,null=True,blank=True)
    email=models.EmailField(null=True,blank=True,unique=True)
    mobile=PhoneNumberField(unique=True, null=False, blank=False,help_text='adjust with country code')
    country=CountryField(blank_label=("Select Country"))
    address=models.CharField(max_length=1000,null=True,blank=True)
    date_of_joining=models.DateTimeField(auto_now_add=True)
    role=models.CharField(max_length=1000,choices=ROLE,default='Select')
    #Password=models.TextField(null=False,blank=False)
    #Confirm_Password=models.TextField(null=False,blank=False)

    #registration sesh hole,,vitore dhuke profile update korte hobe
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    gender=models.CharField(max_length=1000,choices=GENDER,default='Select')
    marital_status=models.CharField(max_length=1000,choices=MARITAL_STATUS,default='Select')
    blood_group=models.CharField(max_length=1000,null=True,blank=True)
    soacial_link=models.TextField(null=True,blank=True)
    date_of_birth=models.CharField(max_length=1000,null=True,blank=True)

    #Company details
    company_name=models.CharField(max_length=1000,null=True,blank=True)
    company_address=models.CharField(max_length=2000,null=True,blank=True)
    company_contact_number=models.CharField(max_length=1000,null=True,blank=True)
    company_logo=models.ImageField(upload_to='images/',null=True,blank=True)

    #Bank details
    bank_name=models.CharField(max_length=2000,null=True,blank=True)
    card_or_account_number=models.TextField(null=True,blank=True)
    branch_name=models.CharField(max_length=2000,null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return '('+str(self.role+')')+' '+str(self.email)
