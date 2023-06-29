#!/usr/bin/env python
# coding: utf-8

import Habit
from Periodicity import Periodicity
from datetime import date, timedelta
from argparse import ArgumentParser
import mysql.connector
#habitArray is an Array, which will hold all habit- instances, while the program is running.
habitArray = []

'''The mysql.connector module gets implemented to create an interface between python and 
the mysql- database. The connection will be assigned with the login data to the sql-server'''
cnx = mysql.connector.connect(user='****', password='****',
                             host='localhost', database='habittrackingapp')
cursor = cnx.cursor(buffered=True)

'''In this part the argparse- modul will be set initialized and the functions step by step
later after defining these.'''
cli = ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")

'''The insertDatabase function provides the function to insert a new habit into the mysql database.
The habitData- argument contains different values as name, desc(description) and per(periodicity) for 
the new habit. The string-value for per will be checked and a fitting Periodicity- value will be
applied.
The data will be inserted in a data-query as insert-statement for the mysql-server.
After creating the new habit, the habitArray will be cleared and loaded with current data from
the database.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.'''
def insertDatabase(habitData):
    if habitData.per == "DAILY":
        periodicityValue = Periodicity.DAILY.value
    else:
        periodicityValue = Periodicity.WEEKLY.value
    
    query1= ('''INSERT INTO habits(habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active)
    VALUES (\''''+habitData.name+'''\', \''''+habitData.desc+'''\', \''''+str(date.today())+'''\',\''''+periodicityValue+'''\', \''''+str(date.today())+'''\',0,0,true)''')
    cursor.execute(query1)
    cnx.commit()
    habitArray.clear()
    loadDatabase()
    
parser_insertDatabase = subparsers.add_parser('insertDatabase', help='Creates new habit with given details!')
parser_insertDatabase.add_argument('-name', help='Name of habit is to provide!')
parser_insertDatabase.add_argument('-desc', help='Description of habit is to provide!')
parser_insertDatabase.add_argument('-per', help='Periodicity of habit is to provide!')
parser_insertDatabase.set_defaults(func= insertDatabase)        

'''The loadDatabase function loads the current data from the mysql database into the habitArray.
After requesting the data from the sql server, the data gets appended to the habitArray as 
Habit- instances.'''
def loadDatabase():
    query2 = ('''SELECT * FROM habits''')
    cursor.execute(query2)
    
    for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:  
        if periodicity == 'daily':
            periodicityValue = Periodicity.DAILY.value
        else:
            periodicityValue = Periodicity.WEEKLY.value    
        habitArray.append(Habit.Habit(habit_ID, habit_name, habit_description, creation_date, periodicityValue, last_finishing, last_streak, best_streak, habit_active))

'''The updateDatabase function provides the function to update a habit in the mysql database.
The habitData- argument contains different values as id, name, desc(description), per(periodicity) and 
active(active status) for the habit. 
After updating the data in the database, the data for the habit gets requested from the database and
the setDatabaseValues- function of the Habit- instance will be used, that the whole habitArray doesn't
have to be renewed.
The data will be inserted in a data-query as insert-statement for the mysql-server.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.'''        
def updateDatabase(habitData):
    query3 = ('''UPDATE habits SET habit_name = \''''+habitData.name+'''\', habit_description = \''''+habitData.desc+'''\', periodicity = \''''+habitData.per+'''\', habit_active = '''+str(habitData.active)+''' WHERE habit_ID = '''+str(habitData.id))
    cursor.execute(query3)
    cnx.commit()
    
    query2 = ('''SELECT * FROM habits WHERE habit_ID = '''+str(habitData.id))
    cursor.execute(query2)
    
    for x in habitArray:
        if x.habitID == int(habitData.id):
            for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:
                if habitData.per == 'DAILY':
                    periodicityValue = Periodicity.DAILY.value
                else:
                    periodicityValue = Periodicity.WEEKLY.value
                x.setDatabaseValues(habit_ID, habit_name, habit_description, periodicityValue, last_finishing, last_streak, best_streak, habit_active)
                
parser_updateDatabase = subparsers.add_parser('updateDatabase', help='Updates habits with given details.')
parser_updateDatabase.add_argument('-id', help='ID of habit is to provide!')
parser_updateDatabase.add_argument('-name', help='Name of habit is to provide!')
parser_updateDatabase.add_argument('-desc', help='Description of habit is to provide!')
parser_updateDatabase.add_argument('-per', help='Periodicity of habit is to provide!')
parser_updateDatabase.add_argument('-active', help='Active status of habit is to provide!')
parser_updateDatabase.set_defaults(func= updateDatabase)    

