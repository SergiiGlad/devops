https://partner.cloudskillsboost.google/catalog_lab/572

### Set zone 
```gcloud config set compute/zone us-central1-a ```

### Get sample code for this lab
```gsutil -m cp -r gs://spls/gsp053/orchestrate-with-kubernetes . cd orchestrate-with-kubernetes/kubernetes```

### Create a cluster with five n1-standard-1 nodes (this will take a few minutes to complete):
```gcloud container clusters create bootcamp --num-nodes 5 --scopes "https://www.googleapis.com/auth/projecthosting,storage-rw"```

### Learn about the deployment object
```
kubectl explain deployment
kubectl explain deployment --recursive
kubectl explain deployment.metadata.name
```

You can also use the output templating feature of kubectl to use curl as a one-liner:

```curl -ks https://`kubectl get svc frontend -o=jsonpath="{.status.loadBalancer.ingress[0].ip}"```

### Scale a Deployment
```kubectl scale deployment hello --replicas=5```


# Rolling update
Deployments support updating images to a new version through a rolling update mechanism. When a Deployment is updated with a new version, it creates a new ReplicaSet and slowly increases the number of replicas in the new ReplicaSet as it decreases the replicas in the old ReplicaSet.

![alt text](rolling.png)

Trigger a rolling update
```kubectl edit deployment hello```
...
containers:
  image: kelseyhightower/hello:2.0.0
...

### Pause a rolling update
If you detect problems with a running rollout, pause it to stop the update. Give that a try now:

```kubectl rollout pause deployment/hello```

```kubectl rollout status deployment/hello```

```kubectl get pods -o jsonpath --template='{range .items[*]}{.metadata.name}{"\t"}{"\t"}{.spec.containers[0].image}{"\n"}{end}'```

### Resume a rolling update
The rollout is paused which means that some pods are at the new version and some pods are at the older version. We can continue the rollout using the resume command.

```kubectl rollout resume deployment/hello```

```kubectl rollout status deployment/hello```

### Rollback an update
Assume that a bug was detected in your new version. Since the new version is presumed to have problems, any users connected to the new Pods will experience those issues.

You will want to roll back to the previous version so you can investigate and then release a version that is fixed properly.

Use the rollout command to roll back to the previous version:
```
kubectl rollout undo deployment/hello
kubectl rollout history deployment/hello
kubectl get pods -o jsonpath --template='{range .items[*]}{.metadata.name}{"\t"}{"\t"}{.spec.containers[0].image}{"\n"}{end}'
```

# Canary deployments

When you want to test a new deployment in production with a subset of your users, use a canary deployment. Canary deployments allow you to release a change to a small subset of your users to mitigate risk associated with new releases.

Create a canary deployment
A canary deployment consists of a separate deployment with your new version and a service that targets both your normal, stable deployment as well as your canary deployment.

![alt text](canary.png)

### Canary deployments in production - session affinity

In this lab, each request sent to the Nginx service had a chance to be served by the canary deployment. But what if you wanted to ensure that a user didn't get served by the Canary deployment? A use case could be that the UI for an application changed, and you don't want to confuse the user. In a case like this, you want the user to "stick" to one deployment or the other.

You can do this by creating a service with session affinity. This way the same user will always be served from the same version. In the example below the service is the same as before, but a new sessionAffinity field has been added, and set to ClientIP. All clients with the same IP address will have their requests sent to the same version of the hello application.

# Blue-green deployments
Rolling updates are ideal because they allow you to deploy an application slowly with minimal overhead, minimal performance impact, and minimal downtime. There are instances where it is beneficial to modify the load balancers to point to that new version only after it has been fully deployed. In this case, blue-green deployments are the way to go.

Kubernetes achieves this by creating two separate deployments; one for the old "blue" version and one for the new "green" version. Use your existing hello deployment for the "blue" version. The deployments will be accessed via a Service which will act as the router. Once the new "green" version is up and running, you'll switch over to using that version by updating the Service.

![alt text](bluegreen.png)

__A major downside of blue-green deployments is that you will need to have at least 2x the resources in your cluster necessary to host your application. Make sure you have enough resources in your cluster before deploying both versions of the application at once.__

