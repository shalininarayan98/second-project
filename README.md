https://github.com/shalininarayan98/playbook-repo

http://35.195.200.179 

https://docs.google.com/presentation/d/1RjkNUI4BVYoT0clRnXZObMbO2OmpbApUUo3wm4cVACA/edit?usp=sharing

# second-project
**Table of Contents**

* [The Brief](#the-brief)
* [Planning](#planning)
* [Risk Assessment](#Riks-Assessment)
* [Deployment CI Pipeline](#Dpeloyment&CI-Pipeline)
* [Testing](#Testing)
* [Commands to launch my app](#Commands-to-launch-my-app)
* [Future Improvements](#Future-Improvements)


# The Brief

- At its core you are creating an application that generates “Objects” upon a set of predefined rules.  These “Objects” can be from whatever domain you wish.
– Service 1: this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.rchitecture for your application, an application must be made composed of at least 4 services that work together.
- Service 2 and 3: These will both generate a random “Object” of your choice
- This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
- The other constraint in this project is the technologies that need to be used. The project needs to utilise the technologies discussed during the training modules. 

     •	Kanban Board: Asana or an equivalent Kanban Board 

     •	Version Control: Git 

     •	CI Server: Jenkins 

     •	Configuration Management: Ansible

     •	Cloud server: GCP virtual machines 
    
     •	Containerisation: Docker python3
from application import db
from application.models import Posts
db.create_all()
- With this project brief in mind, I am going to create a app that generators a prediction for the user's 2020. This will be done by generating a random number (service 1), generating a random letter (service 2), and using these two combinations to generate a prediction (service 3), which is rendered on service 4.

# Planning

Below is my current trello board.

https://imgur.com/hXwjpBU

# Risk Assessment 

https://docs.google.com/document/d/1W1ctLVrTa-uyGnpgiuK6bnaBlaYGS575hKPwuGCXXgM/edit?usp=sharing

# CI Pipeline 

- Project Tracking; Trello used to track our project and keep on track with our timeline. 


- Source Code; Python and Flask. Flask is our web development framework using Jinja2.


- Version Control System; Git. THis records changes to files and allows for flexibility, security, and pull requests.



- CI Server; using webhooks, everytime a push is made onto Git, there is a build trigger on Jenkins which builds up my app using docker-compose.yaml. I used ansible as a configution management tool, so when I run anisble-playbook, creates a jenkins on one VM and the app deployment on the other VM by creating the key-gen. Ansible automates the key-gen and the ssh process allowing for jenkins to ssh into my app deployment VM, and it deploys my app using docker-stack. The benefits to using this are that there its open-source, so no human error. Most importantly, the build/ test and deployment stage is automated making it app scalable. 

- Testing Environment; Pytest (on GCP) Unit testing for each of the individual. 


- As live Environment; GCP. Cloud vendor used as it is more secure, scalable, pay as you go basis. 

# Testing

https://docs.google.com/document/d/1s-c1OT_L4W9cS5aSCJQldkYx2WjmsfufwfRjJAKW3t8/edit?usp=sharing 

# How to launch my app

- Clone this repo (the master branch)
- Create an empty SQL database and set the environmnet variables in your ~/.bashrc in the following format:

   export MY_SQL_USER={username}
   
   export MY_SQL_PASSWORD={password}
   
   export MY_SQL_URL={IP address of SQL database}
   
   export MY_SQL_DB={name of database}
   
   export SECRET_KEY={create a secret key of your choice}
   
   
- cd into service3 and build your database by using the commands 
  python3
  from application import db
  db.application.models import Predictions
  db.create_all()
- Now we need to fill in the table with data entries. It should follow the following structure
  p1=Prediction(predictions=' ')
  db.session.add(p1)
  db.session.commit()
  (Now repeat this so you have 9 data entries, you can make the predictions whatever you like!)
  
- Next we will build my app using docker. Please install docker and docker-compose and add your user to the docker group
- Build my app using 'docker-compose.yaml up -d --build'
- Open the IP address of your VM and see what your 2020 has in store for you!

# Future Improvements 

- Make my SQL database deployable by dockerising it so there is no need to build your own SQL database to use my app.
- Front end design
- User registration and login so users can save their predictions 


