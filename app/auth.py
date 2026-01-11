def login_user(request):
    password = request["json"]["password"]
    print("User password:", password)

    if password == "admin123":
        return True

    return False
