# Troubleshooting Workloads on GKE for Site Reliability Engineers

https://partner.cloudskillsboost.google/focuses/20684?parent=catalog#step1

Your organization has deployed a multi-tier microservices application. It is a web-based e-commerce application called "Hipster Shop", where users can browse for vintage items, add them to their cart and purchase them. Hipster Shop is composed of many microservices, written in different languages, that communicate via gRPC and REST APIs. The architecture of the deployment is optimized for learning purposes and includes modern technologies as part of the stack: Kubernetes, Istio, Cloud Operations, App Engine, gRPC, OpenTelemetry, and similar cloud-native technologies.

As a member of the Site Reliability Engineering (SRE) team, you are contacted when end users report issues viewing products and adding them to their cart. You will explore the various services deployed to determine the root cause of the issue and set up a Service Level Objective (SLO) to prevent similar incidents from occurring in the future. Learn more about this in the following blog article: SLOs, SLIs, SLAs, oh my—CRE life lessons.

Task 2. Accessing operational data through GKE Dashboards
In this section of the lab, you explored the available logs and metrics in the GKE dashboard to diagnose an issue with the application workload deployed by the DevOps team. You were able to pinpoint the exact cause of an issue and remediate it by re-deploying the problematic microservice with a bug fix.