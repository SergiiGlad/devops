# Set the Project ID in environmental variable

```
$ export GOOGLE_CLOUD_PROJECT=`gcloud config list \
  --format 'value(core.project)'`

```