import requests;
import json;

def getGithubRepos(user = "redroach51"):
    repos = requests.get("https://api.github.com/users/" + user + "/repos");
    repos.raise_for_status();
    data = repos.json()
    print (data)
    x = 0;
    repos = [];
    for entry in data:
        for key,value in entry.items():
            if (key == "name"):
                repos.append(value)
    return repos;

def getGithubCommits(repo = "SSW-567-HW04", user = "redroach51"):
    commits = requests.get("https://api.github.com/repos/"+ user + "/" + repo + "/commits")
    commits = commits.json();
    return len(commits);

def main():
    user_input = input("Input GitHub user: ")
    if (user_input == ""):
        print("Default user set to creator RedRoach51.")
        user_input = "RedRoach51";
    repositories = getGithubRepos(user_input)

    i = 1;
    count = 0;

    print(user_input + "'s number of repositories: " + str(len(repositories)));
    for repo_name in repositories:
        commits = getGithubCommits(repo_name, user_input);
        count = count + commits;
        print(str(i) + ".) " + repo_name + ", Commits: " + str(commits));

if __name__ == '__main__':
    main()