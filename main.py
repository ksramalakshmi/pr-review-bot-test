from app.auth import login_user

def main():
    request = {
        "json": {
            "username": "admin",
            "password": "admin123"
        }
    }

    login_user(request)

if __name__ == "__main__":
    main()
