
# Infrastructure as Code Tools

#### Some open-source IaC tools can be categorized into various groups:

| Category | Tools | Description |
|----------|-------|-------------|
| Configuration management tools | Chef, Puppet, Ansible | Popular tools that allow you to install, update, and manage resources on existing infrastructure. |
| Server templating tools | Docker, Vagrant | Allow you to create an image from a configuration file, which is then used to provision infrastructure in a repeatable manner. They promote the idea of an immutable infrastructure. |
| Container orchestration tools | Kubernetes, Docker Swarm | Allow you to orchestrate container workloads in a dynamic cloud-native landscape. |
| Provisioning tools | Terraform, Azure Resource Manager, Google Cloud Deployment Manager, AWS CloudFormation | Allow you to provision servers and other resources in the respective cloud environment. |

#### Mutable vs. Immutable Infrastructure

With immutable infrastructure, you create a new server with the revised configuration if you want to modify an existing server. In a cloud-native environment, where containers are spinning up and down every minute, immutability is a required feature. You should package your application and its dependencies into a container image, and as you want to modify the configuration, you deploy a new container version.
The pets vs. cattle analogy for infrastructure management is popular in the dynamic container space. You treat your infrastructure resources like cattle so that you can delete and build them from scratch when a configuration change is required. Pets are indispensable resources where you make configuration changes in place. Immutability helps simplify your operations, minimize drift, boost consistency between environments, and build a secure infrastructure.

#### Declarative vs. Procedural Approach

| Approach | Description | Tools |
|----------|-------------|-------|
| Procedural | You write separate scripts to achieve the desired state. Over time, you tend to have many scripts that have been applied to your environment, and you can review the modifications via change history. The order of execution of the scripts matters, or else you end up with a different end state. | Chef, Puppet |
| Declarative | You maintain the desired state in a configuration template. If you want to make any modifications, you update the same template to reflect the desired state and let the IaC tool generate the difference script and apply it to the environment. The code in source control always reflects the current state of the infrastructure. This approach helps you to create reusable code since you are just focused on describing the desired state and offloading the complexity of syncing the current and desired state to the IaC tool. | Terraform |

#### Using Terraform to Manage Infrastructure

Terraform is a cloud-agnostic, open-source tool for infrastructure provisioning. Created by HashiCorp in 2014, Terraform uses HashiCorp Configuration Language (HCL) to describe infrastructure code. It supports many providers and can help manage resources in individual cloud providers, such as AWS, Azure, and Google Cloud. Terraform is backed by a large and growing community. The primary function of Terraform is to help you create, modify, and destroy infrastructure resources.

#### Infrastructure Automation With GitOps

GitOps workflows apply DevOps best practices for application development (version control, code review, automated deployments, etc.) to infrastructure deployments. GitOps is based on the declarative model, where configuration files get stored in Git, and approved changes get automatically deployed to the environment. 

# Infrastructure as Code 2.0

https://www.javacodegeeks.com/2026/02/infrastructure-as-code-2-0.html

## 1. What Changed Between IaC 1.0 and 2.0?

| Problem | IaC 1.0 Answer | IaC 2.0 Answer |
| :--- | :--- | :--- |
| Infra drift (reality ≠ code) | Periodic manual audits | Continuous drift detection |
| Security misconfigurations | Post-deploy vulnerability scans | Policy-as-Code enforced pre-deploy |
| Multi-team ownership | Monolithic Terraform state | Modular, decoupled state + Platform teams |
| Secrets in config files | Committed to repos (oops) | Vault, SOPS, or native secret managers |
| Cost visibility | Monthly surprise cloud bill | Cost estimation before applying changes |
| Writing boilerplate | Copy-paste from existing modules | AI-assisted scaffolding |



## 2. Pillar 1: Policy as Code 

If IaC 1.0 was “describe what you want,” IaC 2.0 adds “and enforce what’s allowed.” Policy as Code (PaC) means your security rules, compliance requirements, and organizational standards are written as machine-readable policies that run automatically — before anything is provisioned.

The two dominant tools here are Open Policy Agent (OPA) with its Rego language, and Checkov, which scans Terraform, CloudFormation, and Kubernetes manifests for misconfigurations before they ever touch a cloud environment.

## 3. Pillar 2: Drift Detection
> Drift is entropy applied to your infrastructure. It accumulates slowly and announces itself loudly.
> 
> — Kelsey Hightower, former Google Cloud Developer Advocate

## 4. Pillar 3: GitOps for Infrastructure

Tool	| Best For	| Hosted / Self-hosted	| Open Source
|---|---|---|---|
Atlantis	| Terraform GitOps via PRs |	Self-hosted	| Yes
Flux CD	| Kubernetes manifest sync	| Self-hosted (in-cluster)	| Yes
Argo CD	| Kubernetes + UI dashboard	| Self-hosted (in-cluster)	| Yes
Spacelift	| Multi-tool IaC orchestration	| Hosted SaaS	| Commercial
env0	| Terraform + cost controls	| Hosted SaaS	| Commercial

## 5. Pillar 4: AI-Assisted Infrastructure

* Scaffolding and boilerplate generation
* Explain and audit existing infra
* Cost optimization recommendations

## 6. The Practical Starting Point

| Phase | What to Add | Tooling | Time Investment |
| :--- | :--- | :--- | :--- |
| 1 — Secure | Add Checkov to your CI pipeline | Checkov, pre-commit hooks | 1–2 days |
| 2 — Observe | Run automated drift detection weekly | Terraform scheduled plans, Driftctl | 2–3 days |
| 3 — Govern | Replace direct CLI applies with PR-based workflow | Atlantis or Spacelift | 1–2 weeks |
| 4 — Optimize | Add cost estimation to every PR | Infracost | 2–3 days |
| 5 — Scale | Modularize state, adopt Platform Engineering model | Terraform modules, Backstage | Ongoing |