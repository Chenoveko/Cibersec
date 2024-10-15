import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \n HASH CRACKER for SHA256")
print(ascii_banner)

wordlist_location = str('/usr/share/wordlists/PythonForPentesters/wordlist2.txt')
hash_input = str('5030c5bd002de8713fef5daebd597620f5e8bcea31c603dccdfcdf502a57cc60')

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password! ' + line.strip())
            exit(0)