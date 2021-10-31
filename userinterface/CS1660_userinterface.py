print("What microservice would you like to use?\n1. Apache Hadoop\n2. Apache Spark\n3. Jupyter Notebook\n4. SonarQube and SonarScanner\n")
microservice = input("Selection: ")
if (microservice == "1"):
    #do hadoop stuff
    print("Hadoop")
elif (microservice == "2"):
    #do spark stuff
    print("spark")
elif (microservice == "3"):
    #do jupyter notebook stuff
    print("Jupyter Notebook")
elif (microservice == "4"):
    #do SonarStuff
    print("Sonar")

