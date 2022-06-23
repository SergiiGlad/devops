Task 1: Set the default region and zone for all resources
In Cloud Shell, set the default zone:

gcloud config set compute/zone us-central1-a
Copied!
Set the default region:

gcloud config set compute/region us-central1
Copied!
Learn more about choosing zones and regions here: Regions and Zones documentation

Task 2: Create multiple web server instances
For this load balancing scenario, create three Compute Engine VM instances and install Apache on them, then add a firewall rule that allows HTTP traffic to reach the instances.

Create three new virtual machines in your default zone and give them all the same tag. The code provided sets the zone to us-central1-a. Setting the tags field lets you reference these instances all at once, such as with a firewall rule. These commands also install Apache on each instance and give each instance a unique home page.

gcloud compute instances create www1 \
  --image-family debian-9 \
  --image-project debian-cloud \
  --zone us-central1-a \
  --tags network-lb-tag \
  --metadata startup-script="#! /bin/bash
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>www1</h1></body></html>' | tee /var/www/html/index.html"
Copied!
gcloud compute instances create www2 \
  --image-family debian-9 \
  --image-project debian-cloud \
  --zone us-central1-a \
  --tags network-lb-tag \
  --metadata startup-script="#! /bin/bash
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>www2</h1></body></html>' | tee /var/www/html/index.html"
Copied!
gcloud compute instances create www3 \
  --image-family debian-9 \
  --image-project debian-cloud \
  --zone us-central1-a \
  --tags network-lb-tag \
  --metadata startup-script="#! /bin/bash
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>www3</h1></body></html>' | tee /var/www/html/index.html"
Copied!
Create a firewall rule to allow external traffic to the VM instances:

gcloud compute firewall-rules create www-firewall-network-lb \
    --target-tags network-lb-tag --allow tcp:80
Copied!
Now you need to get the external IP addresses of your instances and verify that they are running.

Run the following to list your instances. You'll see their IP addresses in the EXTERNAL_IP column:

gcloud compute instances list
Copied!
Verify that each instance is running with curl, replacing [IP_ADDRESS] with the IP address for each of your VMs:

curl http://[IP_ADDRESS]
Copied!
Check your lab progress
Click Check my progress below to verify that you've created a group of web servers.

Assessment Completed!
Create multiple web server instances
Assessment Completed!
Task 3: Configure the load balancing service
When you configure the load balancing service, your virtual machine instances will receive packets that are destined for the static external IP address you configure. Instances made with a Compute Engine image are automatically configured to handle this IP address.

For more information, see Setting Up Network Load Balancing.
Create a static external IP address for your load balancer:

gcloud compute addresses create network-lb-ip-1 \
 --region us-central1
Copied!
(Output)

Created [https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-03-xxxxxxxxxxx/regions/us-central1/addresses/network-lb-ip-1].
Add a legacy HTTP health check resource:

gcloud compute http-health-checks create basic-check
Copied!
Add a target pool in the same region as your instances. Run the following to create the target pool and use the health check, which is required for the service to function:

gcloud compute target-pools create www-pool \
    --region us-central1 --http-health-check basic-check
Copied!
Add the instances to the pool:

gcloud compute target-pools add-instances www-pool \
    --instances www1,www2,www3
Copied!
Add a forwarding rule:

gcloud compute forwarding-rules create www-rule \
    --region us-central1 \
    --ports 80 \
    --address network-lb-ip-1 \
    --target-pool www-pool
Copied!
Check your lab progress
Click Check my progress below to verify that you've created an L4 network load balancer that points to the web servers.

Assessment Completed!
Configure the load balancing service
Assessment Completed!
Task 4: Sending traffic to your instances
Now that the load balancing service is configured, you can start sending traffic to the forwarding rule and watch the traffic be dispersed to different instances.

Enter the following command to view the external IP address of the www-rule forwarding rule used by the load balancer:

gcloud compute forwarding-rules describe www-rule --region us-central1
Copied!
Use curl command to access the external IP address, replacing IP_ADDRESS with an external IP address from the previous command:

while true; do curl -m1 IP_ADDRESS; done
Copied!
The response from the curl command alternates randomly among the three instances. If your response is initially unsuccessful, wait approximately 30 seconds for the configuration to be fully loaded and for your instances to be marked healthy before trying again.

Use Ctrl + c to stop running the command.

Task 5: Create an HTTP load balancer
HTTP(S) Load Balancing is implemented on Google Front End (GFE). GFEs are distributed globally and operate together using Google's global network and control plane. You can configure URL rules to route some URLs to one set of instances and route other URLs to other instances. Requests are always routed to the instance group that is closest to the user, if that group has enough capacity and is appropriate for the request. If the closest group does not have enough capacity, the request is sent to the closest group that does have capacity.

