# Facial Recognition Application
It's just a simple express app which provides you with ability to continuously track the presence of conference participants.

## Getting Started

Clone this repository to your local machine.
##### clone repository
`$ git clone https://github.com/Kindest13/facial_recognition.git`

##### before the start install python, pip3, pipenv & node.js
* [python](https://wiki.python.org/moin/BeginnersGuide/Download) - installation guide (or just `$ brew install python3`)
* [pip3](https://pip.pypa.io/en/stable/installing/) - installation guide
* [pipenv](https://pypi.org/project/pipenv/) - installation guide
* [nodejs](https://nodejs.org/uk/download/) - installation guide

Go to the local copy of repository. Open terminal and run the following command
##### install all dependencies defined in package.json and requirements.txt
* `$ pip install -r requirements.txt`
* `$ npm i`

##### Set admin email
Set administrator' email and password to be able to send email with analytics to users' email.
![image](https://user-images.githubusercontent.com/41145554/119695101-87382280-be56-11eb-8f7d-32c77f901c9b.png)

##### run client
`$ npm start`

## Built With

* [Express](https://expressjs.com/) - client library
* [facial_recognition](https://face-recognition.readthedocs.io/en/latest/?badge=latest) - python facial recognition library
