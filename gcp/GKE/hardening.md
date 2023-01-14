https://www.coursera.org/lecture/security-best-practices-in-google-cloud/hardening-your-clusters-tCd2w

With Google Kubernetes Engine, 
* the masters are patched and upgraded for you automatically, 
* and Node auto-upgrade also automatically upgrades nodes in your cluster.

## Automatic upgrade

There are three types of automatic upgrade:
* rapid
provides the latest Kubernetes releases as early as possible and will allow you to be able to use the new GKE features the moment they go GA, generally available. 

* regular is the default
provides access to GKE and Kubernetes features reasonably soon after they are released but on a more steady and predictable release cadence. Regular updates offer a good balance of feature availability and update stability and is recommended for most users.

* stable
provides the least frequent updates to provide more time for feature validation, it is recommended for users that prioritize stability over new functionality. 

It is good practice to regularly audit your cluster configuration for deviations from defined settings. Many of the recommendations covered in this section as well as common misconfigurations can be automatically monitored using the new security health analytics.

When __security health analytics__ has been enabled, it will run scans on your selected resources automatically, twice a day, 12 hours apart, and alert you if it finds any anomalies. 

## Limit the exposure of your cluster control plane and the nodes to the Internet.

By default, the GKE cluster control plane and nodes have Internet routable addresses 

### Private cluster 
that provides network-level protection to your GKE cluster control plane. 
* Public endpoint access enabled, master authorize networks disabled
this is a default setting and allows any public Internet user to make a connection to the control plane. To disable direct Internet access to nodes specify the gcloud tool option enable private nodes at cluster creation. 
* Public endpoint access disabled
this prevents all Internet access to both masters and nodes and works with networks using Cloud Interconnect and Cloud VPN.
* Public endpoint access enabled, master authorize networks enabled
gives the control plane a public IP address but installs a customer configurable firewall in front that allows public Internet connections without the use of a VPN.

* Keep in mind that Google Groups for GKE must be enabled while you are creating your clusters. 
* Upon cluster creation or update, specify the gcloud option enable shielded nodes.
shielded GKE nodes provide verifiable node identity and integrity. Shielded GKE nodes should be enabled with secure boot.

## Pods communicate 

Pods in the same cluster by default are able to communicate with each other without restrictions.
Restricting network access to services makes it much more difficult for attackers to move laterally within your cluster and also provide service protection against accidental or deliberate denial-of-service. 

### Restrict traffic between pods 
* use Istio which also offers load balancing, service authorization, throttling, quota, and metrics
* use Kubernetes network policies to provide basic access control functionality

## Secret management 
provides another level of security for authenticated secrets which are generally stored in the etcd directory.

* HashiCorp Vault
we'll need to configure a third-party secrets manager such as __HashiCorp Vault__ that can be integrated with GKE clusters and will need to be set up before creating your clusters. 
* use Kubernetes secrets natively in GKE making sure to encrypt these at the application layer with a key that you manage.

## Workload Identity 
removes the need to use nodes service accounts or to export service account keys into secrets.
__You should create and use a service account with a minimal privilege to run your GKE cluster instead of using the default compute engine service account.__
##### note that GKE requires at a minimum the service counts who have a monitoring.viewer, monitoring.metric writer, and logging.log writer roles. 

### To harden your clusters against discovery exploits, you can do the following: 
* configure authorized networks to restrict access to only a set of IP ranges. 
* Setup a private cluster to restrict access to only certain VPCs.
* Correct the subjects of the default system discovery and system basic user cluster role bindings to allow access by only certain known users and groups.
* A foundational security concept to give teams the least amount of privileges required to do that job and you can do that in Kubernetes by creating separate namespaces or clusters for each team and environment.
* It is also a good plan to assign cost centers and appropriate labels to each namespace for accountability and chargeback. 

## GKE ingress firewall

GKE also creates ingress firewall rules automatically when creating GKE clusters, services, and ingresses. The priority for all automatically created firewall rules is 1,000, which is the default value for firewall rules. If you'd like more control over firewall behavior, you can create firewall rules with a higher priority. Firewall rules with a higher priority are applied before automatically created firewall rules. Now, to avoid unexpected behavior in your clusters, do not modify or delete firewall rules created by GKE. 
