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

- You are required to create a service-orientated aThe core service 
– Service 1: this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.rchitecture for your application, an application must be made composed of at least 4 services that work together.
- Service 2 and 3: These will both generate a random “Object” of your choice
- This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
- The other constraint in this project is the technologies that need to be used. The project needs to utilise the technologies discussed during the training modules. 

        •	Kanban Board: Asana or an equivalent Kanban Board 

        •	Version Control: Git 

        •	CI Server: Jenkins 

        •	Configuration Management: Ansible

        •	Cloud server: GCP virtual machines 
    
        •	Containerisation: Docker 
- With this project brief in mind, I am going to create a app that generators a prediction for the user's 2020. this will be done by generating a random letter, a random number and using these two combinations to generate a prediction. 

# Planning

Below is my current trello board.

https://imgur.com/hXwjpBU

# Risk Assessment 

https://docs.google.com/document/d/1W1ctLVrTa-uyGnpgiuK6bnaBlaYGS575hKPwuGCXXgM/edit?usp=sharing

# CI Pipeline 

-Project Tracking; Trello used to track our project and keep on track with our timeline. 


-Source Code; Python and Flask. Flask is our web development framework using Jinja2.


-Version Control System; Git. THis records changes to files and allows for flexibility, security, and pull requests.



-CI Server; using webhooks, everytime a push is made onto Git, there is a build trigger on Jenkins which builds up my app using docker-compose.yaml. I used ansible as a configution management tool, so when I run anisble-playbook, creates a jenkins on one VM and the app deployment on the other VM by creating the key-gen. Ansible automates the key-gen and the ssh process allowing for jenkins to ssh into my app deployment VM, and it deploys my app using docker-stack. The benefits to using this are that there its open-source, so no human error. Most importantly, the build/ test and deployment stage is automated making it app scalable. 

-Testing Environment; Pytest (on GCP) Unit testing for each of the individual. 


-As live Environment; GCP. Cloud vendor used as it is more secure, scalable, pay as you go basis. 

# How to launch my app

- Fork my repo (the master branch)


