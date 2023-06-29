#!/usr/bin/env python
# coding: utf-8

from datetime import date
import Periodicity

# Habit class
class Habit:
      
    '''The constructor for the Habit class takes id, name, description, creationDate, periodicity, lastFinishing, lastStreak,
    bestStreak and active arguments and assigns these to the Habits attributes.'''    
    def __init__(self, id, name, description, creationDate, periodicity, lastFinishing, lastStreak, bestStreak, active):
        self.habitID = id
        self.habitName = name
        self.habitDescription = description
        self.creationDate = creationDate
        self.periodicity = periodicity
        self.lastFinishing = lastFinishing
        self.lastStreak = lastStreak
        self.bestStreak = bestStreak
        self.habitActive = active
        
    '''The setDatabaseValues function takes id, name, description, periodicity, lastFinishing, lastStreal, bestStreak
    and active arguments for updating database function and assigns these to the given habits attributes.'''    
    def setDatabaseValues(self, id, name, description, periodicity, lastFinishing, lastStreak, bestStreak, active):
        self.habitID = id
        self.habitName = name
        self.habitDescription = description
        self.periodicity = periodicity
        self.lastFinishing = lastFinishing
        self.lastStreak = lastStreak
        self.bestStreak = bestStreak
        self.habitActive = active
        
    '''The getLastFinished function returns the value of lastFinishing.'''
    def getLastFinished(self):
        return self.lastFinishing
     
    '''The getPeriodicity function returns the value of periodicity.'''   
    def getPeriodicity(self):
        return str(self.periodicity)
    
    '''The getLastStreak function returns the value of lastStreak.'''
    def getLastStreak(self):
        return self.lastStreak
    
    '''The getBestStreak function returns the value of bestStreak.'''
    def getBestStreak(self):
        return self.bestStreak
    
    '''The getActiveState function returns the value of habitActive.'''
    def getActiveState(self):
        return self.habitActive
    
    '''The string representation function returns the attributes of the habit.'''
    def __str__(self):
        return """ID: {0}\nName: {1}\nDescription: {2}\nCreation date: {3}\nPeriodicity: {4}\nLast completed: {5}\nLast streak: {6}\nBest streak: {7}\nActive state: {8}""".format(self.habitID, self.habitName, self.habitDescription, self.creationDate, self.periodicity, self.lastFinishing,
               self.lastStreak, self.bestStreak, self.habitActive)
    




