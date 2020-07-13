
# Infrastructure as code

__The concept behind Deployment Manager is "infrastructure as code". You can treat the templates like code, placing them under version control in a repository, and so forth.__


# Deployment Manager

Setting up your environment in GCP can entail many steps: 
* setting up compute network and storage resources, 
* and keeping track of their configurations.

If you want to change your environment, you figure out the commands to change it from the old state to the new. 
If you want to clone your environment, you do all those commands again. This is a lot of work. 

It's more efficient to use a template. That means a specification of what the environment should look like. 
It's declarative rather than imperative. GCP provides Deployment Manager to let you do just that. 

It's an Infrastructure Management Service that automates the creation and management of your Google Cloud Platform resources for you. 
To use it, you create a template file using either the YAML markup language or Python that describes what you want the components of your environment to look like. 
Then, you give the template to Deployment Manager, which figures out and does the actions needed to create the environment your template describes. 
If you need to change your environment, edit your template and then tell Deployment Manager to update the environment to match the change. 

Here's a tip: you can store and version control your Deployment Manager templates in Cloud Source repositories.


#### To print the entire list of resource types, type the following command.
```
gcloud deployment-manager types list

gcloud deployment-manager types list --filter="name ~ ^compute\.v1\."

gcloud services list --available

gcloud beta billing accounts list

gcloud beta deployment-manager type-providers describe pubsub-v1 --project gcp-types

gcloud beta deployment-manager types list --provider compute-v1 --project gcp-types

```

## Deployment Manager Infrastructure CodeLab

https://codelabs.developers.google.com/codelabs/gcp-infra-deployment-manager/index.html?index=..%2F..cloud#2


##### Enable the Deployment Manager and Compute Engine APIs

https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/tree/master/dm/templates/project

The Google Cloud Deployment Manager v2 API provides services for configuring, deploying, and viewing Google Cloud services and APIs via templates which specify deployments of Cloud resources.

##### Activate the following APIs for the DM Creation Project:

* Google Cloud Deployment Manager V2 API
* Google Cloud Resource Manager API
* Google Cloud Billing API
* Google Identity and Access Management (IAM) API
* Google Service Management API

You may use the gcloud services enable command to do this:
```sh
gcloud services enable deploymentmanager.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable cloudbilling.googleapis.com
gcloud services enable iam.googleapis.com
gcloud services enable servicemanagement.googleapis.com
```

You can use Python or Jinja2 to create templates for Deployment Manager. We recommend that you use Python templates, because Python allows for greater flexibility and more features as you scale your application. It is possible to mix and match templates.

One advantage of using templates for your deployment is the ability to create and define custom properties, which let you reuse templates across zones, regions, and projects.

You can use references to define the properties of your configuration or templates instead of directly providing values.

##### Configuration file structure
```
#  imported templates, if applicable
imports:
  #  path relative to the configuration file
- path: path/to/template.jinja
  name: my-template
- path: path/to/another/template.py
  name: another-template

resources:
  - name: NAME_OF_RESOURCE
    type: TYPE_OF_RESOURCE
    properties:
      property-a: value
      property-b: value
      ...
      property-z: value
  - name: NAME_OF_RESOURCE
    type: TYPE_OF_RESOURCE
    properties:
      property-a: value
      property-b: value
      ...
      property-z: value
```

##### Previewing a new configuration
```
gcloud deployment-manager deployments create example-config --config configuration-file.yaml --preview
```     


https://console.developers.google.com/apis/library/sqladmin.googleapis.com?project=turing-archway-254318

#### Update values script
```
source ~/cpo200/config

sed -i \
-e s/'<guestbook-project-id>'/$DEVSHELL_PROJECT_ID/g \
-e s/'<your-default-zone>'/$CPO200_ZONE/ \
-e s/'<guestbook-sql-connection-name>'/$CPO200_SQL_CONNECTION_NAME/ \
-e s/'<guestbook-sql-password>'/$CPO200_SQL_PW/ \
-e s/'<guestbook-external-ip-address>'/$CPO200_GB_DM_IP/ \
-e s/'<startup-scripts-bucket>'/$CPO200_SCRIPTS_BUCKET/ \
guestbook-basic.yaml
```

## Templates for manageability
A huge configuration file can be difficult to manage. Templates are a way to break down configurations into composable units that can be separately updated and can be reused. Templates are included in the *.yaml configuration using import:.

Here are some of the benefits of Deployment Manager templates:

* Composability - easier to manage and maintain definitions.
* Reusability - easy to reuse definitions across deployments.
* Maintainability - maintain consistent definitions in one place.
* The Deployment Manager configuration and template files use two kinds of variables, template variables and environment variables.

Template variables are abstract properties that allow you to declare the value to be passed to the template in the *.yaml configuration file. You can change the value for each deployment in it's *.yaml file without having to make changes to the underlying templates.

Example: Passing zone as a template variable allows you to start a test deployment in a different zone from the production deployment.

Environment variables allow you to reuse templates in different projects and deployments. Rather than representing properties of resources, they represent more global properties such as a Project ID or a the name of the deployment.

Example: You want to start the same deployment in two projects, proj-east and proj-west. You could declare environment variables for the two Project IDs and then use these in the Deployment Manager configuration files.
