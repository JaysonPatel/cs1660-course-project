# Jupyter Notebooks
## Overview 
Jupyter Notebooks only consists of a single image. The image hosts a jupyter notebooks data science library on port 8888.

## Jupyter Notebooks Workload
1. I took the image from jupyter/datascience-notebook and used the `docker pull jupyter/datascience-notebook command` in the cloud shell to pull the image from docker.
2. I then ran `docker tag bde2020/hadoop-namenode gcr.io/$projectname/jupyter/datascience-notebook` to tag this with the path to my gcr images.
3. I then used `docker push gcr.io/$projectname/jupyter/datascience-notebook` to make this a usable image for deployment.
5. After deploying the image I used to rescale action to limit the pods to 1.
6. I then exposed ports 8888:8888 and created a service for the jupyter notebook 

## Screenshots
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Jupyter%20Notebooks/Jupyter%20Running.png?raw=true "Jupyter Running")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Jupyter%20Notebooks/Jupyter%20Workload.png?raw=true "Workloads")
![Alt text](https://github.com/JaysonPatel/cs1660-course-project/blob/main/Jupyter%20Notebooks/Services.png?raw=true "Services")
