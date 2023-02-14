# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Asiel Garcia

## Lab Question Answers

Answer for Question 1: 
The reason that RESTful APIs are scalable is because they optimize client-server interactions. Statelessness removes server load because the server does not have to retain past client request information. As well as well managed caching being able to partially/completely eliminate some client-server interactions.

Question 2:
The resources that the mail server is providing to the clients is sender, reciever, subject, body and some other data that can be accessed such as inbox if that counts as part of the resources.

Question 3:
One common method not used in our mail server is PUT. We could extend our mail server to use this method by allowing it to update the instance of a resource by replacing the existing source(mail) with a new mail.

Question 4:
API keys are one option for REST API authentication. They are used to check if a client can access the resources. They will only be allowed to access the resources if they have a key that is unique and generated toa first-time client. Although they are less secure than other options, they do provide some security as well as tracking usage of that specific api.
...
