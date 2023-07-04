from habit import Habit
from periodicity import Periodicity
from datetime import date, timedelta
from argparse import ArgumentParser
import mysql.connector
#habit_array is an Array, which will hold all habit- instances, while the program is running.
habit_array = []
#************************************************************************************************** 
#Communication with mySQL database
#connection and functions
#************************************************************************************************** 
'''The mysql.connector module gets implemented to create an interface between python and 
the mysql- database. The connection will be assigned with the login data to the sql-server'''
cnx = mysql.connector.connect(user='****', password='*******',
                             host='localhost', database='habittrackingapp')
cursor = cnx.cursor(buffered=True)


def insert_database(habit_data):
    '''The insert_database function provides the function to insert a new habit into the mysql database.
    The habit_data- argument contains different values as name, desc(description) and per(periodicity) for 
    the new habit. The string-value for per will be checked and a fitting Periodicity- value will be
    applied.
    The data will be inserted in a data-query as insert-statement for the mysql-server.
    After creating the new habit, the habitArray will be cleared and loaded with current data from
    the database.
    
    Parameter:
                habit_data (object): object, which holds the attributes:
                                    name (string): Holds the name for the new habit
                                    desc (string): Holds the description for the new habit
                                    per (string): Holds the periodicity value for the new habit
    Returns:
                none
    '''   
    if habit_data.per == "DAILY":
        periodicity_value = Periodicity.DAILY.value
    else:
        periodicity_value = Periodicity.WEEKLY.value
    
    query1= ('''INSERT INTO habits(habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active)
    VALUES (\''''+habit_data.name+'''\', \''''+habit_data.desc+'''\', \''''+str(date.today())+'''\',\''''+periodicity_value+'''\', \''''+str(date.today())+'''\',0,0,true)''')
    cursor.execute(query1)
    cnx.commit()
    habit_array.clear()
    load_database()
    
def load_database():
    '''The loadDatabase function loads the current data from the mysql database into the habitArray.
    After requesting the data from the sql server, the data gets appended to the habitArray as 
    Habit- instances.
    
    Parameter:
                none
    Returns:
                none
    '''
    query2 = ('''SELECT * FROM habits''')
    cursor.execute(query2)
    
    for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:  
        if periodicity == 'daily':
            periodicity_value = Periodicity.DAILY.value
        else:
            periodicity_value = Periodicity.WEEKLY.value    
        habit_array.append(Habit(habit_ID, habit_name, habit_description, creation_date, periodicity_value, last_finishing, last_streak, best_streak, habit_active))


def update_database(habit_data):      
    '''The update_database function provides the function to update a habit in the mysql database.
    The habit_data- argument contains different values as id, name, desc(description), per(periodicity) and 
    active(active status) for the habit. 
    After updating the data in the database, the data for the habit gets requested from the database and
    the set_database_values- function of the Habit- instance will be used, that the whole habit_array doesn't
    have to be renewed.
    The data will be inserted in a data-query as insert-statement for the mysql-server.
       
    Parameter:
                habit_data (object): object, which holds the attributes:
                                    name (string): Holds the name for the habit to change
                                    desc (string): Holds the description for the habit to change
                                    per (string): Holds the periodicity value for the habit to change
                                    active (bool): Holds the active state of the habit to change
                                    id (int): Holds the ID of the habit to change
    Returns:
    
    '''    
    query3 = ('''UPDATE habits SET habit_name = \''''+habit_data.name+'''\', habit_description = \''''+habit_data.desc+'''\', periodicity = \''''+habit_data.per+'''\', habit_active = '''+str(habit_data.active)+''' WHERE habit_ID = '''+str(habit_data.id))
    cursor.execute(query3)
    cnx.commit()
    
    query2 = ('''SELECT * FROM habits WHERE habit_ID = '''+str(habit_data.id))
    cursor.execute(query2)
    
    for x in habit_array:
        if x.habit_id == int(habit_data.id):
            for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:
                if habit_data.per == 'DAILY':
                    periodicity_value = Periodicity.DAILY.value
                else:
                    periodicity_value = Periodicity.WEEKLY.value
                x.set_database_values(habit_ID, habit_name, habit_description, periodicity_value, last_finishing, last_streak, best_streak, habit_active)
                

