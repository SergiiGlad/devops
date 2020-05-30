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
* through the web-based console, 
* through the SDK and its command-line tools, 
* through the APIs, 
* through a mobile app.
