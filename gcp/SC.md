
## GCP Source Codessh

#### GCP SDK
```
gcloud source repos clone mesquite --project=turing-archway-254318
```

#### Authenticate by using SSH

Generate a key pair
```
ssh-keygen -t rsa -C email@domain
```

Register a public key

https://source.cloud.google.com/user/ssh_keys?register=true


Work
```
git clone ssh://sgladc@softserveinc.com@source.developers.google.com:2022/p/mesquiteisd-poc/r/misd-gcp-poc-automation
```

Enable security key detection

```
 gcloud source project-configs update --enable-pushblock
```

https://cloud.google.com/docs/ci-cd