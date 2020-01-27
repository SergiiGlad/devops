## Jenkins

__Jenkins__ is an open source automation server written in Java. Jenkins helps to automate the non-human part of the software development process, with continuous integration and facilitating technical aspects of continuous delivery

## Node
A node is a machine which is part of the Jenkins environment and is capable of executing a Pipeline.

## SCM tools that Jenkins supports

The SCM or Source Code Management tools Jenkins supports are 
* SVN, 
* Clearcase, 
* CVS, 
* Git, 
* AccuRev, 
* Perforce, 
* RTC, 
* Mercurial.

## Types of pipelines in Jenkins

* CI CD pipeline (Continuous Integration Continuous Delivery)
* Scripted pipeline
* Declarative pipeline

## Agent

Agent specifies the execution point for a particular stage in the pipeline or the entire pipeline itself.

## Jenkins Master Slave Architecture

 * Jenkins Master-Slave architecture is important to accomplish Continuius Deployment
 * Jenkins Slave need to have Jenkins installed on them
 * Useful in scenarios where it distributes the load when we have parallel and complex builds

## CD Pipeline on Jenkins

Build step should have _Execute shell_ and _command__