'''The deleteDatabase function provides the function to delete a habit from the mysql database.
The habitID- argument contains the value id of the habit to delete. 
After deleting the data in the database, the habitArray will be cleared and loaded with current data from
the database.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.'''      
def deleteDatabase(habitID):
    query4 = ('''DELETE FROM habits WHERE habit_ID = '''+str(habitID.id))
    cursor.execute(query4)
    cnx.commit()
    habitArray.clear()
    loadDatabase()
    
parser_deleteDatabase = subparsers.add_parser('deleteDatabase', help='Delete habit for given ID in database!')
parser_deleteDatabase.add_argument('-id', help='ID of habit is to provide!')
parser_deleteDatabase.set_defaults(func= deleteDatabase)
    
'''The searchOverallBestStreak function provides the function to search through the habitArray, comparing the
best streaks and holding the bestStreak- value and the related ID.
The active- argument contains a boolean, which just exists to be able to run the function
with argparse and pytest as well. 
After the habitArray got searched through, the result will be printed in the console.
The functions returns the ID of the habit with the bestStreak, that pytest can compare it later.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.'''         
def searchOverallBestStreak(active):
    bestStreak = 0
    bestStreakID = 0
    
    for x in habitArray:
        if x.getBestStreak() >= bestStreak:
            bestStreak = x.getBestStreak()
            bestStreakID = x.habitID
        
    for y in habitArray:
        if y.habitID == bestStreakID:
            print("The habit {0} with the ID {1} has the best streak of {2}!".format(y.habitName, y.habitID, y.getBestStreak()))
            return (y.habitID)    

parser_searchOverallBestStreak = subparsers.add_parser('searchOverallBestStreak', help='Search for habit with the best streak!')
parser_searchOverallBestStreak.add_argument('-active', type=bool, help='Set to True')
parser_searchOverallBestStreak.set_defaults(func= searchOverallBestStreak)  

'''The searchActiveHabits function provides the function to search through the habitArray for habits,
which are currently active.
The active- argument contains a boolean, which just exists to be able to run the function
with argparse and pytest as well. 
While the habitArray get searched through, the result will be iterativley printed in the console.
The functions returns the an activeArray, which gets appended step by step, that pytest can compare it later.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.'''    
def searchActiveHabits(activeState):
    activeArray = []
    for x in habitArray:
        if x.getActiveState() == True:
            print(x)
            activeArray.append(x.habitID)
    return (activeArray)

parser_searchActiveHabits = subparsers.add_parser('searchActiveHabits', help='Search for active habits!')
parser_searchActiveHabits.add_argument('-active', type=bool, help='Set to True')
parser_searchActiveHabits.set_defaults(func= searchActiveHabits)  

'''The searchIDBestStreak function provides the function to search through the habitArray for the 
bestStreak of the given habit ID.
The id- argument contains an id, which provides the habit to search for. 
When the related habit is found in the habitArray, the result will be printed with the bestStreak.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.'''  
def searchIDBestStreak(id):
    for x in habitArray:
        if x.habitID == int(id.id):
            print("The habit {0} with the ID {1} has the best streak of {2}!".format(x.habitName, x.habitID, x.getBestStreak()))
            return (x.getBestStreak())
            
parser_searchIDBestStreak = subparsers.add_parser('searchIDBestStreak', help='Search the best streak for an ID!')
parser_searchIDBestStreak.add_argument('-id', help='ID of habit is to provide!')
parser_searchIDBestStreak.set_defaults(func= searchIDBestStreak)

'''The searchSamePeriodicities function provides the function to search through the habitArray for habits,
which have the given periodicity.
The periodicity- argument contains a Periodicity- value, which provides the data to search through the
habitArray.
While the habitArray get searched through, the result will be iterativley printed in the console.
The functions returns the a perArray, which gets appended step by step, that pytest can compare it later.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.''' 
def searchSamePeriodicities(periodicity):
    perArray = []
    for x in habitArray:
        if x.getPeriodicity() == periodicity.per:
            print(x)
            perArray.append(x.habitID)
    return (perArray)        
                                       
parser_searchSamePeriodicities = subparsers.add_parser('searchSamePeriodicities', help='Shows all habits with same periodicity!')
parser_searchSamePeriodicities.add_argument('-per', help='Periodicity of habit is to provide (DAILY/ WEEKLY!')
parser_searchSamePeriodicities.set_defaults(func= searchSamePeriodicities)                                        

'''The showHabit function provides the function to show the details of a given habit.
The id- argument contains an id, which provides the habit to search for.
When the related habit is found in the habitArray, the details of the habit will be printed.
Under the function- definition the function will be added to the argparse with related arguments to
run the function.''' 
def showHabit(id):
    for x in habitArray:
        if x.habitID == int(id.id):
            print(x)
            
