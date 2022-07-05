https://partner.cloudskillsboost.google/focuses/16374?parent=catalog#step1

# Overview
Terraform is the infrastructure as code offering from HashiCorp. It is a tool for building, changing, and managing infrastructure in a safe, repeatable way. Operators and Infrastructure teams can use Terraform to manage environments with a configuration language called the HashiCorp Configuration Language (HCL) for human-readable, automated deployments.

Infrastructure as code is the process of managing infrastructure in a file or files rather than manually configuring resources in a user interface. A resource in this instance is any piece of infrastructure in a given environment, such as a virtual machine, security group, network interface, etc. At a high level, Terraform allows operators to use HCL to author files containing definitions of their desired resources on almost any provider (AWS, Google Cloud, GitHub, Docker, etc.) and automates the creation of those resources at the time of apply.

A simple workflow for deployment will follow closely to the steps below:

__Scope__ - Confirm what resources need to be created for a given project.

__Author__ - Create the configuration file in HCL based on the scoped parameters.

__Initialize__ - Run terraform init in the project directory with the configuration files. This will download the correct provider plug-ins for the project.

__Plan & Apply__ - Run terraform plan to verify creation process and then terraform apply to create real resources as well as the state file that compares future changes in your configuration files to what actually exists in your deployment environment.

### Destructive Changes
A destructive change is a change that requires the provider to replace the existing resource rather than updating it. This usually happens because the cloud provider doesn't support updating the resource in the way described by your configuration.

### Destroy Infrastructure
You have now seen how to build and change infrastructure. Before moving on to creating multiple resources and showing resource dependencies, you will see how to completely destroy your Terraform-managed infrastructure.

Destroying your infrastructure is a rare event in production environments. But if you're using Terraform to spin up multiple environments such as development, testing, and staging, then destroying is often a useful action.

Resources can be destroyed using the terraform destroy command, which is similar to terraform apply but it behaves as if all of the resources have been removed from the configuration.

Try the terraform destroy command. Answer yes to execute this plan and destroy the infrastructure:

```terraform destroy```

### Implicit and Explicit Dependencies

By studying the resource attributes used in interpolation expressions, Terraform can automatically infer when one resource depends on another. In the example above, the reference to google_compute_address.vm_static_ip.address creates an implicit dependency on the google_compute_address named vm_static_ip.

Terraform uses this dependency information to determine the correct order in which to create and update different resources. In the example above, Terraform knows that the vm_static_ip must be created before the vm_instance is updated to use it.

Implicit dependencies via interpolation expressions are the primary way to inform Terraform about these relationships, and should be used whenever possible.

Sometimes there are dependencies between resources that are not visible to Terraform. The depends_on argument can be added to any resource and accepts a list of resources to create explicit dependencies for.

For example, perhaps an application you will run on your instance expects to use a specific Cloud Storage bucket, but that dependency is configured inside the application code and thus not visible to Terraform. In that case, you can use depends_on to explicitly declare the dependency.

### Defining a Provisioner

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "f1-micro"
  tags         = ["web", "dev"]
  provisioner "local-exec" {
    command = "echo ${google_compute_instance.vm_instance.name}:  ${google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip} >> ip_address.txt"
  }
  # ...
}

