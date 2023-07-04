from datetime import date
import periodicity

# Habit class
class Habit:
      
    
    def __init__(self, id, name, description, creation_date, periodicity, last_finishing, last_streak, best_streak, active):
        '''The constructor for the Habit class takes id, name, description, creation_date, periodicity, last_finishing, last_streak,
        best_streak and active arguments and assigns these to the Habits attributes.
    
        Parameter:
                    self: Accessing the instance
                    id (int): ID of the habit
                    name (string): Name of the habit
                    description (string): Description of the habit
                    creation_date (date): Date of creation
                    periodicity (string): Holds the value of the an Periodicity
                    last_finishing (date): Date for the last completion
                    last_streak (int): Counter for the current streak
                    best_streak (int): Integer holding best streak value 
                    active (bool): States if the habit is active
        Returns:
                    none
        '''        
        self.habit_id = id
        self.habit_name = name
        self.habit_description = description
        self.creation_date = creation_date
        self.periodicity = periodicity
        self.last_finishing = last_finishing
        self.last_streak = last_streak
        self.best_streak = best_streak
        self.habit_active = active
   
      
    def set_database_values(self, id, name, description, periodicity, last_finishing, last_streak, best_streak, active):
        '''The set_database_values function takes id, name, description, periodicity, last_finishing, last_streak, best_streak
        and active arguments for updating database function and assigns these to the given habits attributes.
    
        Parameter:
                    self: Accessing the instance
                    id (int): ID of the habit
                    name (string): Name of the habit
                    description (string): Description of the habit
                    creation_date (date): Date of creation
                    periodicity (string): Holds the value of the an Periodicity
                    last_finishing (date): Date for the last completion
                    last_streak (int): Counter for the current streak
                    best_streak (int): Integer holding best streak value 
                    active (bool): States if the habit is active
        Returns:
                    none
        '''  
        self.habit_id = id
        self.habit_name = name
        self.habit_description = description
        self.periodicity = periodicity
        self.last_finishing = last_finishing
        self.last_streak = last_streak
        self.best_streak = best_streak
        self.habit_active = active    
    
   
    def get_last_finished(self):
        '''The get_last_finished function returns the value of last_finishing.
    
        Parameter:
                    self: Accessing the instance
        Returns:
                    none
        '''
        return self.last_finishing     
    
     
    def get_periodicity(self):
        '''The get_periodicity function returns the value of periodicity.
    
        Parameter:
                    self: Accessing the instance
        Returns:
                    periodicity (string): returns periodicity value as string
        '''
        return str(self.periodicity)
      
    
    def get_last_streak(self):
        '''The get_last_streak function returns the value of last_streak.
    
        Parameter:
                    self: Accessing the instance
        Returns:
                    last_streak (int): returns the value for last_streak
        '''
        return self.last_streak
    
    
    def get_best_streak(self):
        '''The get_best_streak function returns the value of best_streak.
    
        Parameter:
                    self: Accessing the instance
        Returns:
                    best_streak (int): returns value for best_streak
        '''
        return self.best_streak
    
   
    def get_active_state(self):
        '''The get_active_state function returns the value of habit_active.
    
        Parameter:
                    self: Accessing the instance
        Returns:
                    habit_active (bool): returns the value of habit_active
        
        '''
        return self.habit_active 
    
    
    def __str__(self):
        '''The string representation function returns the attributes of the habit.
    
        Parameter:
                    self: Accessing the instance
        Returns:
                    str: returns String-method for the habit- class with details about the instance
        '''
        return """ID: {0}\nName: {1}\nDescription: {2}\nCreation date: {3}\nPeriodicity: {4}\nLast completed: {5}\nLast streak: {6}\nBest streak: {7}\nActive state: {8}""".format(self.habit_id, self.habit_name, self.habit_description, self.creation_date, self.periodicity, self.last_finishing,
               self.last_streak, self.best_streak, self.habit_active)
    
    
