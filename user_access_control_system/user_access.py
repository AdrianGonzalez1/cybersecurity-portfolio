# Base class
class User:
    user_count = 0  # Class variable to track number of users created

    def __init__(self, username, role="Guest", access_level="Guest"):
        self.username = username
        self.role = role
        self.access_level = access_level
        User.user_count += 1

    def login(self):
        print(f"{self.username} has logged in as a {self.role}.")

    def get_permissions(self):
        return ["login"]


# Admin subclass
class Admin(User):
    def __init__(self, username):
        super().__init__(username, role="Admin", access_level="Admin")

    def get_permissions(self):
        return ["login", "change_password", "manage_users"]


# Analyst subclass
class Analyst(User):
    def __init__(self, username):
        super().__init__(username, role="Analyst", access_level="Analyst")

    def get_permissions(self):
        return ["login", "view_reports"]


# Guest subclass
class Guest(User):
    def __init__(self, username):
        super().__init__(username, role="Guest", access_level="Guest")

    def get_permissions(self):
        return ["login"]


# Test Script
if __name__ == "__main__":
    admin_user = Admin("admin_jane")
    analyst_user = Analyst("analyst_joe")
    guest_user = Guest("guest_mary")

    for user in [admin_user, analyst_user, guest_user]:
        user.login()
        print(f"Permissions for {user.username}: {user.get_permissions()}\n")

    print(f"Total users created: {User.user_count}")