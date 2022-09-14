import requests as reqs
import optparse
from time import sleep

def input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-u", "--url", dest="url", help="URL with parameter that you want to check.")
    parse_object.add_option("-w", "--wordlist", dest="wordlist", help="Use your wordlist that contains XSS payloads.")
    parse_object.add_option("-t", "--time", dest="time", help="Set timing template. Each request for the second you set.")

    (user_input, args) = parse_object.parse_args()

    if not user_input.url:
        print("Please enter a URL. For help -h or --help")
    if not user_input.wordlist:
        print("Please enter a wordlist. For help -h or --help")
    if not user_input.time:
        print("Please enter a time. For help -h or --help")

    return user_input

def request(url, parameter):
    response = reqs.get(url + parameter)
    print(f"\rSending request {i+1} of {len(list)}", end="")
    if (response.status_code == 200):
        print(f"\nline {i+1} --> {parameter} would be vulnerable.")
def wordlist(wordlist):
    list = []
    with open(wordlist, encoding='utf8', errors='ignore') as f:
        for line in f:
            list.append(line.rstrip('\n'))
    return list

user_input = input()

try:
    while True:
        list = wordlist(user_input.wordlist)
        time = float(user_input.time)
        for i in range(len(list)):
            request(user_input.url, list[i])
            sleep(time)
except KeyboardInterrupt:
    print(f"\nSent {i+1} of {len(list)} request. Quitting.")
except TypeError:
    print("")