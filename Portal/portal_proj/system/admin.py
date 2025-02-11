from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from system.models import *

# Register CustomUser with UserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'admin_name', 'email', 'admin_id', 'phone')
    search_fields = ('admin_name__username', 'email', 'admin_id')
    
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'manager_name', 'email', 'manager_id', 'phone')
    search_fields = ('manager_name__username', 'email', 'manager_id')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'employee_name', 'email', 'employee_id', 'phone')
    search_fields = ('employee_name__username', 'email', 'employee_id')

@admin.register(useer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'user_name', 'email', 'user_id', 'phone')
    search_fields = ('user_name__username', 'email', 'user_id')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'student_name', 'email', 'student_id', 'registration_date')
    search_fields = ('student_name__username', 'email', 'student_id')

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('Sno', 'college_name', 'location', 'contact', 'college_id')
    search_fields = ('college_name__username', 'location', 'college_id')
