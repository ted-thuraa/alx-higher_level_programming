#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) """
if __name__ == '__main__':
    from urllib import request
    from urllib import parse
    from sys import argv
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        test = response.read().decode('UTF-8')
        print(test)
