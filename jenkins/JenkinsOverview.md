# Jenkins

Jenkins is an automation tool written in Java with built-in plugins for continuous integration tasks. It is used to continuously build and test projects making it easier to integrate the changing codes to it.

Jenkins takes care of the rest of the process of build, deployment, testing, and analysis by automating it.

Provides great collaboration between development and operations team, making it into a single DevOps team

https://opensource.com/article/18/8/devops-jenkins-2

One of the key ideas of DevOps is infrastructure-as-code—having the infrastructure for your delivery/deployment pipeline expressed in code—just as the products that flow it.

Let's start by talking about the foundations. Jenkins and its plugins make the building blocks available for your pipeline tasks via its own programming steps—the Jenkins domain-specific language (DSL).

## DSL steps

When Jenkins started evolving toward the pipeline-as-code model, some of the earliest changes came in the form of a plugin—the workflow plugin. This included the creation of a set of initial DSL steps that allowed for coding up simple jobs in Jenkins and, by extension, simple pipelines.

## Scripted Pipelines

The original approach for creating pipelines in Jenkins 2 is now referred to as scripted. At the highest level, Scripted Pipelines are wrapped in a node block. Here a __node__ refers to a system that contains the Jenkins agent pieces and can run jobs (formerly referred to as a slave instance).

The node gets mapped to a system by using a __label__. A label is simply an identifier that has been added when configuring one or more nodes in Jenkins (done via the global Manage Nodes section).

## Stages

Although this simple node block is technically valid syntax, Jenkins pipelines generally have a further level of granularity—stages. A stage is a way to divide up the pipeline into logical functional units. It also serves to group DSL steps and Groovy code together to do targeted functionality. 

Each stage in a pipeline also gets its own output area in the new default Jenkins output screen—the __Stage View__. 

## Declarative Pipelines

As the name suggests, declarative syntax is more about declaring what you want in your pipeline and less about coding the logic to do it. It still uses the DSL steps as its base, but includes a well-defined structure around the steps. This structure includes many directives and sections that specify the items you want in your pipeline.

## Jenkinsfiles

Although the Jenkins application is the main environment for developing and running our pipelines, the pipeline code itself can also be placed into an external file named Jenkinsfile. Doing this then allows us to treat our pipeline code as any other text file—meaning it can be stored and tracked in source control and go through regular processes, such as code reviews.

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
