from django.shortcuts import render ,redirect
from django.urls import path
from auth_system.auth_manager import user_login, user_logout
from auth_system.utils import dashboard
from auth_system.dashboard_content import get_dashboard_content

from .models import *
from django.contrib.auth.decorators import login_required

def adm_view(request):
    admins = Admin.objects.all()  # Fetch all admins for better data handling (optional)
    
    context = {
        "admins": admins,
    }

    return render(request, 'adm_dashboard.html', context)


def dashboard(request): 
    admins = Admin.objects.all()  # Load all admins
    employees = Employee.objects.all()  # Fetch all employees
    users = User.objects.all()  # Fetch all users
    students = Student.objects.all()  # Fetch all students
    colleges = College.objects.all()  # Fetch all colleges

    context = {
        
        "employees": employees,
        "admins": admins,
        "users": users,
        "students": students,
        "colleges": colleges,
    }
    return render(request, 'dashboard.html', context)

def add_admin(request):
    if request.method == "POST":
        admin_name = request.POST.get("admin_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        admin_id = request.POST.get("admin_id")

        # Generate next Sno
        last_admin = Admin.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_admin.Sno) + 1) if last_admin and last_admin.Sno else "1"

        # Save to database
        Admin.objects.create(Sno=next_sno, admin_name=admin_name, email=email, password=password, phone=phone, admin_id=admin_id)

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect

def add_user(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_id = request.POST.get("user_id")
        phone = request.POST.get("phone")

        # Generate next Sno
        last_user = User.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_user.Sno) + 1) if last_user and last_user.Sno else "1"

        # Save to database
        User.objects.create(
            Sno=next_sno, 
            user_name=user_name, 
            email=email, 
            password=password, 
            user_id=user_id, 
            phone=phone
        )

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect


def add_student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        student_id = request.POST.get("student_id")
        registration_date = request.POST.get("registration_date")

        # Generate next Sno
        last_student = Student.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_student.Sno) + 1) if last_student and last_student.Sno else "1"

        # Save to database
        Student.objects.create(
            Sno=next_sno, 
            student_name=student_name, 
            email=email, 
            password=password, 
            student_id=student_id, 
            registration_date=registration_date
        )

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect


def add_college(request):
    if request.method == "POST":
        college_name = request.POST.get("college_name")
        location = request.POST.get("location")
        contact = request.POST.get("contact")
        college_id = request.POST.get("college_id")

        # Generate next Sno
        last_college = College.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_college.Sno) + 1) if last_college and last_college.Sno else "1"

        # Save to database
        College.objects.create(Sno=next_sno, college_name=college_name, location=location, contact=contact, college_id=college_id)

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect


def add_employee(request):
    if request.method == "POST":
        employee_name = request.POST.get("employee_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        employee_id = request.POST.get("employee_id")

        # Generate next Sno
        last_employee = Employee.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_employee.Sno) + 1) if last_employee and last_employee.Sno else "1"

        # Save to database
        Employee.objects.create(Sno=next_sno, employee_name=employee_name, email=email, password=password, phone=phone, employee_id=employee_id)

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect

def add_manager(request):
    if request.method == "POST":
        manager_name = request.POST.get("manager_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        manager_id = request.POST.get("manager_id")

        # Generate next Sno
        last_manager = Manager.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_manager.Sno) + 1) if last_manager and last_manager.Sno else "1"

        # Save to database
        Manager.objects.create(Sno=next_sno, manager_name=manager_name, email=email, password=password, phone=phone, manager_id=manager_id)

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect

def emp_dashboard(request):
    if request.method == "POST":
        if 'update_user' in request.POST:
            user_id = request.POST.get("user_id")
            try:
                user = User.objects.get(user_id=user_id)
                user.user_name = request.POST.get("user_name", user.user_name)
                user.email = request.POST.get("email", user.email)
                user.phone = request.POST.get("phone", user.phone)
                new_password = request.POST.get("password")
                if new_password:
                    user.password = new_password
                user.save()
            except User.DoesNotExist:
                pass
            return redirect('emp_dashboard')
        if 'delete_user' in request.POST:
            user_id = request.POST.get("user_id")
            try:
                user = User.objects.get(user_id=user_id)
                user.delete()
            except User.DoesNotExist:
                pass
            return redirect('emp_dashboard')
    users = User.objects.all()
    students = Student.objects.all()
    colleges = College.objects.all()
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        'users': users,
        'students': students,
        'colleges': colleges,
    }
    return render(request, 'emp_dashboard.html', context)

def manager_view(request):
    
    employees = Employee.objects.all()  # Fetch all employees
    admins = Admin.objects.all()  # Fetch all admins
    users = User.objects.all()  # Fetch all users
    students = Student.objects.all()  # Fetch all students
    colleges = College.objects.all()  # Fetch all colleges

    context = {
        
        "employees": employees,
        "admins": admins,
        "users": users,
        "students": students,
        "colleges": colleges,
    }

    return render(request, "manager_dashboard.html", context)


