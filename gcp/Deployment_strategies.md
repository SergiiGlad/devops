# Deploying new versions of software always carries risk.

We want to make sure we test new versions effectively before going live, and when ready to deploy a new version, we do so with zero downtime.
Let me discuss some strategies that can help achieve these objectives.

#### Rolling update

Rolling updates allow you to deploy new versions with no downtime.
The typical configuration is to have multiple instances of a service behind a load balancer.
A rolling update will then update one instance at a time.
This strategy works fine if the API is not changed, or is backward compatible or if it is okay to have two versions of the same service running during the update.
If you are using instance groups, rolling updates are a built-in feature.
You just define the rolling update strategy when you perform the update.
For Kubernetes, rolling updates are there by default.
We just need to specify the replacement Docker image.
Finally, for App Engine, rolling updates are completely automated.

#### Blue-green
Use a blue-green deployment when you don't want multiple versions of a service to run simultaneously.
Blue-green deployments use twofold deployment environments.
The blue deployment is running the current deployed production software while the green-deployment environment is available for deploying updated versions of the software.
When you want to test a new software version, you deploy it to the green environment.
Once testing is complete, the workload is shifted from the current, which would be the blue in this case, to the new, the green environment.
This strategy mitigates the risk of a bad deployment by allowing they switchback to the previous deployment if something goes wrong.
For Compute Engine, you can use DNS to migrate requests, while in Kubernetes you can configure your service to route to new pods using labels, which is just a simple configuration change.
App Engine allows you to split traffic, which you explored in the previous lab of this course.

#### Canary releases
Now, you can use Canary releases prior to rolling update to reduce risk.
With a Canary release, you make a new deployment with the current deployment still running.
Then you send a small percentage of traffic to the new deployment and monitor it.
Once you have confidence in your new deployment, you can route more traffic to the new deployment until 100 percent is routed this way.
In Compute Engine, you can create a new instance group and add it to the load balancer as an additional back end.
In Kubernetes, you can create a new pod with the same labels as the existing pods.
The service will automatically divert a portion of the request to the new pod.
In App Engine, you can again use the traffic splitting feature to drive a portion of traffic to the new version.

# Introduction to Heterogeneous deployments

Heterogeneous deployments typically involve connecting two or more distinct infrastructure environments or regions to address a specific technical or operational need. Heterogeneous deployments are called "hybrid", "multi-cloud", or "public-private", depending upon the specifics of the deployment. For the purposes of this lab, heterogeneous deployments include those that span regions within a single cloud environment, multiple public cloud environments (multi-cloud), or a combination of on-premises and public cloud environments (hybrid or public-private).

Various business and technical challenges can arise in deployments that are limited to a single environment or region:

Maxed out resources: In any single environment, particularly in on-premises environments, you might not have the compute, networking, and storage resources to meet your production needs.
Limited geographic reach: Deployments in a single environment require people who are geographically distant from one another to access one deployment. Their traffic might travel around the world to a central location.
Limited availability: Web-scale traffic patterns challenge applications to remain fault-tolerant and resilient.
Vendor lock-in: Vendor-level platform and infrastructure abstractions can prevent you from porting applications.
Inflexible resources: Your resources might be limited to a particular set of compute, storage, or networking offerings.
Heterogeneous deployments can help address these challenges, but they must be architected using programmatic and deterministic processes and procedures. One-off or ad-hoc deployment procedures can cause deployments or processes to be brittle and intolerant of failures. Ad-hoc processes can lose data or drop traffic. Good deployment processes must be repeatable and use proven approaches for managing provisioning, configuration, and maintenance.

Three common scenarios for heterogeneous deployment are multi-cloud deployments, fronting on-premises data, and continuous integration/continuous delivery (CI/CD) processes.

The following exercises practice some common use cases for heterogeneous deployments, along with well-architected approaches using Kubernetes and other infrastructure resources to accomplish them.