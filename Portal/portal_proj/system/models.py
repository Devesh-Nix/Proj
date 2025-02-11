from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('SuperAdmin', 'SuperAdmin'),
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('User', 'User'),
        ('Student', 'Student'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User')
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="system_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="system_user_permissions",
        blank=True
    )


class Admin(models.Model):
    Sno = models.AutoField(primary_key=True)  # Automatically increments
    admin_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=50, unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.admin_id:
            self.admin_id = f"ADM{self.Sno:04d}"  # Example: ADM0001
        super().save(*args, **kwargs)


class Manager(models.Model):
    Sno = models.AutoField(primary_key=True)  # Automatically increments
    manager_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    manager_id = models.CharField(max_length=50, unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.manager_id:
            self.manager_id = f"MGR{self.Sno:04d}"  # Example: MGR0001
        super().save(*args, **kwargs)


class Employee(models.Model):
    Sno = models.AutoField(primary_key=True)  # Automatically increments
    employee_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = f"EMP{self.Sno:04d}"  # Example: EMP0001
        super().save(*args, **kwargs)


class User(models.Model):
    Sno = models.AutoField(primary_key=True)  # Automatically increments
    user_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50, unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = f"USR{self.Sno:04d}"  # Example: USR0001
        super().save(*args, **kwargs)

class Student(models.Model):
    Sno = models.AutoField(primary_key=True)  # Automatically increments
    student_name = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True, blank=True) 
    registration_date = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = f"STU{self.Sno:04d}"  # Example: USR0001
        super().save(*args, **kwargs)

class College(models.Model):
    Sno = models.AutoField(primary_key=True)  # Automatically increments
    college_name = models.CharField(unique=True, max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    college_id = models.CharField(max_length=50, unique=True) 

