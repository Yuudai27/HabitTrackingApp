#!/usr/bin/env python
# coding: utf-8

import pytest
import sys
from Periodicity import Periodicity
from datetime import date
import HabitTrackingApp
from HabitTrackingApp import completeTask, updateDatabase, searchOverallBestStreak, searchActiveHabits, searchIDBestStreak, showHabit, insertDatabase, deleteDatabase, searchSamePeriodicities

'''The ID- class provides an object with an id- attribute, to
be able to call functions from the HabitTrackingApp and also being
able to user argparse.'''
class ID: 
    def __init__(self, id):
        self.id = id

'''The Active- class provides an object with an active- attribute, to
be able to call functions from the HabitTrackingApp and also being
able to user argparse.'''
class Active: 
    def __init__(self, active):
        self.active = active
 
'''The Create- class provides an object with name, desc and per- attributes, 
to be able to call functions from the HabitTrackingApp and also being
able to user argparse.'''
class Create: 
    def __init__(self, name, desc, per):
        self.name = name
        self.desc = desc
        self.per = per

'''The Update- class provides an object with id, name, desc, per and active- 
attributes, to be able to call functions from the HabitTrackingApp and also being
able to user argparse.'''
class Update: 
    def __init__(self, id, name, desc, per, active):
        self.id = id
        self.name = name
        self.desc = desc
        self.per = per
        self.active = active

'''The Perio- class provides an object with an per- attribute, to
be able to call functions from the HabitTrackingApp and also being
able to user argparse.'''
class Perio: 
    def __init__(self, per):
        self.per = per

'''The test_insertDatabase- function tests the insertDatabase- function from the 
HabitTrackingApp. A habit with predefined values will be created in the
database. To check the result, the habitArray will searched through for 
the newly created habit and its values compared to predefined ones.'''        
def test_insertDatabase():
    name = "Climbing"
    desc = "Rock it!"
    per = Periodicity.WEEKLY.value
    
        
    testData = Create(name, desc, per)
    
    insertDatabase(testData)
    for x in HabitTrackingApp.habitArray:
        if x.habitName == name:
            assert x.habitDescription == desc
            assert x.getPeriodicity() == per
            assert x.creationDate == date.today()

'''The test_updateDatabase- function tests the updateDatabase- function from the 
HabitTrackingApp. A habit with predefined values will be updated in the
database. To check the result, the habitArray will searched through for 
the currently updated habit and its values compared to predefined ones.'''               
def test_updateDatabase():
    id = 2
    name = "kitchen"
    desc = "cook in it"
    per = Periodicity.DAILY.value
    active = True
    
        
    testData = Update(id, name, desc, per, active)
    
    updateDatabase(testData)
    for x in HabitTrackingApp.habitArray:
        if x.habitID == id:
            assert x.habitName == name and x.habitDescription == desc and x.getPeriodicity() == per and x.getActiveState() == active
            
'''The test_deleteDatabase- function tests the deleteDatabase- function from the 
HabitTrackingApp. A habit with a predefined id will be deleted from the
database. To check the result, the habitArray will searched through for 
the deleted habit and as long as the counter stays 0 the test passes.''' 
def test_deleteDatabase():
    idValue = ID(6)
    deleteDatabase(idValue)
    
    counter = 0
    for x in HabitTrackingApp.habitArray:
        if x.habitID == 6:
            counter = counter + 1
    assert counter == 0
    
'''The test_searchIDBestStreak- function tests the searchIDBestStreak- function from the 
HabitTrackingApp. A habit with a predefined id will be searched in the habitArray
and the bestStreak- value derived. 
The result will be compared to the invoked searchIDBestStreak- function.'''                     
def test_searchIDBestStreak():
    idValue = ID(1)
    bestStreak = 0
    
    for x in HabitTrackingApp.habitArray:
        if x.habitID == idValue.id:
            bestStreak = x.getBestStreak()
    
    assert searchIDBestStreak(idValue) == bestStreak

'''The test_completeTask- function tests the completeTask- function from the 
HabitTrackingApp. A habit with a predefined id will be completed in the database. 
The getLastFinished- date will be compared to the today- value at the point calling
the function.'''     
def test_completeTask():
    idValue = ID("1")
    completeTask(idValue)
    for x in HabitTrackingApp.habitArray:
        if x.habitID == 1:
            assert x.getLastFinished() == date.today()

'''The test_searchActiveHabits- function tests the searchActiveHabits- function from the 
HabitTrackingApp. The activeBool variable is just to call the function with an argument,
that it still works with argparse.
An activeCounter counts the active habits in the habitArray.
The result will be compared to the length of the result array of the invoked 
searchActiveHabits- function.'''             
def test_searchActiveHabits():
    activeBool = Active(True)
    activeCounter = 0
    for x in HabitTrackingApp.habitArray:
        if x.getActiveState() == True:
            activeCounter = activeCounter + 1
            
    assert len(searchActiveHabits(activeBool)) == activeCounter

'''The test_searchOverallBestStreak- function tests the searchOverallBestStreak- function from the 
HabitTrackingApp. The activeBool variable is just to call the function with an argument,
that it still works with argparse.
The bestStreak and bestStreakID will hold the results for the ID and the value of the habit with
the highest best streak in the habitArray.
The resulting ID will be compared to the ID of the invoked searchOverallBestStreak- function.'''    
def test_searchOverallBestStreak():
    activeBool = Active(True)
    bestStreak = 0
    bestStreakID = 0
    
    for x in HabitTrackingApp.habitArray:
        if x.getBestStreak() >= bestStreak:
            bestStreak = x.getBestStreak()
            bestStreakID = x.habitID
    
    assert searchOverallBestStreak(activeBool) == bestStreakID

'''The test_searchSamePeriodicities- function tests the searchSamePeriodicities- function from the 
HabitTrackingApp. The perValue variable provides the periodicity value to invoke and compare the 
function later.
The habitArray will be searched for the given periodicity and counts it with the perCounter.
The resulting counter will be compared to the length of the result array of the invoked 
searchSamePeriodicities- function.'''      
def test_searchSamePeriodicities():
    perValue = Perio(Periodicity.DAILY.value)
    perCounter = 0
    for x in HabitTrackingApp.habitArray:
        print(x.getPeriodicity)
        if x.getPeriodicity() == perValue.per:
            perCounter = perCounter + 1       
    assert len(searchSamePeriodicities(perValue)) == perCounter
    
#test_insertDatabase()
#test_updateDatabase()    
#test_deleteDatabase()    
#test_searchIDBestStreak()    
#test_completeTask()
#test_searchActiveHabits()
#test_searchOverallBestStreak()
#test_searchSamePeriodicities()



