from flask import Flask, redirect, url_for, request
import os
app = Flask(__name__)

formpage = """<!DOCTYPE html>
<html>
    <style>
    .content {
        display: flex;
        align-items: center;
        flex-direction: column;
        width: 250px;
        height: 320px;
        background-color: #457b9d;
        position: absolute;
        top:0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
        border-radius: 10px;
    }
    .centerstyle {
        justify-content: center;
        align-items: center;
        text-align: center;
        color: #ffffff;
        font-family: Arial, Helvetica, sans-serif;
    }
    .button {
        background-color: #fffcf2; /* Green */
        border: none;
        color: black;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        width: 150px;
        margin: 5px;
        border-radius: 5px;
    }
    </style>
	<head>
		<title>CS1660 data toolbox</title>
	</head>
	<body>
	<div class="content">
	    <h2 class="centerstyle">Big Data Toolbox</h2>
		<button onclick=" window.open('http://34.73.196.168:9870','_blank')" class="button"> Hadoop</button>
		<button onclick=" window.open('http://34.74.213.16:8080','_blank')" class="button"> Spark</button>
		<button onclick=" window.open('http://104.196.154.26:8888','_blank')" class="button"> Jupyter</button>
		<button onclick=" window.open('http://35.231.243.96:9000','_blank')" class="button"> Sonar</button>
	</div>
	</body>
</html>
"""

@app.route("/", methods=['GET', 'POST'])
def form():
    return formpage

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=os.getenv('PORT'))