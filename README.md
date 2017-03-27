YAML TO LOSANT
=========================

The Yamltolosant is an applicatioin for  creating devices in losant platform , and send data to the created devices,The following are documents on what need to be done to work on the product.

Installation
------------
These are instructions on how to setup a platform where you can use application. These instructions are specifically for Ubuntu Linux. If you're on another OS, you can install Ubuntu inside a VM. 
Install ` virtualenv `  using 
`
sudo apt-get install virtualenv 

`
Run `git clone .` This will get a copy of the latest source code into the `yamltolosant` directory. We'll call this the "working directory". Go to this directory using ` cd yamltolosant `
Create a virtualenv using 
`
mkvirtualenv -p $(which python3) ~/iot_env

` 
Activate the virtualenv using 
`

. ~/iot_env/bin/activate

`
(don't forget the initial *.*).
Your prompt should have `(iot_env)` prefixed to it. 
Now you should be inside the `yamltolosant` directory and should have activated the `iot_env` environment. 
Install requirements inside virtualenv  using `pip install -r requirements.txt`

   Losant Account
=========================
There also need a losant account you can create it from https://www.losant.com
Then  Create Losant Application (for further details https://docs.losant.com/getting-started/walkthrough )
you can to see Application Id on the right upper corner , just copy it , and create application token ( https://docs.losant.com/applications/application-tokens/)

we will assume that your eamil is `me@mine.com` and password is `MYpassword` and applicationId is `myapplicationid` key is `mykeyvalue` and secret key as `mysecretkey`

Configure losant account with application
==========================================
just replace the email ,  password, applicationId , key , secret values at the yamltolosant.py then can to use the application by calling yamltolosant function with yaml file as argument
in this case 
    email = "me@mine.com"
    password = "MYpassword"
    applicationId = 'myapplicationid '
    key = 'mykeyvalue'
    secret = 'mysecretkey'


Example
-------
just run `python` from the working directory 

```
  >>> import yamltolosant
  >>> yamltolosant.yamltolosant("logger.yaml")
```
here i used logger.yaml file as input file which you get it by pulling this repository 
after successful compleation there create a new_device_info.json file with newly created device informations