def delete_database(habit_id):
    '''The delete_database function provides the function to delete a habit from the mysql database.
    The habit_id- argument contains the value id of the habit to delete. 
    After deleting the data in the database, the habit_array will be cleared and loaded with current data from
    the database.
     
    Parameter:
                habit_id (object): object, which holds the attributes:
                                  id (int): Holds the ID of the habit to delete
    Returns:
                none
    '''      
    query4 = ('''DELETE FROM habits WHERE habit_ID = '''+str(habit_id.id))
    cursor.execute(query4)
    cnx.commit()
    habit_array.clear()
    load_database()
#************************************************************************************************** 
#Analytical funtions
#**************************************************************************************************        
def search_overall_best_streak(active):   
    '''The search_overall_best_streak function provides the function to search through the habit_array, comparing the
    best streaks and holding the best_streak- value and the related ID separated for DAILY and WEEKLY habits.
    The active- argument contains a boolean, which just exists to be able to run the function
    with argparse and pytest as well. 
    After the habit_array got searched through, the result will be printed in the console.
    The functions returns the ID of the habit with the best_streak, that pytest can compare it later.
      
    Parameter:
                active (object): object, which holds the attributes:
                                  active (bool): Holds the value of a boolean,
                                  but jsut necessary to be able to run the CLI with
                                  argparse and run Pytest
    Returns:
                id_array (int): returns IDs of the habit with the best streak for DAILY and WEEKLY habits
    '''    
    daily_best_streak = 0
    daily_best_streak_id = 0
    weekly_best_streak = 0
    weekly_best_streak_id = 0
    
    for x in habit_array:
        if x.get_periodicity() == "DAILY":
            if x.get_best_streak() >= daily_best_streak:
                daily_best_streak = x.get_best_streak()
                daily_best_streak_id = x.habit_id
        else:
            if x.get_best_streak() >= weekly_best_streak:
                weekly_best_streak = x.get_best_streak()
                weekly_best_streak_id = x.habit_id
                
        
    for y in habit_array:
        if y.habit_id == daily_best_streak_id:
            print("The habit {0} with the ID {1} has the best streak of {2} for DAILY periodicity!".format(y.habit_name, y.habit_id, y.get_best_streak()))
        if y.habit_id == weekly_best_streak_id:
            print("The habit {0} with the ID {1} has the best streak of {2} for WEEKLY periodicity!".format(y.habit_name, y.habit_id, y.get_best_streak()))
    id_array = [daily_best_streak_id, weekly_best_streak_id]
    return (id_array)    


def search_active_habits(active_state):
    '''The search_active_habits function provides the function to search through the habit_array for habits,
    which are currently active.
    The active- argument contains a boolean, which just exists to be able to run the function
    with argparse and pytest as well. 
    While the habit_array get searched through, the result will be iterativley printed in the console.
    The functions returns the an active_array, which gets appended step by step, that pytest can compare it later.
     
    Parameter:
                active_state (object): object, which holds the attributes:
                                  active (bool): Holds the value of a boolean,
                                  but jsut necessary to be able to run the CLI with
                                  argparse and run Pytest
    Returns:
                active_array (int): returns the array with all ID's of habits, which are active
    '''   
    active_array = []
    for x in habit_array:
        if x.get_active_state() == True:
            print(x)
            active_array.append(x.habit_id)
    return (active_array)


def search_id_best_streak(id): 
    '''The search_id_best_streak function provides the function to search through the habit_array for the 
    best_streak of the given habit ID.
    The id- argument contains an id, which provides the habit to search for. 
    When the related habit is found in the habit_array, the result will be printed with the best_streak.
      
    Parameter:
                habit_id (object): object, which holds the attributes:
                                  id (int): Holds the ID of the habit to search through for the best streak
    Returns:
                x.get_best_streak() (int): returns the value of the best streak for the habit
    '''  
    for x in habit_array:
        if x.habit_id == int(id.id):
            print("The habit {0} with the ID {1} has the best streak of {2}!".format(x.habit_name, x.habit_id, x.get_best_streak()))
            return (x.get_best_streak())
            

