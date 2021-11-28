# Graphical User Interface
I created a GUI using flask which consists of 4 buttons that navigate you to the endpoints of each of the 4 services. I made a docker image from scratch for this for the extra credit.

## Making the GUI
1. I started by making the basic flask application in python and adding a header and 4 buttons that navigate to the endpoints when clicked. There was not much backend needed at all for this.
2. I then made a dockerfile to make and image of this to deloy to gcp and saved it as jrp134/cs1660-gui 
3. I took the image from jrp134/cs660-gui and used the `docker pull jrp134/cs660-gui command` in the cloud shell to pull the image from docker.
4. I then ran `docker tag jrp134/cs660-gui gcr.io/$projectname/jrp134/cs660-gui` to tag this with the path to my gcr images.
5. I then used `docker push gcr.io/$projectname/jrp134/cs660-gui` to make this a usable image for deployment.
6. I navigated to my kubernetes cluster and deployed this image using the ENVIRONMENT VARIABLES from the docker compose
7. After deploying the image I used to rescale action to limit the pods to 1.
8. I then exposed ports 5000:5000 and created a service for the web application. 
