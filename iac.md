
# Infrastructure as Code Tools

#### Some open-source IaC tools can be categorized into various groups:

• Configuration management tools – Chef, Puppet, and Ansible are popular tools that allow you to install, update, and manage resources on existing infrastructure.
• Server templating tools – Tools like Docker and Vagrant allow you to create an image from a configuration file, which is then used to provision infrastructure in a repeatable manner. They promote the idea of an immutable infrastructure, which we will explain later in this article.
• Container orchestration tools – Tools like Kubernetes and Docker Swarm allow you to orchestrate container workloads in a dynamic cloud-native landscape.
• Provisioning tools – Tools like Terraform, Azure Resource Manager, Google Cloud Deployment Manager, and AWS CloudFormation allow you to provision servers and other resources in the respective cloud environment.

#### Mutable vs. Immutable Infrastructure

With immutable infrastructure, you create a new server with the revised configuration if you want to modify an existing server. In a cloud-native environment, where containers are spinning up and down every minute, immutability is a required feature. You should package your application and its dependencies into a container image, and as you want to modify the configuration, you deploy a new container version.
The pets vs. cattle analogy for infrastructure management is popular in the dynamic container space. You treat your infrastructure resources like cattle so that you can delete and build them from scratch when a configuration change is required. Pets are indispensable resources where you make configuration changes in place. Immutability helps simplify your operations, minimize drift, boost consistency between environments, and build a secure infrastructure.
Declarative vs. Procedural Approach
With a procedural approach, you write separate scripts to achieve the desired state. Over time, you tend to have many scripts that have been applied to your environment, and you can review the modifications via change history. The order of execution of the scripts matters, or else you end up with a different end state. Tools like Chef and Puppet follow the procedural style of infrastructure management. 

With the declarative approach, you maintain the desired state in a configuration template. If you want to make any modifications, you update the same template to reflect the desired state and let the IaC tool generate the difference script and apply it to the environment. Tools like Terraform follow the declarative approach, where the code in source control always reflects the current state of the infrastructure. The declarative approach helps you to create reusable code since you are just focused on describing the desired state and offloading the complexity of syncing the current and desired state to the IaC tool.

#### Using Terraform to Manage Infrastructure

Terraform is a cloud-agnostic, open-source tool for infrastructure provisioning. Created by HashiCorp in 2014, Terraform uses HashiCorp Configuration Language (HCL) to describe infrastructure code. It supports many providers and can help manage resources in individual cloud providers, such as AWS, Azure, and Google Cloud. Terraform is backed by a large and growing community. The primary function of Terraform is to help you create, modify, and destroy infrastructure resources.

#### Infrastructure Automation With GitOps

GitOps workflows apply DevOps best practices for application development (version control, code review, automated deployments, etc.) to infrastructure deployments. GitOps is based on the declarative model, where configuration files get stored in Git, and approved changes get automatically deployed to the environment. 