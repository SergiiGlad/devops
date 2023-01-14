## DevOps Basics

What Is DevOps?
**DevOps** - is the practice of operations and development engineers participating together through the entire service lifecycle; from the design and development process all the way to production support. DevOps is also characterized by operations staff making use of many of the same techniques as developers for their systems work. https://theagileadmin.com/what-is-devops/

__DevOps__ is a software development practice which blends software development (Dev) with the IT operations (Ops) making the whole development lifecycle simpler and shorter by constantly delivering builds, fixes, updates, and features.

(google)  __DevOps__ is an organizational and cultural movement that aims to increase software delivery velocity, improve service reliability, and build shared ownership among software stakeholders.

(By Pavan Belagatti, Developer Advocate at Harness)
DevOps is a hot topic that is quickly becoming the way of software development. It aims to promote development speed and reduce costs while increasing productivity and efficiency in your organization. DevOps is powered by automating your entire development, delivery, and operations processes. With continuous integration (CI) and continuous delivery (CD), you can do more with less, so it is beneficial to start implementing these concepts into your company as early as possible.
What Is DevOps?
DevOps is a cultural phenomenon used by companies that like to release quality software fast. It is done by automating the entire development and delivery process with the help of techniques and tools. However, it is not just a set of tools but a broader movement that focuses on how to improve the flow of software by streamlining the processes and mindset.
The idea behind DevOps is to have an end-to-end automated pipeline from Dev (development) to Ops (operations). This way, the software moves quickly and can be tested as it moves through different phases of delivery and deployment. Continuous integration and continuous delivery become an essential part of the DevOps initiative and carry a lot of importance.

#### Kaizen’s Guiding Principles

* Good processes bring good results
* Go see for yourself to grasp the current situation (gemba)
* Speak with data, manage by facts
* Take action to contain and correct root causes of problems
* Work as a team
* Kaizen is everybody’s business

## DevOps tools

DevOps | Tools
--- | ---
Source code repository | Git CloudForce TFC Subversion
Build server | SonarQube Jenkins Artifactory
Configuration management | Puppet Ansible Salt Chef
Test automation | Selenium Water
Virtual infrastructure | Amazone Web Services Microsoft Azure VMware vCloud

## Infrastructure Automation

Infrastructure AS Code.

Infrastructure templates allow you to specify your project's infrastructure in a declarative and reusable way.

Infrastructure as code enables you to describe, through code, the infrastructure that you need for your application.
With infrastructure as code, you can maintain both your application code and everything you need to deploy your application in a central code repository. The advantages to infrastructure as code are:
* Consistent configurations
* Improved scalability
* Faster deployments
* Better traceability

### Golden Image to Foil Ball

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
SRE is a discipline that applies aspects of software engineering to operations whose goals are to create ultra-scalable and highly reliable software systems.
 Book
[Site Reliability Engineer](http://shop.oreilly.com/product/0636920041528.do)

__[What is SRE (site reliability engineering) ?](https://www.redhat.com/en/topics/devops/what-is-sre?utm_medium=Email&utm_campaign=weekly&sc_cid=7013a000002gUYhAAM "REDHAT Topics")__

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

## DevOps automation

__Continuous integration__ is a DevOps practice where developers continuously commit their code changes into a source repository. Then, at regular intervals, the system will conduct an automated build, deploy, and test.

The process of having shorter release cycles (sometimes serveral times a day) i.e creating small features and integrating them to the source code, and employing automated build and test processes for quicker feedback is called __Continuous Integration__

The advantages of Continuous Integration includes:
 * Frequent Commits hence small feature release
 * Automated Build and Testing
 * Instant Feedback to Developer
 * Low Risk and Faster Delivery
 

__Continuous delivery__ expands on continuous integration by automatically deploying code changes through the support environments, pausing for _approval_ before going to production.

__Continuous deployment__ does not wait for approval; rather, it goes to production automatically after successfully passing through automated testing in the support environments.


__Canary release__ is a technique to reduce the risk of introducing a new software version in production by slowly rolling out the change to a small subset of users before rolling it out to the entire infrastructure and making it available to everybod. - [MartinFowler.com](https://martinfowler.com/bliki/CanaryRelease.html)

## Jenkins

__Jenkins__ is an open source automation server written in Java. Jenkins helps to automate the non-human part of the software development process, with continuous integration and facilitating technical aspects of continuous delivery. It is a server-based system that runs in servlet containers such as Apache Tomcat. It supports version control tools, including AccuRev, CVS, Subversion, Git, Mercurial, Perforce, ClearCase and RTC, and can execute Apache Ant, Apache Maven and sbt based projects as well as arbitrary shell scripts and Windows batch commands. The creator of Jenkins is Kohsuke Kawaguchi. Released under the MIT License, Jenkins is free software.





