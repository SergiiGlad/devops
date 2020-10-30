
```
gcloud sql instances patch cloudsql001 --authorized-networks=$(dig +short myip.opendns.com @resolver1.opendns.com)
```

## Google Cloud SQL Proxy

__Google Cloud SQL Proxy__ provides secure access to Cloud SQL Second Generation instances without having to whitelist IP addresses or configure SSL. __Cloud SQL Proxy__ provides several important benefits:

 * __Secure connections:__ The proxy automatically encrypts traffic to and from the database using TLS 1.2 with a 128-bit AES cipher; SSL certificates are used to verify client and server identities.
 * __Easier connection management:__ The proxy handles authentication with Cloud SQL, removing the need to provide static IP addresses.
The proxy does not provide a new connectivity path; it relies on existing IP connectivity. For example, you cannot use the proxy to connect with an instance using Private IP unless the proxy is using a VPC network that has been configured for private services access.