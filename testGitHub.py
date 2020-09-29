import unittest
import GitHub_API_Keys
class testGitHub(unittest.TestCase):

    #  Noticed when I was running the code that the repository list is alphabetically sorted
    #  As of right now, "Agile_Methods_Project" is consistently the first reposistory
    #  Check to see if the correct repository was gathered
    def testGithubRepos(self):
        names = GitHub_API_Keys.getGithubRepos();
        self.assertEqual(names[0], "Agile_Methods_Project", "First listed repository of RedRoach51 is Agile_Methods_Project (As of 9/29/2020)")

    #  I would much like to make a "dump" repository to consistently check
    #  Having that sort of thing seems very disorganized for my personal GitHub though
    #  I'll just have the code check one of the older repositories that likely aren't getting touched.
    #  Check to see if the correct amount of commits was gathered
    def testGitHubCommits(self):
        name = "SSW-567-HW02"
        user_input = "RedRoach51"
        commit = GitHub_API_Keys.getGithubCommits(name,user_input);
        self.assertEqual(commit, 6, "Recorded amount of commits for RedRoach51/SSW-567-HW02 is 6 (As of 9/29/2020)")

    #  Admittedly, I'd love to have a test for a print function
    #  Unfortunately, a print function "prints" and doesn't return anything
    #  Can't think of an efficient + consistent method of essentially re-testing my entire code
    #  Much rather the "difficult" part of connecting to the APIs get tested instead

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()