To set up a load balancer with a Compute Engine backend, your VMs need to be in an instance group. The managed instance group provides VMs running the backend servers of an external HTTP load balancer. For this lab, backends serve their own hostnames.

First, create the load balancer template:

gcloud compute instance-templates create lb-backend-template \
   --region=us-central1 \
   --network=default \
   --subnet=default \
   --tags=allow-health-check \
   --image-family=debian-9 \
   --image-project=debian-cloud \
   --metadata=startup-script='#! /bin/bash
     apt-get update
     apt-get install apache2 -y
     a2ensite default-ssl
     a2enmod ssl
     vm_hostname="$(curl -H "Metadata-Flavor:Google" \
     http://169.254.169.254/computeMetadata/v1/instance/name)"
     echo "Page served from: $vm_hostname" | \
     tee /var/www/html/index.html
     systemctl restart apache2'
Copied!
Managed instance groups (MIGs) let you operate apps on multiple identical VMs. You can make your workloads scalable and highly available by taking advantage of automated MIG services, including: autoscaling, autohealing, regional (multiple zone) deployment, and automatic updating. Create a managed instance group based on the template:

gcloud compute instance-groups managed create lb-backend-group \
   --template=lb-backend-template --size=2 --region=us-central1

gcloud compute instance-groups managed set-named-ports lb-backend-group --named-ports=http:80 --zone=us-central1-a

Create the fw-allow-health-check firewall rule. This is an ingress rule that allows traffic from the Google Cloud health checking systems (130.211.0.0/22 and 35.191.0.0/16). This lab uses the target tag allow-health-check to identify the VMs.

gcloud compute firewall-rules create fw-allow-health-check \
    --network=default \
    --action=allow \
    --direction=ingress \
    --source-ranges=130.211.0.0/22,35.191.0.0/16 \
    --target-tags=allow-health-check \
    --rules=tcp:80
Copied!
Now that the instances are up and running, set up a global static external IP address that your customers use to reach your load balancer.

gcloud compute addresses create lb-ipv4-1 \
    --ip-version=IPV4 \
    --global
Copied!
Note the IPv4 address that was reserved:

gcloud compute addresses describe lb-ipv4-1 \
    --format="get(address)" \
    --global
Copied!
Create a health check for the load balancer:

gcloud compute health-checks create http http-basic-check \
    --port 80
Copied!
Google Cloud provides health checking mechanisms that determine whether backend instances respond properly to traffic. For more information, please refer to the document
Create a backend service:

gcloud compute backend-services create web-backend-service \
    --protocol=HTTP \
    --port-name=http \
    --health-checks=http-basic-check \
    --global
Copied!
Add your instance group as the backend to the backend service:

gcloud compute backend-services add-backend web-backend-service \
    --instance-group=lb-backend-group \
    --instance-group-zone=us-central1-a \
    --global
Copied!
Create a URL map to route the incoming requests to the default backend service:

gcloud compute url-maps create web-map-http \
    --default-service web-backend-service
Copied!
URL map is a Google Cloud configuration resource used to route requests to backend services or backend buckets. For example, with an external HTTP(S) load balancer, you can use a single URL map to route requests to different destinations based on the rules configured in the URL map:
Requests for https://example.com/video go to one backend service.
Requests for https://example.com/audio go to a different backend service.
Requests for https://example.com/images go to a Cloud Storage backend bucket.
Requests for any other host and path combination go to a default backend service.
Create a target HTTP proxy to route requests to your URL map:

gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map-http
Copied!
Create a global forwarding rule to route incoming requests to the proxy:

gcloud compute forwarding-rules create http-content-rule \
    --address=lb-ipv4-1\
    --global \
    --target-http-proxy=http-lb-proxy \
    --ports=80
Copied!
A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. For a general understanding of forwarding rules, see Forwarding rule concepts.
Check your lab progress
Click Check my progress below to verify that you've created an L7 HTTP(S) load balancer.

Assessment Completed!
Create an HTTP load balancer
Assessment Completed!
Task 6: Testing traffic sent to your instances
In the Cloud Console, from the Navigation menu, go to Network services > Load balancing.

Click on the load balancer that you just created (web-map-http).

In the Backend section, click on the name of the backend and confirm that the VMs are Healthy. If they are not healthy, wait a few moments and try reloading the page.

When the VMs are healthy, test the load balancer using a web browser, going to http://IP_ADDRESS/, replacing IP_ADDRESS with the load balancer's IP address.

This may take three to five minutes. If you do not connect, wait a minute, and then reload the browser.

Your browser should render a page with content showing the name of the instance that served the page, along with its zone (for example, Page served from: lb-backend-group-xxxx).

Congratulations!