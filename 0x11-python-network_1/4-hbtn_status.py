#!/usr/bin/python3
"""fetche https://alx-intranet.hbtn.io/status"""
if __name__ == '__main__':
    import requests
    response = requests.get("https://alx-intranet.hbtn.io/status")
    html = response.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
