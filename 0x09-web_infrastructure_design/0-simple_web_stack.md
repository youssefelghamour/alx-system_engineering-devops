![Image of a simple web infrastructure](0-simple_web_stack.PNG)

# Simple Web Infrastructure Representation

This is a representation of a simple web infrastructure, composed of a single server with a LAMP stack that hosts the website reachable via www.foobar.com. It is composed of: 1 server, 1 web server (Nginx), 1 application server, 1 application files (code base), 1 database (MySQL), 1 domain name foobar.com configured with a www record that points to the server IP 8.8.8.8.

## Basics

##### What is a server?

A server is a dedicated computer with special software or hardware that makes it more powerful than a normal computer. A server can be both a software and a hardware. Its purpose is to deliver services to other computers that, in this context, are referred to as clients.

##### What is the role of the domain name?

Domain names serve as a human-friendly alias to refer and access websites. Thanks to the DNS, websites can be accessed using their domain names, and the DNS handles the translation of these names to their corresponding IP addresses.

##### What type of DNS record www is in www.foobar.com?

www is a CNAME record for www.foobar.com, and it points to the same IP address as foobar.com.

##### What is the role of the web server?

The role of a web server is to handle HTTP requests from the user and provide responses by serving static content directly or managing dynamic content by interacting with an application server.

##### What is the role of the application server?

The application server collaborates with the web server to deliver dynamic responses to the user. It serves as the engine that runs the application by retrieving the code base and actively interacting with the database.

##### What is the role of the database?

The role of the database is to store, manipulate, and retrieve data when needed.

##### What is the server used to communicate with the computer of the user requesting the website?

The communication between the server and the user’s computer follows the TCP/IP protocols, adhering to the OSI model, which acts as the standard framework for internet communication.

## Issues with this infrastructure

##### SPOF: Single Point of Failure

This framework presents multiple Single Points of Failure (SPOFs). For example, in the case of a failure in one component, the website will be inaccessible.

##### Downtime during Maintenance

During the maintenance of one of the components, such as restarting the web server for code deployment, the website will have to be down, temporarily rendering the website inaccessible to users.

##### Cannot Scale if Too Much Incoming Traffic

This framework will have difficulties when facing a high volume of incoming traffic, resulting in downtime or performance issues.

To address these problems, we can implement redundancy measures and introduce a load balancer to handle and distribute the incoming traffic to multiple servers.

