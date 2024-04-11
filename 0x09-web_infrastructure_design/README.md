Here is a basic task in the system engineering repository
It contains taskes that sets us up to understad basic network setting

**To foster my understanding in the web infracstruture design**

here are answers to asked questions

**========================TASK ONE================**
You must be able to explain some specifics about this infrastructure:

**What is a server?**

A server is a basic computer component which processes and stores data which can be access
uppon rewuest.

A server can either be in form of an hardware or software components and they run in in an OS design model.

**What is the role of the domain name**

A domain name is used to cloud an ip address for clients readability whic is more easier to memorize that random numerical values.

**What type of DNS record www is in www.foobar.com**
The type of dns record www is in foobar is an A record DNS record type. This is beacuse it points a domain name to its ip adress.

**What is the role of the web server**
The role of a web server is to store and process static web pages as result upon request from clients.

**What is the role of the application server**

An application server stores an process business logic upon request. Business logi here means all the algorithm, functions, and programs a sofware needs to display to make an application or web page functional.

**What is the role of the database**

A database is used to store data or information related to any aspect of business operations. It can be very large, depending on the opration is it intended to cary out.

**What is the server using to communicate with the computer of the user requesting the website**
What the server uses to communicate with the computer is the HTTP (Hyper Text Transfer Protocol). The browser send this reques to the server asking it to response with available web page of an ip.

**explaining what the issues are with this infrastructure**
The design in task one lacks many functionalities for security and efficiency.

**SPOF** The SPOF(Single Point of Failure) is when much load is being placed on a single server. That is, a design with only one sever running can experince server breakdown beacuse of high traffic. Cannot scale if too much incoming traffic and also, there are no monitoring system

**Downtime when maintenance needed**
This type of design would definitely expereinced downtime during a maintenace schedule beacuse its server sould be
down and there would be no backup

**========================TASK TWO================**

You must be able to explain some specifics about this infrastructure:

**For every additional element, why you are adding it**
The load balancer distribute traffic among servers for efficiency

**What distribution algorithm your load balancer is configured with and how it works**
The load balancer distibutive algorithm is the round robin schedle method where each server recieves traffic after the other had recieved. That is, the traffic are distibuted sequencially to all servers.

**Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both**
The load balancer is enables to perform active-passive. This enable maintenace to be carried out without interuspting the servers

Active-active: Active-active signifies a configuration where multiple nodes in a network are simultaneously active and operational. In this setup, all nodes are engaged in processing requests and can independently handle user traffic. 

**How a database Primary-Replica (Master-Slave) cluster works**
It enables data from one database server (primary, previously known as “master”) to be replicated to one or more database servers (secondaries, previously known as “slaves”)

**What is the difference between the Primary node and the Replica node in regard to the application**
I have no idea!

**==========Task 2==========**

For every additional element, why you are adding it
**What are firewalls for**
Firewall are used to block malicious traffic or threats from users or clients

**Why is the traffic served over HTTPS**
Traffic served over HTTPS are generally secured becasue all communication are encrypted

**What monitoring is used for**
Monitoring is used to track the generally activities and data of esach server. It takes care of troubleshooting, and remediation of network performance issues

**How the monitoring tool is collecting data**
Server monitoring tools track the activity on the server by streaming event logs, also called log files, that the server automatically generates.

**Explain what to do if you want to monitor your web server QPS**
I would generally say, connect the monitors to the servers.
