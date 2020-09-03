## Virtual Private Cloud (VPC)

* Pick persistend disk: standard or SSD 
* Pick local SSD for scratch space too if you need it
* Define a startup script if you like

Preemptible VMs

VPCs have routing tables to forward traffic within the network , even across subnets.
VPC routing tables are built in.
VPC belong to GCP project.
Excahnge traffic between two VPC peering does

__With global Cloud Load Balancing, your application presents a single front-end to the world__
* Users get a single, global anycast IP address
* Traffic goes over the Google backbone from the closest point-of-presence to the user
* Backends are selected based on load
* Only healthy backends receive traffic
* No pre-warming is required

__Cloud DNS is highly available and scalable__

__Cloud CDN (Content Delivery Network)__

* Use Google's globally distributed edge caches to cache content close to your users

## Shared VPC

When you use Shared VPC, you __designate a project__ as a host project and attach one or more other __service projects__ to it. 

The VPC networks in the host project are called __Shared VPC networks__.

__Shared VPC__ lets organization administrators delegate administrative responsibilities, such as creating and managing instances, to Service Project Admins while maintaining centralized control over network resources like subnets, routes, and firewalls. 

Shared VPC is also referred to as "XPN" in the API.


