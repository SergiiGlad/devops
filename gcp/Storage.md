## Google Cloud Platform 

GCP has other storage options to meet your needs for 
* structured 
* unstructured 
* transactional 
* relational data. 

Cloud option:

* Cloud Storage
* Cloud SQL
* Cloud Spanner
* Cloud Data Store
* CLoud Big Table

__Cloud Storage__:
* bunch of bytes
* fully managed scalable service
* Cloud Storage is not a file system because each of your objects in Cloud Storage has a URL
* The storage objects are immutable, which means that you do not edit them in place but instead you create new versions

_Cloud Storage Classes_
* Multi-regional - most frequently accessed - 99.95%
* Regional 99.9% - accessed frequently within a region - 99.9%
* Nearline - Accessed less than once a month  - 99%
* Coldline - Accessed less than once a year - 99% 

__Cloud Datastore__

Cloud Datastore actually stores structured objects

__Cloud Bigtable__

* Data can also be streamed in through a variety of popular stream processing frameworks, like Cloud Dataflow Streaming, Spark Streaming and Storm. 
* If streaming is not an option, data can also be read from and written to Cloud Bigtable through batch processes like Hadoop map reduce, Dataflow or Spark.

__Cloud SQL__ is a managed RDBMS

* Cloud SQL provides several replica services like read, failover, and external replicas
* helps you backup your data with either on-demand or scheduled backups 
* It can also scale both vertically by changing the machine type, and horizontally via read replicas

__Cloud Spanner__

* It offers transactional consistency at a global scale, schemas, SQL, and automatic synchronous replication for high availability