Step 1: Verify that python is installed, make sure it is not 3.8.4 as there are issues with that version.
Step 2: Create a virtual environment and once you've activated it, make sure to run 'pip install -r requirements.txt'
Step 3: Run the following command 'python .\manage.py runserver'
Step 4: if you get the usual flask is running on then you should be able to access http://127.0.0.1:5000/user/signup 

virtual environment is https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 

Notes: Currently the DB config is set to work locally but I have not test it and we'll have to move it to a mysql or postgres instance.
       this readme is also not properly formatted but I am currently too lazy.

Ping me on discord if you have any issues but bare with me as I am busy until the evenings. 