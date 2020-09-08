SUDO:
sudo dnf install snapd
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install heroku --classic
Modify path:
PATH=$PATH:/var/lib/snapd/snap/bin
-----------
$ pip install pipenv
$ pip install gnicorn
$ cd project_dir
$ python -m venv ./venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ pip install gnicorn
$ pip freeze > requirements.txt
$ vi Procfile
  
-----
$ heroku login
###$ heroku git:clone -a dsrblog
### $ cd dsrblog
Make some changes to the code you just cloned and deploy them to Heroku using Git.
$ git config --local user.email "dsrawat.temp@gmail.com"
$ git config --local user.name "Dharmender Rawat"
$ git add .
$ git commit -am "make it better"
$ git push heroku master
----------
https://dsrblog.herokuapp.com/
https://git.heroku.com/dsrblog.git
Troubleshooting:
$ heroku logs --tail
2020-09-01T07:06:17.285050+00:00 heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/favicon.ico" host=dsrblog.herokuapp.com request_id=e757bc40-e112-47a8-9830-9c5d85ae15e1 fwd="157.119.215.133" dyno= connect= service= status=503 bytes= protocol=http
$ heroku ps:scale web=1
--> Add Procfile -in the same folder where you have git, manage.py
	<contents:>
	web: gunicorn app:run
$ git add .
$ git commit -am "added gunicorn"
$ git push heroku master
$ heroku ps:scale web=1