def search_same_periodicities(periodicity):
    '''The search_same_periodicities function provides the function to search through the habit_array for habits,
    which have the given periodicity.
    The periodicity- argument contains a Periodicity- value, which provides the data to search through the
    habit_array.
    While the habit_array get searched through, the result will be iterativley printed in the console.
    The functions returns the a per_array, which gets appended step by step, that pytest can compare it later.
        
    Parameter:
                periodicty (object): object, which holds the attributes:
                                    per (string): Holds the Periodicity value as string
    Returns:
                per_array (int): returns the array with ID of all habit with the given periodicity
    '''  
    per_array = []
    for x in habit_array:
        if x.get_periodicity() == periodicity.per:
            print(x)
            per_array.append(x.habit_id)
    return (per_array)        
#************************************************************************************************** 
#Workflow functions    
#************************************************************************************************** 
def show_habit(id):
    '''The show_habit function provides the function to show the details of a given habit.
    The id- argument contains an id, which provides the habit to search for.
    When the related habit is found in the habit_array, the details of the habit will be printed.
       
    Parameter:
                habit_id (object): object, which holds the attributes:
                                  id (int): Holds the ID of the habit to show
    Returns:
                none
    '''   
    for x in habit_array:
        if x.habit_id == int(id.id):
            print(x)
                    

def complete_task(id):
    '''The complete_task function provides the function to complete the task of a given habit.
    The id- argument contains an id, which provides the habit to search for.
    First last_streak_value and best_streak_value will be initiliazed with value 0.
    If the periodicity is DAILY, it will be checked if the last_finished data is in the range of + 1 day or not.
    If so, the last_streak_value will be assigned with the current value of the habit and increased by 1.
    Further the last_streak_value will be compared with the best_streak of the habit. If its higher than the best
    streak, the best_streak_value gets assigned the last_streak_value.
    If the last_finished date is is out of the range of +1 day, last_streak_value stays 0.
    If the periodicity value is WEEKLY the date range will checked for +7 days.

    Following will be the database updated depending if the best_streak_value differs from 0.
    The difference is that the best_streak will be updated in the database, if its the case.
    The data of the updated habit will be requested again and the habit_array- instance updated
    as well.
    Finally a new entry will be inserted in the habitcalendar.
    
    Parameter:
                habit_id (object): object, which holds the attributes:
                                  id (int): Holds the ID of the habit to complete
    Returns:
                none
    '''      
    last_streak_value = 0
    best_streak_value = 0
    for x in habit_array:
        if x.habit_id == int(id.id):
            if x.get_periodicity() == "DAILY":
                if x.get_last_finished() + timedelta(1) > date.today() or x.get_last_finished() + timedelta(1) == date.today():
                    last_streak_value = x.get_last_streak() +1
                    if last_streak_value > x.get_best_streak():
                        best_streak_value = last_streak_value
            else:
                if x.get_last_finished() + timedelta(7) > date.today() or x.get_last_finished() + timedelta(7) == date.today():
                    last_streak_value = x.get_last_streak() +1
                    if last_streak_value > x.get_best_streak():
                        best_streak_value = last_streak_value
    if best_streak_value != 0:
        query3 = ('''UPDATE habits SET last_finishing = \'''' +str(date.today())+ '''\',  last_streak = '''+str(last_streak_value)+''', best_streak = '''+str(best_streak_value)+''' WHERE habit_ID = '''+str(id.id))
        cursor.execute(query3)
        cnx.commit()
    
        query2 = ('''SELECT * FROM habits WHERE habit_ID = '''+str(id.id))
        cursor.execute(query2)
    
        for x in habit_array:
            if x.habit_id == int(id.id):
                for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:
                    if periodicity == "daily":
                        periodicity_value = Periodicity.DAILY.value
                    else:
                        periodicity_value = Periodicity.WEEKLY.value
                    x.set_database_values(habit_ID, habit_name, habit_description, periodicity_value, last_finishing, last_streak, best_streak, habit_active)
    
        query5 = ('''INSERT INTO habitcalendar(habit_ID, completion_date) VALUES ('''+str(id.id)+''', \''''+str(date.today())+'''\')''')
        cursor.execute(query5)
        cnx.commit()
    else:
        query3 = ('''UPDATE habits SET last_finishing = \'''' +str(date.today())+'''\',  last_streak = '''+str(last_streak_value)+''' WHERE habit_ID = '''+str(id.id))
        cursor.execute(query3)
        cnx.commit()
    
        query2 = ('''SELECT * FROM habits WHERE habit_ID = '''+str(id.id))
        cursor.execute(query2)
    
        for x in habit_array:
            if x.habit_id == int(id.id):
                for(habit_ID, habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active) in cursor:
                    if periodicity == "daily":
                        periodicity_value = Periodicity.DAILY.value
                    else:
                        periodicity_value = Periodicity.WEEKLY.value
                    x.set_database_values(habit_ID, habit_name, habit_description, periodicity_value, last_finishing, last_streak, best_streak, habit_active)
        query5 = ('''INSERT INTO habitcalendar(habit_ID, completion_date) VALUES ('''+str(id.id)+''', \''''+str(date.today())+'''\')''')
        cursor.execute(query5)
        cnx.commit()
                                                                       

