# Bucket

Create Bucket
```sh
gsutil mb gs://uniq_buckets_name
```

Accesing public data
```
gsutil ls https://storage.googleapis.com/[BUCKET_NAME]/[OBJECT_NAME]
```

__Bucket naming rules:__

Do not include sensitive information in the bucket name, because the bucket namespace is global and publicly visible.
Bucket names must contain only lowercase letters, numbers, dashes (-), underscores (_), and dots (.). Names containing dots require [verification](https://cloud.google.com/storage/docs/domain-name-verification).
Bucket names must start and end with a number or letter.
Bucket names must contain 3 to 63 characters. Names containing dots can contain up to 222 characters, but each dot-separated component can be no longer than 63 characters.
Bucket names cannot be represented as an IP address in dotted-decimal notation (for example, 192.168.5.4).
Bucket names cannot begin with the "goog" prefix.
Bucket names cannot contain "google" or close misspellings of "google".
Also, for DNS compliance and future compatibility, you should not use underscores (_) or have a period adjacent to another period or dash. For example, ".." or "-." or ".-" are not valid in DNS names.


The Copy URL button provides a shareable URL similar to the following:
https://storage.googleapis.com/YOUR_BUCKET_NAME/kitten.png

gsutil acl ch -u AllUsers:R gs://YOUR-BUCKET-NAME/ada.jpg

gsutil acl ch -d AllUsers gs://YOUR-BUCKET-NAME/ada.jpg ///???? access is right