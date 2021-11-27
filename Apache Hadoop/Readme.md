# Hadoop
## Overview 
The Hadoop deployment consists of a name node that is connected to two data nodes. The name node has an open port on 9870 that allows you to access the web service to view activity and monitor data nodes. It also has an open port of 9000 for hdfs requests.

## Name Node
1. I took the image from bde2020/hadoop-namenode and used the `docker pull bde2020/hadoop-namenode command` in the cloud shell to pull the image from docker.
2. I then ran `docker tag bde2020/hadoop-namenode gcr.io/$projectname/namenode` to tag this with the path to my gcr images.
3. I then used `docker push gcr.io/$projectname/namenode` to make this a usable image for deployment.
4. I navigated to my kubernetes cluster and deployed this image using the ENVIRONMENT VARIABLES from the docker compose and .env file on the BDE git.
5. After deploying the image I used to rescale action to limit the pods to 1.
6. I then exposed ports 9000:9000 and 9078:9078 and created a service for the namenode 


## Data Node
1. I took the image from bde2020/hadoop-datanode and used the `docker pull bde2020/hadoop-datanode command` in the cloud shell to pull the image from docker.
2. I then ran `docker tag bde2020/hadoop-datanode gcr.io/$projectname/datanode` to tag this with the path to my gcr images.
3. I then used `docker push gcr.io/$projectname/datanode` to make this a usable image for deployment.
4. I navigated to my kubernetes cluster and deployed this image using the ENVIRONMENT VARIABLES from the docker compose and .env file on the BDE git.
5. I needed to change one of the ENVIRONMENT VARIABLES to the location of the namenode which was specified by the ip and port in the service that I had created.
6. After deploying the image I used to rescale action to limit the pods to 2.

## Screenshots
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Apache%20Hadoop/Hadoop%20Running.png?raw=true "Hadoop Running")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Apache%20Hadoop/Hadoop%20Workload.png?raw=true "Workloads")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Apache%20Hadoop/Services.png?raw=true "Services")
