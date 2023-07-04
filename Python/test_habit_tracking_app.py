import pytest
import sys
from periodicity import Periodicity
from datetime import date
import habit_tracking_app
from habit_tracking_app import complete_task, update_database, search_overall_best_streak, search_active_habits, search_id_best_streak, show_habit, insert_database, delete_database, search_same_periodicities

class ID: 
    '''The ID- class provides an object with an id- attribute, to
    be able to call functions from the habit_tracking_app and also being
    able to user argparse.'''
    def __init__(self, id):
        self.id = id


class Active: 
    '''The Active- class provides an object with an active- attribute, to
    be able to call functions from the habit_tracking_app and also being
    able to user argparse.'''
    def __init__(self, active):
        self.active = active


class Create: 
    '''The Create- class provides an object with name, desc and per- attributes, 
    to be able to call functions from the habit_tracking_app and also being
    able to user argparse.'''
    def __init__(self, name, desc, per):
        self.name = name
        self.desc = desc
        self.per = per 


class Update:
    '''The Update- class provides an object with id, name, desc, per and active- 
    attributes, to be able to call functions from the habit_tracking_app and also being
    able to user argparse.'''
    def __init__(self, id, name, desc, per, active):
        self.id = id
        self.name = name
        self.desc = desc
        self.per = per
        self.active = active


class Perio: 
    '''The Perio- class provides an object with an per- attribute, to
    be able to call functions from the habit_tracking_app and also being
    able to user argparse.'''
    def __init__(self, per):
        self.per = per

     
def test_insert_database():
    '''The test_insertDatabase- function tests the insertDatabase- function from the 
    habit_tracking_app. A habit with predefined values will be created in the
    database. To check the result, the habit_array will searched through for 
    the newly created habit and its values compared to predefined ones.
    
    Parameter:
                none
    Returns:
                none
    ''' 
    name = "Climbing"
    desc = "Rock it!"
    per = Periodicity.WEEKLY.value
    
        
    testData = Create(name, desc, per)
    
    insert_database(testData)
    for x in habit_tracking_app.habit_array:
        if x.habit_name == name:
            assert x.habit_description == desc
            assert x.get_periodicity() == per
            assert x.creation_date == date.today()
  
              
def test_update_database():
    '''The test_update_database- function tests the update_database- function from the 
    habit_tracking_app. A habit with predefined values will be updated in the
    database. To check the result, the habit_array will searched through for 
    the currently updated habit and its values compared to predefined ones.
    
    Parameter:
                none
    Returns:
                none
    ''' 
    id = 2
    name = "kitchen"
    desc = "cook in it"
    per = Periodicity.DAILY.value
    active = True
    
        
    test_data = Update(id, name, desc, per, active)
    
    update_database(test_data)
    for x in habit_tracking_app.habit_array:
        if x.habit_id == id:
            assert x.habit_name == name and x.habit_description == desc and x.get_periodicity() == per and x.get_active_state() == active


def test_delete_database():
    '''The test_delete_database- function tests the delete_database- function from the 
    habit_tracking_app. A habit with a predefined id will be deleted from the
    database. To check the result, the habit_array will searched through for 
    the deleted habit and as long as the counter stays 0 the test passes.
    
    Parameter:
                none
    Returns:
                none
    ''' 
    id_value = ID(6)
    delete_database(id_value)
    
    counter = 0
    for x in habit_tracking_app.habit_array:
        if x.habit_id == 6:
            counter = counter + 1
    assert counter == 0            

                    
def test_search_id_best_streak():
    '''The test_search_id_best_streak- function tests the search_id_best_streak- function from the 
    habit_tracking_app. A habit with a predefined id will be searched in the habit_array
    and the best_streak- value derived. 
    The result will be compared to the invoked search_id_best_streak- function.
    
    Parameter:
                none
    Returns:
                none
    '''
    id_value = ID(1)
    best_streak = 0
    
    for x in habit_tracking_app.habit_array:
        if x.habit_id == id_value.id:
            best_streak = x.get_best_streak()
    
    assert search_id_best_streak(id_value) == best_streak    
 

def test_complete_task():
    '''The test_complete_task- function tests the complete_task- function from the 
    HabitTrackingApp. A habit with a predefined id will be completed in the database. 
    The get_last_finished- date will be compared to the today- value at the point calling
    the function.
    
    Parameter:
                none
    Returns:
                none
    '''    
    id_value = ID("1")
    complete_task(id_value)
    for x in habit_tracking_app.habit_array:
        if x.habit_id == 1:
            assert x.get_last_finished() == date.today() 
           
        
def test_search_active_habits():
    '''The test_search_active_habits- function tests the search_active_habits- function from the 
    habit_tracking_app. The activeBool variable is just to call the function with an argument,
    that it still works with argparse.
    An activeCounter counts the active habits in the habit_array.
    The result will be compared to the length of the result array of the invoked 
    search_active_habits- function.
    
    Parameter:
                none
    Returns:
                none
    '''  
    active_bool = Active(True)
    active_counter = 0
    for x in habit_tracking_app.habit_array:
        if x.get_active_state() == True:
            active_counter = active_counter + 1
            
    assert len(search_active_habits(active_bool)) == active_counter

    
def test_search_overall_best_streak():
    '''The test_search_overall_best_streak- function tests the search_overall_best_streak- function from the 
    habit_tracking_app. The activeBool variable is just to call the function with an argument,
    that it still works with argparse.
    The daily_best_streak and daily_best_streak_id will hold the results for the ID and the value of the habit with
    the highest best streak for DAILY- habits in the habitArray and weekly_best_streak and weekly_best_streak_id for
    WEEKLY- habits.
    The resulting IDs will be compared to the IDs of the invoked search_overall_best_streak- function.'''
    active_bool = Active(True)
    daily_best_streak = 0
    daily_best_streak_id = 0
    weekly_best_streak = 0
    weekly_best_streak_id = 0
    
    for x in habit_tracking_app.habit_array:
        if x.get_periodicity() == "DAILY":
            if x.get_best_streak() >= daily_best_streak:
                daily_best_streak = x.get_best_streak()
                daily_best_streak_id = x.habit_id
        else:
            if x.get_best_streak() >= weekly_best_streak:
                weekly_best_streak = x.get_best_streak()
                weekly_best_streak_id = x.habit_id
                
    id_array = search_overall_best_streak(active_bool)
    assert id_array[0] == daily_best_streak_id and id_array[1] == weekly_best_streak_id 

    
def test_search_same_periodicities():
    '''The test_search_same_periodicities- function tests the search_same_periodicities- function from the 
    habit_tracking_app. The per_value variable provides the periodicity value to invoke and compare the 
    function later.
    The habit_array will be searched for the given periodicity and counts it with the per_counter.
    The resulting counter will be compared to the length of the result array of the invoked 
    search_same_periodicities- function.
    
    Parameter:
                none
    Returns:
                none
    '''   
    per_value = Perio(Periodicity.DAILY.value)
    per_counter = 0
    for x in habit_tracking_app.habit_array:
        if x.get_periodicity() == per_value.per:
            per_counter = per_counter + 1       
    assert len(search_same_periodicities(per_value)) == per_counter
