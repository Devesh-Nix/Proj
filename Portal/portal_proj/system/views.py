from django.shortcuts import render ,redirect
from django.urls import path
from auth_system.auth_manager import user_login, user_logout
from auth_system.utils import dashboard
from auth_system.dashboard_content import get_dashboard_content

from .models import *
from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard_view(request):
#     # Dummy data for sales metrics
#     sales_data = {
#         "active_users": 100,  
#         "premium_users": 50,  
#         "total_users": 500,  
#         "total_employees": 30,  
#         "total_superadmins": 5,  
#         "total_admins": 10,  
#         "total_managers": 20,  
#         "total_sale": "10L",  
#         "yearly_sale": "10.2k",  
#         "monthly_sale": "4.2k",  
#         "weekly_sale": "80L",  
#         "daily_sale": "10L",  
#     }

#     return render(request, 'dashboard.html', sales_data)

# @login_required
# def manage_admin_view(request):
#     admins = Admin.objects.all()
#     print(admins)
#     return render(request, 'dashboard.html', {"admins": admins})


# def dashboard_view(request):
#     user_role = request.user.role  # Assuming role is stored in user model
#     content_permissions = get_dashboard_content(user_role)

#     return render(request, "dashboard.html", {"content_permissions": content_permissions})

def adm_view(request):
    return render(request,'adm_dashboard.html')

def dashboard(request):
    admins = Admin.objects.all()  # Load all admins
    return render(request, 'dashboard.html', {'admins': admins})

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
        last_user = useer.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_user.Sno) + 1) if last_user and last_user.Sno else "1"

        # Save to database
        useer.objects.create(
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