# The load_database- call at this point ensures, that the habit_array will be loaded, as the program starts.
load_database() 
#************************************************************************************************** 
#Creating of the Command-Line-Interface
#************************************************************************************************** 
'''In this part the argparse- modul will be set initialized and the functions step by step
later after defining these.'''
cli = ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")

#creates subcommand for insert_database
parser_insert_database = subparsers.add_parser('insert_database', help='Creates new habit with given details!')
parser_insert_database.add_argument('-name', help='Name of habit is to provide!')
parser_insert_database.add_argument('-desc', help='Description of habit is to provide!')
parser_insert_database.add_argument('-per', help='Periodicity of habit is to provide!')
parser_insert_database.set_defaults(func= insert_database)    

#creates subcommand for update_database
parser_update_database = subparsers.add_parser('update_database', help='Updates habit with given details.')
parser_update_database.add_argument('-id', help='ID of habit is to provide!')
parser_update_database.add_argument('-name', help='Name of habit is to provide!')
parser_update_database.add_argument('-desc', help='Description of habit is to provide!')
parser_update_database.add_argument('-per', help='Periodicity of habit is to provide!')
parser_update_database.add_argument('-active', help='Active status of habit is to provide!')
parser_update_database.set_defaults(func= update_database)   

#creates subcommand for delete_database
parser_delete_database = subparsers.add_parser('delete_database', help='Delete habit for given ID in database!')
parser_delete_database.add_argument('-id', help='ID of habit is to provide!')
parser_delete_database.set_defaults(func= delete_database)

#creates subcommand for search_overall_best_streak
parser_search_overall_best_streak = subparsers.add_parser('search_overall_best_streak', help='Search for habit with the best streak!')
parser_search_overall_best_streak.add_argument('-active', type=bool, help='Set to True')
parser_search_overall_best_streak.set_defaults(func= search_overall_best_streak) 

#creates subcommand for search_active_habits
parser_search_active_habits = subparsers.add_parser('search_active_habits', help='Search for active habits!')
parser_search_active_habits.add_argument('-active', type=bool, help='Set to True')
parser_search_active_habits.set_defaults(func= search_active_habits) 

#creates subcommand for search_id_best_streak
parser_search_id_best_streak = subparsers.add_parser('search_id_best_streak', help='Search the best streak for an ID!')
parser_search_id_best_streak.add_argument('-id', help='ID of habit is to provide!')
parser_search_id_best_streak.set_defaults(func= search_id_best_streak)

#creates subcommand for search_same-periodicities
parser_search_same_periodicities = subparsers.add_parser('search_same_periodicities', help='Shows all habits with same periodicity!')
parser_search_same_periodicities.add_argument('-per', help='Periodicity of habit is to provide (DAILY/ WEEKLY!')
parser_search_same_periodicities.set_defaults(func= search_same_periodicities) 

#creates subcommand for show_habit
parser_show_habit = subparsers.add_parser('show_habit', help='Shows details of the habit with given ID!')
parser_show_habit.add_argument('-id', help='ID of habit is to provide!')
parser_show_habit.set_defaults(func= show_habit)  

#creates subcommand for complete_task
parser_complete_task = subparsers.add_parser('complete_task', help='Completes habit with given ID!')
parser_complete_task.add_argument('-id', help='ID of habit is to provide!')
parser_complete_task.set_defaults(func= complete_task)  

'''The following code checks if proper subcommands will be used in the console, when calling the program.
Otherwise the help function will be printed.'''
if __name__ == "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else: 
        args.func(args)    

               
