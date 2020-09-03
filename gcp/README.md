## What is cloud computing?

__Cloud computing is a way of using I.T. that has these five equally important traits.__
 *  you get computing resources on-demand and self-service. 
 *  you access these resources over the net from anywhere you want. 
 *  the provider of those resources has a big pool of them and allocates them to customers out of that pool. 
 *  the resources are elastic. If you need more/less resources you can get , rapidly. 
 *  the customers pay only for what they use or reserve as they go. If they stop using resources, they stop paying. 
 
 _That's it. That's the definition of cloud._

## Virtualized data centers

 __Virtualized data centers__ brought you Infrastructure as a Service, IaaS, and Platform as a Service, PaaS offerings. 
 __IaaS__ offerings provide raw compute, storage, and network organized in ways that are familiar from data centers. 
 __PaaS__ offerings, on the other hand, bind application code you write to libraries that give access to the infrastructure your application needs. That way, you can just focus on your application logic. In the IaaS model, you pay for what you allocate. In the PaaS model, you pay for what you use. Both sure beat the old way where you bought everything in advance based on lots of risky forecasting. 

## How GCP is organized. 

__A Zone__ is a deployment area for Google Cloud Platform Resources. 
__Zones__ are grouped into regions, independent geographic areas, and you can choose what regions your GCP resources are in.
__All the zones__ within a region have fast network connectivity among them. Locations within regions usually have round trip network latencies of under five milliseconds. Think of a zone as a single failure domain within a region.

## Google Cloud Identity, and Access Management, 

also called IM, or IAM to control who can do what. 

The principle of least privilege is very important in managing.
This principle says that each user should have only those privileges needed to do their jobs.

There are four ways to interact with GCP's management layer: 
* through the cloud platform console - web user interface ( gcloud, gsutil Cloud Storage, bq BigQuery )
* through the SDK or Cloud shell - its command-line tools
* through the APIs - RESTful base API , JSON as interchange format , OAuth 2.0
* through a mobile app - Android or iOS

__An IAM policy__ has a "who" (identity), a "can do what" part (access), and an "on which resource" part. The "who" part names the user or users you're talking about.
who - google account, google group, service account, an entire GSuite or a Cloud Identity domain;

__An IAM policy__ is a collection of users and their roles.

can do what - part is defined by an IAM role;
#### There are three kinds of roles in Cloud IAM:
##### IAM primitive roles - apply across all GCP services in a project
 * owner
 * editor
 * viewer
 * billing administrator
_Be careful, if you have several people working together on a project that contains sensitive data, primitive roles are probably too coarse_

#### IAM predefined roles apply to a particular GCP service ina project
Compute Engines InstanceAdmin Role
Some companies decide they'd rather stick with the predefined roles. 

#### Custom
A lot of companies have a least-privileged model in which each person in your organization has the minimum amount of privilege needed to do his or her job.
Сustom roles can only be used at the project or organization levels. They can't be used at the folder level. 


What if you want to give permissions to a Compute Engine virtual machine, rather than to a person? 
__Then you would use a service account.__

Granting, changing and revoking access to resources

Treat your configuration as code and perform repeatable deployments.
