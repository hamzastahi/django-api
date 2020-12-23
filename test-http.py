from requests import request

url = "http://127.0.0.1:8000/"

params1 = {}
response = request("GET", url+"helloworld", params=params1)
if response.json() == "Hello Stranger!" :
    print("first request passed successfully !")
else :
    print("first request not passed !")

params2 = {"name":"safaa"}
response = request("POST", url+"helloworld", params=params2)
if response.json() == "Hello "+params2.get("name")+"!":
    print("second request passed successfully !")
else :
    print("second request not passed !")

params3 = {}
response = request("GET", url+"versionz", params=params3)
if "Git Hash" in response.json() and "Project Name" in response.json() and response.json().get("Project Name") == "endocode":
    print("third request passed successfully !")
else:
    print("third request not passed !")
