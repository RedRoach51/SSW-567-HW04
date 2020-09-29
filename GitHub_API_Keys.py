import requests;
import json;



#print(data);
#print(data[0])
#for entry in data:
#    print (entry.key);


def getGithubRepos(user = "redroach51"):
    repos = requests.get("https://api.github.com/users/" + user + "/repos");
    repos.raise_for_status();
    data = repos.json()
    x = 0;
    repos = [];
    for entry in data:
        for key,value in entry.items():
            if (key == "name"):
                repos.append(value)
    return repos;

def getGithubCommits(repos, user):
    print(user + "'s number of repositories: " + str(len(repos)));
    x = 0;
    count = 0;
    for entry in repos:
        x = x + 1
        commits = requests.get("https://api.github.com/repos/RedRoach51/" + entry + "/commits")
        commits = commits.json();
        count = count + len(commits);
        print (str(x) + ".) " + entry + ", Commits: " + str(len(commits)));
    print("Total commits: " + str(count))

user_input = input("Input GitHub user: ")
if (user_input == ""):
    print("Default user set to creator RedRoach51.")
    user_input = "RedRoach51";
repositories = getGithub(user_input)
getGithubCommits(repositories, user_input);


