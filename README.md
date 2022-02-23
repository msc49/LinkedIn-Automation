# LinkedIn Connection Automator

I decided I wanted to expand my LinkedIn connections for individuals who were in roles I was interested in. To make the process easier, I decided to automate it for myself.

This file automatically logs you in and adds connections for you; therefore, saving us all time.

The file randomly selects one of the following roles: software-engineer, full-stack-developer, backend-developer, front-end-developer, python-developer and blockchain-developer.

It then only looks for connects in London (where I am based) and people who went to my university to add. 


## Prerequisites

please make sure you have dotenv installed and selenium installed on your local machine. If you do not, then run the following commands:

```
pip install -U selenium
pip install python-dotenv
```

You must also download chromedriver, which you can do from the following link:
https://chromedriver.chromium.org/downloads

Once that is completed, cd into the respective directory where the chromedriver is located and run the following command:

```
mv /usr/local/bin
```
We are almost done!

Now clone this repository to your local machine and in your terminal run:

```
touch .env
```

Inside this file, add your email and password exactly as listed below

EMAIL=YOUREMAIL
PASSWORD=YOURPASSWORD

(Make sure the variables are capitalised or the main.py file may not recognise it)

## How to run

In your terminal, you can run:

```
python main.py
```

or depending on your machine

```
python3 main.py
```

This works because at the end of the main.py file, I have already created an instance of the class and called the connections method


