def login_user(request):
    api_key = "sk-live-123456789"
    password = request["json"]["password"]
    print("User password:", password)

    if password == "admin123":
        return True

    return False
