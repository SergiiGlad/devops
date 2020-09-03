# Cloud KMS

__Cloud KMS__ is a cloud-hosted key management service that lets you manage cryptographic keys for your cloud services the same way you do on-premises. It includes support for encryption, decryption, signing, and verification using a variety of key types and sources including Cloud HSM for hardware-backed keys.

## Enable Cloud KMS Service

```bash
gcloud services enable cloudkms.googleapis.com \
    --project "${GOOGLE_CLOUD_PROJECT}"
```    

__Key Ring__ is a logical collection of cryptographic keys. The __Key Ring__ contains metadata about the keys such as their location.

## Configure IAM

Cloud KMS is integrated with Google Cloud Identity and Access Management (IAM). Cloud KMS IAM roles are largely divided into two categories:
* Permission to manage keys
* Permission to use keys

For example, the roles/cloudkms.admin role allows the holder to create Key Rings, Crypto Keys, set IAM policies, and perform management-related operations. The roles/cloudkms.cryptoKeyEncrypterDecrypter grants the holder the encrypt and decrypt data, but it does not include management permissions.

IAM roles are inherited by their parent resource. If someone has the roles/cloudkms.admin role on the Google Cloud project, they are an admin of all keys in that project. If they have roles/cloudkms.admin on a Key Ring, they are an admin of all keys in that Key Ring. If they have roles/cloudkms.admin on a single Crypto Key, they are only an admin of that key.



## Encrypt data
<https://cloud.google.com/kms/docs/quickstart#encrypt_data>

Labs
<https://codelabs.developers.google.com/codelabs/encrypt-and-decrypt-data-with-cloud-kms/index.html?index=..%2F..index#0>

```bash
gcloud kms encrypt \
    --location "global" \
    --keyring "mesquite" \
    --key "vpn_password" \
    --plaintext-file ./mysecret.txt \
    --ciphertext-file ./mysecret.txt.encrypted 

cat mysecret.txt.encrypted | base64
```

```    
echo -n ./mysecret.txt | gcloud kms encrypt \
    --location "global" \
    --keyring "mesquite" \
    --key "vpn_password" \
    --plaintext-file - \
    --ciphertext-file - \
    | base64
```    




