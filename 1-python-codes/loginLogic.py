

class CreateAccount:
    def __init__(self, valid_user_name: str, valid_password: str):
        self.valid_user_name = valid_user_name
        self.valid_password = valid_password

    def getAccountDetails(self):
        return f'username: {self.valid_user_name} password:{self.valid_password}\n'

    def login(self):
        user_name = input("Enter username:\n")
        if user_name == self.valid_user_name:
            print(f'Hello {user_name}! Please enter password:\n')
            password = input("Enter password:\n")
            if password == self.valid_password:
                print(f'Logged In Successfully!!\n')
            else:
                print(f'**Invalid Password**\n')
        else:
            print(f'**Invalid User**\n')


if __name__ == "__main__":
    print("Create Account:\n")
    main_user_name = input("Enter username for account:\n")
    main_password = input("Enter password for account:\n")
    account = CreateAccount(main_user_name, main_password)
    print("Account Created Successfully!!!\n")
    account.getAccountDetails()

    print("Login to your account\n")
    account.login()
