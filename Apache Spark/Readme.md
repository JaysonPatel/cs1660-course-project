# Spark
## Overview 
The Spark deployment consists of a master node that is connected to two worker nodes. The master node has an open port on 8080 that allows you to access the web service to view activity and monitor worker nodes.

## Spark Master
1. I took the image from bitnami/spark and used the `docker pull bitnami/spark command` in the cloud shell to pull the image from docker.
2. I then ran `docker tag bitnami/spark gcr.io/$projectname/bitnami/spark` to tag this with the path to my gcr images.
3. I then used `docker push gcr.io/$projectname/bitnami/spark` to make this a usable image for deployment.
4. I navigated to my kubernetes cluster and deployed this image using the ENVIRONMENT VARIABLES from the docker compose file on the bitnami git.
5. The main ENVIRONMENT VARIABLE to change is SPARK_MODE=master 
6. After deploying the image I used to rescale action to limit the pods to 1.
7. I then exposed ports 8080:8080 and created a service for the spark master 


## Spark Worker
1. The same image is used for the worker and the only change is SPARK_MODE=worker in the ENVIRONMENTAL VARIABLES
2. I also needed to change the location of the master in a similar way to Hadoop and I did this by looking at the ip of the service that I had created
3. After deploying the image I used to rescale action to limit the pods to 2.

## Screenshots
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Apache%20Spark/Spark%20Running.png?raw=true "Spark Running")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Apache%20Spark/Spark%20Workload.png?raw=true "Workloads")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Apache%20Spark/Services.png?raw=true "Services")
