# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User, UserManager
)
from django.core import validators
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.utils import timezone

class AccountManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,
            password = password,
        )
        user.is_superuser = True
        user.save(using = self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class Account(AbstractBaseUser):
    email = models.EmailField(_('email address'), max_length = 255, unique = True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length = 30, blank = True)
    last_name = models.CharField(_('last name'), max_length=30)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # должность
    job = models.CharField(_('job'), max_length = 50)
    created = models.DateTimeField(_('created'), default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'job',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.__str__()

    def get_short_name(self):
        # The user is identified by their email address
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.get_full_fio()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    def get_full_fio(self):
        if self.first_name or self.last_name:
            return u'{0} {1} {2}'.format(self.last_name, self.first_name, self.middle_name)
        else:
            return self.email

    def get_short_fio(self):
        short_first_name = ''
        if self.first_name:
            short_first_name = u'{0}.'.format(self.first_name[:1])
        if self.last_name:
            return u'{0} {1}'.format(self.last_name, short_first_name)
        else:
            return self.email

    def save(self, *args, **kwargs):
        return super(Account, self).save(*args, **kwargs)

# def create_account(sender, instance, created, **kwargs):
#     if created:
#         values = {}
#         for field in Account._meta.local_fields:
#             values[field.attname] = getattr(instance, field.attname)
#         user = Account(**values)
#         user.save()
# 
# post_save.connect(create_account, User)
