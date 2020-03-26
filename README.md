# Texas_corona
simple API on cases in Texas


### Getting Started
Go to https://github.com/Darius-Ndubi/Texas_corona.git
Download or clone the repository to your local machine. 
Open the project using your ide

----
#### Prerequisites
 - Python 3 and above.
 - Virtual environment.
 - Flask
 - flask-restplus
 - Postman or insomnia
 - Browser e.g Chrome, firefox
 
 ----
  #### Installing
Create a virtual enviroment. *virtualenv name_of_virtual_enviroment.
Folder with the 'name_of_virtual_enviroment' will be created and that is out enviroment.
Navigate inside the folder, open folder called Scripts or scripts and run the script activate. *Type activate
Clone this repo to your local computer using git clone https://github.com/Darius-Ndubi/Fast-Food-Fast-API
Switch into the project directory
Install the project's dependencies by running pip install -r requirements.txt 
    if using pipenv run `pipenv install' in the virtual environment
Run the app locally with python run.py or python3 run.py
Navigate to your project folder and open it using the terminal.

#### Application requirements
The requirements.txt files will contain all the requirements needed for the application. 
To install the requirements :

  pip install -r requirements.txt
  
Ensure you are located within the project directory and your virtual environment is activated 
Some of the third party modules that will be installed are:

- flask - Python module used for building web application.
- flask-restplus - flask extension used for developing API.

create a .env and in it add
  - export APP_DEBUG=""
  
Save the file and on terminal run source .env_sample

#### Postman
User order features. 
Endpoint available for this api are shown in the table below:

````
| Requests    |   EndPoint                     | Functionality                         | Fields
| ----------- |:------------------------------:| -------------------------------------:|

|  GET        |  /api/v1/<county_name>         | Number of cases per county in texas   |
|  GET        |/api/v1/per_capita/<county_name>| Number of cases per capita in county  |
````
 
Run application on postman

  http://127.0.0.1:5000/api/v1/<county_name>
  

  
 ***
 
 #### Built using

* python 3.6
* Flask
* flask-restplus


#### Versioning
Most recent version: version 1

***

#### Authors
Darius Ndubi
