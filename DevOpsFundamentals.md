## DevOps Basics

What Is DevOps?
**DevOps** - is the practice of operations and development engineers participating together through the entire service lifecycle; from the design and development process all the way to production support. DevOps is also characterized by operations staff making use of many of the same techniques as developers for their systems work. https://theagileadmin.com/what-is-devops/


#### Kaizen’s Guiding Principles

* Good processes bring good results
* Go see for yourself to grasp the current situation (gemba)
* Speak with data, manage by facts
* Take action to contain and correct root causes of problems
* Work as a team
* Kaizen is everybody’s business

## Infrastructure Automation

Infrastructure AS Code

#### Golden Image to Foil Ball

**Provisioning** is the process of making a server ready for operation, including hardware, OS, system services, network connectivity.

**Deployment** is the process of automatically deploying and upgrading applications on a server.

**Orchestration** is the act of performing coordinated operations across multiple systems.

**Configuration management** is an overarching term dealing with change control of system configuration after initial provision, but is often also applied to maintaining and upgrading application and application dependencies. 

**Imperative** - also known as “procedural,” this is an approach where commands desired to produce a state are defined and executed. 

**Declarative** - also known as “functional,” this is an approach where you define a desired state and the tool converges the existing system on the model.

**Idempotent** - the ability to execute the CM procedure repeatedly and end up in the same state each time. 

**Self service** - is the ability for an end user to kick off one of these processes without having to go through other people.

## Continuous Delivery

#### Continuous Delivery has the following benefits:
1.	Time to market goes down
2.	Quality increases not decreases
3.	Limits your Work In Progress
4.	Shortens lead times for changes
5.	Improves Mean Time To Recover

#### Continuous Integration Practices

1.	Builds should pass the coffee test (< 5 minutes)
2.	Commit really small bits
3.	Don’t leave the build broken
4.	Use a trunk based development flow
5.	Don't allow flaky tests, fix them!
6.	The build should return a status, a log, and an artifact

#### The Continuous Delivery Pipeline

1.	Only build artifacts once
2.	Artifacts should be immutable
3.	Deployment should go to a copy of production before going into production
4.	Stop deploys if it a previous step fails
5.	Deployments should be idempotent


## Reliability Engineering

**Engineering Doesn't End With Deployment**

#### Operate For Design: Metrics and Monitoring

The 6 Monitoring Areas
1.	Service Performance and Uptime
2.	Software Component Metrics
3.	System Metrics
4.	App Metrics
5.	Performance 
6.	Security

## The Future of DevOps

##### Cloud to Containers to Serverless

**cloud computing** is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction” 





