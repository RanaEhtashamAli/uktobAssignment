# uktobAssignment

# Project Setup:

* Take pull of this repository.
* Create a new python virtual environment using following command:
  * For windows: python -m venv env
  * For Mac or Linux: python3 -m venv env
* Activate the python environment:
  * For windows: env/Scripts/activate
  * For Mac or Linux: source env\bin\activate
* Install all the dependencies listed in the requirements.txt with following command:
  * pip install -r requirements.txt

* Once done with the above commands. Create a new file called .env in the root folder. Copy the content of .env.example 
  file and paste it inside the .env file. Now update all the environment variable according to your local environment.
* Execute this command to migrate all the database tables: 
  * python manage.py migrate
* Execute the following command to create a user in database:
  * python manage.py createsuperuser
* This command will ask for a username and password. Provide them as per you like.


* Once all above things are done go to this URL: localhost:8000/api/schema/swagger-ui/
* Here you'll see all the available APIs in the project.
* Firstly open: /api/token/ post call. Click try it out. It will ask you to provide username and password. 
  Provide username and password of the user created above and click Execute.
* Below you'll see the access and refresh token response. Copy access token.
* Go the top of the page and click on the Authorize button. It will ask you about the access token paste the token and click Authorize.
* Then you can try out any notes API.
