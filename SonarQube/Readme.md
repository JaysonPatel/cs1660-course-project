# SonarQube and SonarScanner 
## Overview 
The SonarQube and Sonar Scanner deployment consists of a single image and optional postgres image. Ususally the SonarQube runs with a fixed postgres database but has the option to connect to the users specified database. I chose to have the user connect their own database and only deploy the SonarQube image as I could not see the connection and test things without having a sonar account.

## SonarQube and SonarScanner 
1. I took the image from bitnami/spark and used the `docker pull docker pull sonarqube command` in the cloud shell to pull the image from docker.
2. I then ran `docker tag sonarqube gcr.io/$projectname/sonarqube` to tag this with the path to my gcr images.
3. I then used `docker push gcr.io/$projectname/sonarqube` to make this a usable image for deployment.
4. I navigated to my kubernetes cluster and deployed this image.
5. After deploying the image I used to rescale action to limit the pods to 1.
6. I then exposed ports 9000:9000 and created a service for SonarQube

## Screenshots
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/SonarQube/SonarQube%20Running.png?raw=true "SonarQube Running")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/SonarQube/SonarQube%20Workload.png?raw=true "Workloads")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/SonarQube/Services.png?raw=true "Services")
