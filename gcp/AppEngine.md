# App Engine

* App engine will scale your application automatically in response to the amount of traffic it receives
* you only pay for those resources you use 
* There are no servers for you to provision or maintain
* That's why App Engine is especially suited for applications where the workload is highly variable or unpredictable like web applications and mobile backend
* App Engine offers two environments: standard and flexible. 

## App Engine standard environment

* Easily deploy you application
* Autoscale workloads
* Free daily quota
* Usage best pricing

##### Requirements
Sandbox constrains:
* No writing to local files
* All requests time out at 60s
* Limits on third-party software

## App Engine flexible environment
* Build adm deploy conteinerized apps with a click
* No sandbox constraints
* Can access App Engine resources

Your application runs inside Docker containers on Google Compute Engine Virtual Machines, VMs.
App Engine manages these Compute Engine machines for you.

## Achieve continuous deployment to Google Kubernetes Engine (GKE) with Cloud Build

Make sure that the following APIs are enabled in the Google Cloud Console:

GKE API
Container Registry API
Cloud Build API
Cloud Source Repositories API