# Kubernetes: Deep Dive

Softserve course

Teacher: Eldar Aliiev

Session 1

https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/

https://kubernetes.io/docs/reference/setup-tools/kubeadm/https://kubernetes.io/docs/concepts/cluster-administration/addons/

https://github.com/kubernetes-sigs/kubespray

https://github.com/kubernetes/kops

https://kops.sigs.k8s.io/getting_started/install/

https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc

https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-tech-category=*all&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all&awsf.whitepapers-global-methodology=*all

https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html

Creating a cluster with kubeadm
Using kubeadm, you can create a minimum viable Kubernetes cluster that conforms to best practices. In fact, you can use kubeadm to set up a cluster that will pass the Kubernetes Conformance tests. ...

Session 2 25/10/2022

# API OVERVIEW

https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/

Open API standard https://swagger.io/

Controller = Kubernetes Operator

https://kubernetes.io/docs/concepts/extend-kubernetes/operator/

https://developer.ibm.com/articles/kubernetes-operators-patterns-and-best-practices/?utm_medium=Email&utm_source=Newsletter&utm_content=DEVWW&utm_term=10013593&utm_id=n05&spMailingID=47371808&spUserID=NzMwNjQ3NDUzODY3S0&spJobID=2321613592&spReportId=MjMyMTYxMzU5MgS2


```sh
kubectl api-resources
```

https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/

https://swagger.io/specification/

https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/

https://kubernetes.io/docs/concepts/extend-kubernetes/operator/


h/w
1. v1
2. v1beta1

1. with namespace
2. clusterscope

1. Only one version v1 or v1beta have been able to serve
2. I created custom object. Then I run any command (like logs, exec) I got "you must specify at least one command for the container"
3. Lens shows CRD



# Kubernetes Operators

https://go.dev/doc/install  
https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/  
https://book-v1.book.kubebuilder.io/beyond_basics/generating_crd.html  
https://github.com/operator-framework/operator-sdk/blob/latest/testdata/go/v3/memcached-operator/controllers/memcached_controller.go  
https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/  

https://olm.operatorframework.io/docs/  
https://youtu.be/nJ-GVWyMEsw?t=18802  



