def get_dashboard_content(role):
    """Returns dashboard content based on user role"""
    content = {
        "SuperAdmin": [
            "Dashboard",
            "Request",
            "Admin",
            "Manager",
            "Employee",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "Admin": [
            "Dashboard",
            "Manager",
            "Employee",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "Manager": [
            "Dashboard",
            "Employee",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "Employee": [
            "Dashboard",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],

    }

    return content.get(role, [])  # Default to an empty list if the role is missing
