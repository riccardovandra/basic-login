### FUNCTIONS ###


def login():
    login_name = input('Login Username: ')
    with open('users.txt', 'r') as users:
        u = {}
        # For every line in the users file read and create 2 variables to append in a dict
        for line in users:
            key, value = line.strip().split('\t')
            u[key] = value
            # print(u)
            # print(u.get(login_name))
        if login_name in u:  # If the login name that you typed exists in the dictionary
            print('Username exists, you need to type the password')
            password = input(login_name + ',insert your password ')

            if password == u.get(login_name):
                print('access granted')
            else:
                print(login_name, ',typed the wrong password')
        else:
            print('No username with this name,please try another username or exit')

# TODO - allow multiple users to register


def register():
    with open('users.txt', 'a+') as f:  # if it's not there create it
        username = input('Type the username that you want ')
        password = input('Type the password that you want ')
        f.write(username + '\t' + password)
    print('your profile is correctly registered')
    main()


### MAIN PROGRAM ###

def main():
    welcome_message = input(
        'Hello user, to login type "login" or you can register by typing "register" ')

    if welcome_message == 'login':
        login()
    elif welcome_message == 'register':
        register()
    else:
        print('Your selected option is not available')
        main()


main()
