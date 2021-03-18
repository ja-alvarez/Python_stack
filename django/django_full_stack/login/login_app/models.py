from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
#from datetime import datetime
from django.core.validators import validate_email

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name description should be at least 2 characters"
        try:
            validate_email(postData['email'])
        except:
            errors['email'] = 'Please enter a valid email'
        if len(postData['password'])<8:
            errors['password'] = 'Password must be at least eight characters long'
        if postData['confirmpassword'] != postData['password']:
            errors['confirmation'] = 'Your passwords did not match'
        return errors

#My UserManager
'''
    def basic_validator(self, postData):
        errors = {}
        if len(User.objects.filter(email=postData['email']))>0:
            errors['exists'] = 'Email already registered!'  #revisar exists* en views*
        else: 
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):        
                errors['email'] = "Email looks wrong. Check and write it again!"
#            if len(postData['email']) < 1:
#                errors['email'] = 'Your email looks too short!'
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name description should be at least 2 characters"
        if len(postData['password'])<8:
            errors['password'] = 'Password must be at least eight characters long'
        if (postData['confirmpassword']) != (postData['password']): #No es la longitud la que valido acá****
            errors['confirmpassword'] = "Passwords didn't match"
        return errors

    def encrypt (self, password):
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return password

    def validate_login (self, postData, user):
        errors = {}
        if len(user) > 0:
            pw_given = postData ['password']
            pw_hash = user[0].password
            if bcrypt.checkpw(pw_given.encode(), pw_hash.encode()) is False:
                errors['incorrect_pass'] = 'Your password is incorrect'         ###### incorrect_pass - pass_incorrecto
        else:
            errors['invalid_user'] = "User doesn't exit"                          ########### invalid_user* usuario_invalido
        return errors
'''
#DATE
'''
            if (postData['birth'] == None): #I had written None instead of 0
                errors['birth'] = 'Tell us your birthday :)'
            else: 
                fecha = postData['birth']
                fechanacimiento = datetime.strptime(fecha, "%Y-%m-%d") #check this!: format or errors in date
                hoy = datetime.now()              #"%d/%m/%Y"
                diferencia = hoy - fechanacimiento
                edadActual = diferencia.days / 365
                if edadActual < 16:
                    errors['birth'] = 'You need to be over 16 years old to access'
'''

class User (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100)
#    birthday = models.DateTimeField(auto_now_add=False)  #DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()