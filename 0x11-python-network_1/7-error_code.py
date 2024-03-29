#!/usr/bin/python3
#!/usr/bin/python3
"""displays the body of the response."""
if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        html = response.text
        print(html)