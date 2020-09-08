# Secure Compute Mode

## Seccomp in Kubernetes

Your seccomp profiles defines what system calls should be allowed or blocked, and the container runtime will apply then at container start time so the kernel can enforce it. 