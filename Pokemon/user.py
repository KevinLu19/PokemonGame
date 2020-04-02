# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 11/5/2019
# File: user.py
# Purpose: File for user functions such as handling scores and guessing answers.
# Modification: - Added basic member function of a user class.
# ----------------------------------------------------------------------------------------

class User:

    def __init__(self):
        self.userScore = 0
    
    def getScore (self):
        return self.score

    def setAnswer (self, answer):
        self.userAnswer = answer
    
    def getAnswer (self):
        return self.userAnswer
    
    def incrementScore (self):
        self.userScore = self.userScore + 1

        return self.userScore