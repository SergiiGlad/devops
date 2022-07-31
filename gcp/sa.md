create a service account

```
export SA_NAME="natural-language-api"
gcloud iam service-accounts create $SA_NAME --display-name $SA_NAME
```


create a credential key file

```
export PROJECT_ID=$(gcloud config get-value core/project)
gcloud iam service-accounts keys create key.json \
--iam-account  $SA_NAME@$PROJECT_ID.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/key.json"
```

Invoke the analyzeSentiment request:

```
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @request_analyze_sentiment.json \
https://language.googleapis.com/v1/documents:analyzeSentiment
```