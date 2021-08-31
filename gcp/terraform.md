https://cloud.google.com/architecture/managing-infrastructure-as-code

```bash
PROJECT_ID=$(gcloud config get-value project)
gsutil mb gs://${PROJECT_ID}-tfstate

gsutil versioning set on gs://${PROJECT_ID}-tfstate

gcloud auth application-default loginecho 

export GOOGLE_APPLICATION_CREDENTIALS="/Users/sgladc/.config/gcloud/application_default_credentials.json"
```