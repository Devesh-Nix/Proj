from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .dashboard_content import get_dashboard_content

@login_required
def dashboard(request):
    user = request.user
    role = user.role  # Get user role
    content_permissions = get_dashboard_content(role)  # Fetch content permissions

    return render(request, 'dashboard.html', {'content_permissions': content_permissions})
