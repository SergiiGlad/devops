# Accessing the Google Cloud Console and Cloud Shell

https://partner.cloudskillsboost.google/course_sessions/1123594/labs/266754

* Create a virtual machine (VM) instance
* Explore the VM details
* Create an IAM service account
* Set the access control list for a Cloud Storage object
* Authenticate as a service account in Cloud Shell
* Install the nginx Web server
* Web page that contains the cat image

gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone us-central1-f
gcloud compute ssh gcelab2 --zone us-central1-f

cat << EOF > startup.sh
#! /bin/bash
apt-get update
apt-get install -y nginx
service nginx start
sed -i -- 's/nginx/Google Cloud Platform - '"\$HOSTNAME"'/' /var/www/html/index.nginx-debian.html
EOF