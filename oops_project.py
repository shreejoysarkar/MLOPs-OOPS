
import re
class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exist
                           
                           ->""")
        
        if user_input == "1": 
            self.signup()
        elif user_input =='2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        while True:
            
            email = input('enter your email here ->')
            password = input('setup your password here ->')
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is None:
                print("Invalid email format. Try again.")
                continue
            
        # Password validation: must be 8 digits
            if not password.isdigit() or len(password) != 8:
                print("Password must be exactly 8 digits. Try again.")
                continue

            print("Valid email and password accepted.")

            self.username = email
            self.password = password
            print('You have successfully signed up.')
            print('\n')
            self.menu()

    def signin(self):
        if self.username =="" and self.password=="":
            print("Please signup first. Pressing 1.")
        else:
            uname = input('enter your email/username here->')
            pwd = input('enter your password->')
            if self.username == uname and self.password == pwd:
                print("you have signed in successfully!!")
                self.loggedin=True

            else: 
                print("please input correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin ==True:
            txt = input('enter your post here->')
            print(f'Following content has been posted - {txt}')
        else :
            print('Sign in first to post something')
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input('Enter your message here ->')
            frnd = input('Whom to send the msg?')
            print(f'Message {txt}  sent successfully to ',{frnd})

        else:
            print('you need to signin first')
        print('\n')
        self.menu()

        

        


obj = chatbook()
