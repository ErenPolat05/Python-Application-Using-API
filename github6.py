import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

        self.token = "Your Github Access Token"

    def GetUser(self,username):
        response = requests.get(self.api_url+"/users/"+username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()
    
    def createRepostory(self,name):
        response = requests.post(self.api_url+"/users/repos?access_token="+self.token,json= {
            "name": name,
            "description": "This is your first repository",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
        return response.json()


github = Github()

while True:
    choose = input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nChoose: ")

    if choose == "4":
        break
    else:
        if choose == "1":
            username = input("Username: ")
            result = github.GetUser(username)
            print(f"name: {result['name']},public repos:{result['public_repos']},followers: {result['followers']}")




        elif choose == "2":
            username = input("Username: ")
            result = github.getRepositories(username)
            for repo in result:
             print(repo["name"])

        elif choose == "3":
            name = input("Name: ")
            result = github.createRepostory(name)
            print(result)

        else:
            print("Wrong Type, Please Try Again.")