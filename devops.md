_DevOps is the union of people, processes and products to enable continuous delivery of value to end users."_
                                                                                     - _Donovan Brown_ -


# How To Become a DevOps Engineer 

https://medium.com/@devfire/how-to-become-a-devops-engineer-in-six-months-or-less-366097df7737

DevOps is a way to deliver software with shared pain and responsibility.

**devops**:DevOps is meant to combine the words developer and operations.It's an engineering practice and culture of automating and monitoring infrastructure to build and run software and services.
**netdevops**: NetDevOps expands upon DevOps principles, extending the engineering practices to the network.

#### What is the difference between Pipeline and Project in Jenkins?

The main difference between any job and a Pipeline Job is that the Pipeline Scripted job runs on the Jenkins master, using a lightweight executor expected to use very few resources in order to translate the pipeline to atomic commands that execute or send to the agents.

![alt text](Foundation.png)



![alt text](six_parts.png)


### Continuous Integration (CI) and Continuous Deploymnent (CD) techniques and principals designed to automate the workflow of a modern app developer.

### A CI/CD server allows us to piece together actions for our pipeline such as test code, package code, deploy code with simple "if. then, else" style logic.

## CI - Continuous Intergation

  Development project often consists of many developers, all working on individual features and code. Eventually the individual work needs to be brought together and combined into a single code base. Individual developers should be testing their code as they work, but that code still needs re-verifying when it's part of the full codebase.
  Developing software requires planning for change, contibuously observing the results, and incrementally course-correcting based on the results. This is how CI operates.
  The practice of merging all developer working copies to a shared code line several times a day, and validating each integration with an automated build.

## CD - Continuous Delivery

  A software engineering approach in which teams produce software inshort cycles, ensuring thet software can be reliably released at any time. 
  In practice, continuous delivery focuses on an automated deployment pipeline.

## CD - Continuous Deployment
  Continuous Deploymnet is generally defined as a Continuous Delivery pipeline with no manual gates between initial code commit / check-in and production.

## Continuous Development ( CICD )

**Continuous development is the natural progression of iteration times shrinking into insignificance. Thtough heavy use of automation, flexible infrastructure and modular architecture, software development leaders have come to the point where each code change is its own deploymnet.

  * **Continuous Integration**: Merging of development work with code base constantly so that automated tetsing can catch problems early
  * **Continuous Delivery**: Software package delivery mechanism for releasing code to staging for review and inspection
  * **Continuous Deployment**: Relies on CI and CD to automatically release code into production as soon as it is ready. Constant flow of new features into production

Continuous Integration ----> Continuous Delivery ----> Continuous Deployment

![alt text](cicd.png)


**The microservice-based approach to architecting an application uses an API to expose discrete functions of the application; these functions are know as _microservices_**

### Container:
  * Containers may run on a bare-metal system or in a virtualized OS.
  * Containers (at least the Docker model) are "immutable", meaning that they cannot be changed. In fact, they are versioned, similar to source control.
  * An application in a container typically runs as **root**. However, it does not have unrestricted access to the entire system on which it runs.