parser_showHabit = subparsers.add_parser('showHabit', help='Shows details of the habit with given ID!')
parser_showHabit.add_argument('-id', help='ID of habit is to provide!')
parser_showHabit.set_defaults(func= showHabit)            

'''The completeTask function provides the function to complete the task of a given habit.
The id- argument contains an id, which provides the habit to search for.
First lastStreakValue and bestStreakValue will be initiliazed with value 0.
If the periodicity is DAILY, it will be checked if the lastFinished data is in the range of + 1 day or not.
If so, the lastStreakValue will be assigned with the current value of the habit and increased by 1.
Further the lastStrakValue will be compared with the bestStreak of the habit. If its higher than the best
streak, the bestStreakValue gets assigned the lastStreakValue.
If the lastFinished date is is out of the range of +1 day, lastStreakValue stays 0.
If the periodicity value is WEEKLY the date range will checked for +7 days.

Following will be the database updated depending if the bestStreakValues differs from 0.
The difference is that the bestStreak will be updated in the database, if its the case.
The data of the updated habit will be requested again and the habitArray- instance updated
as well.
Finally a new entry will be inserted in the habitcalendar.

Under the function- definition the function will be added to the argparse with related arguments to
run the function.''' 
def completeTask(id):
    lastStreakValue = 0
    bestStreakValue = 0
    for x in habitArray:
        if x.habitID == int(id.id):
            if x.getPeriodicity() == "DAILY":
                if x.getLastFinished() + timedelta(1) > date.today() or x.getLastFinished() + timedelta(1) == date.today():
                    lastStreakValue = x.getLastStreak() +1
                    if lastStreakValue > x.getBestStreak():
                        bestStreakValue = lastStreakValue
            else:
                if x.getLastFinished() + timedelta(7) > date.today() or x.getLastFinished() + timedelta(7) == date.today():
                    lastStreakValue = x.getLastStreak() +1
                    if lastStreakValue > x.getBestStreak():
                        bestStreakValue = lastStreakValue
    if bestStreakValue != 0:
        query3 = ('''UPDATE habits SET last_finishing = \'''' +str(date.today())+ '''\',  last_streak = '''+str(lastStreakValue)+''', best_streak = '''+str(bestStreakValue)+''' WHERE habit_ID = '''+id.id)
        cursor.execute(query3)
        cnx.commit()
    
        query2 = ('''SELECT * FROM habits WHERE habit_ID = '''+str(id.id))
        cursor.execute(query2)
    
        for x in habitArray:
            if x.habitID == int(id.id):
                for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:
                    if periodicity == "daily":
                        periodicityValue = Periodicity.DAILY.value
                    else:
                        periodicityValue = Periodicity.WEEKLY.value
                    x.setDatabaseValues(habit_ID, habit_name, habit_description, periodicityValue, last_finishing, last_streak, best_streak, habit_active)
    
        query5 = ('''INSERT INTO habitcalendar(habit_ID, completion_date) VALUES ('''+str(id.id)+''', \''''+str(date.today())+'''\')''')
        cursor.execute(query5)
        cnx.commit()
    else:
        query3 = ('''UPDATE habits SET last_finishing = \'''' +str(date.today())+'''\',  last_streak = '''+str(lastStreakValue)+''' WHERE habit_ID = '''+id.id)
        cursor.execute(query3)
        cnx.commit()
    
        query2 = ('''SELECT * FROM habits WHERE habit_ID = '''+str(id.id))
        cursor.execute(query2)
    
        for x in habitArray:
            if x.habitID == int(id.id):
                for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:
                    if periodicity == "daily":
                        periodicityValue = Periodicity.DAILY.value
                    else:
                        periodicityValue = Periodicity.WEEKLY.value
                    x.setDatabaseValues(habit_ID, habit_name, habit_description, periodicityValue, last_finishing, last_streak, best_streak, habit_active)
        query5 = ('''INSERT INTO habitcalendar(habit_ID, completion_date) VALUES ('''+str(id.id)+''', \''''+str(date.today())+'''\')''')
        cursor.execute(query5)
        cnx.commit()
                                       
parser_completeTask = subparsers.add_parser('completeTask', help='Completes habit with given ID!')
parser_completeTask.add_argument('-id', help='ID of habit is to provide!')
parser_completeTask.set_defaults(func= completeTask)                                       

# The loadDatabase- call at this point ensures, that the habitArray will be loaded, as the program starts.
loadDatabase() 

'''The following code checks if proper subcommands will be used in the console, when calling the program.
Otherwise the help function will be printed.'''
if __name__ == "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else: 
        args.func(args)    


