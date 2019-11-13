# ProfanityCheck
Usage:
Set up python3. If you have issues, set up python3 as a virtual environment
Guide for virtual environment: https://stackoverflow.com/questions/10763440/how-to-install-python3-version-of-package-via-pip-on-ubuntu


Then install the following packages using pip3: 

- profanity-check

- flask

- flask-restful


Running the program:

In terminal, first run:
```
python3 sym.py 
```
This will start the server for the API

Now, you must add profane words to the database. To do this, send a POST request with the endpoint /explict. 
The header should be a multi-part form with the following parameters:
- id (as an int)
- word (as a string)

To run the profanity checker, send a POST request using the endpoint /send with the json input in the header
See demo.json for example json input

Files:
- sym.py- sets up the API environment and begins the testing server. Calls censor.py
- censor.py- the main program which runs the profanity checks
- symbaloo.db- the database file which will store the forbidden words
- demo.json- a demo json file used as input in the post request
