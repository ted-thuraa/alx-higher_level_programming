#!/bin/bash
#  script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
curl "$1" - X POST -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"