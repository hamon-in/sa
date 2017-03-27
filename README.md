YAML TO LOSANT
=========================

The Yamltolosant is an applicatioin for  creating devices in losant platform , and send data to the created devices 

Installation
------------

For use this application just pull this repo  and install the requirment for that run this command after activating a vitualenvironment  can be installed using
   ``` pip install -r requirements.txt 
   ```
   Losant Account
=========================
There also need a losant account you can create it from https://www.losant.com
Then  Create Losant Application (for further details https://docs.losant.com/getting-started/walkthrough )
you can to see Application Id on the right upper corner , just copy it , and create application token ( https://docs.losant.com/applications/application-tokens/)

Configure losant account with application
==========================================
just replace the email ,  password, applicationId , key , secret values at the first five line then can to use the application by calling yamltolosant function with yaml file as argument

Example
-------
from the python shell 

```
  >>> import yamltolosant
  >>> yamltolosant.yamltolosant("logger.yaml")
```
here i used logger.yaml file as input file which you get it by pulling this repository 
after successful compleation there create a new_device_info.json file with newly created device informations
