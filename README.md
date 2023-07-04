# HabitTrackingApp

## Structure of the application
The application consists once of the Python program, with a separate Habit- and Periodicty-</br>
module and implements the argparse- and the mySQL-Connector-Python- module to be able</br>
to use a Command-Line-Interface and to have an interface to exchange information with</br>
the mySQL- database. The application holds the data of the habits in instances of the</br>
Habit- class, which gets updated with every change in the mySQL- database. </br>
The other part of the application is the mySQL- database, which has the habits- and the</br>
habitCalendar- table. The habits- table holds all information for the habits in the</br>
application (habit_ID, habit_name, habit_description, creation_date, periodicity,</br> 
last_finishing, last_streak, best_streak and habit_active) and the habitCalendar holds</br>
the information, when a habit got completed(calendar_ID, habit_ID and completion_date).

## Installing Python
1.) Download the Python Anaconda installer </br>
2.) Install Python Anaconda </br>
3.) Start the Anaconda Prompt </br>
4.) install the mysql-connector-python with the following command:
```python
pip install mysql-connector-python
``` 
## Installing mySQL-database
5.) install a mySQL- server on your system, if there is no existing </br>
6.) Unpack the sql files into your root- folder of the MySQL server </br>
7.) Open the terminal and enter the following command:
```python
mysql -u root -p < habittrackingapp.sql
``` 
8.) The root password will be requested. After entering the command will be executed </br>
9.) Enter the following command:
```python
mysql -u root -p < habits.sql
```
10.) The root password will be requested. After entering the command will be executed </br>
11.) Enter the following command:
```python
mysql -u root -p < habitcalendar.sql
``` 
12.) The root password will be requested. After entering the command will be executed </br>
13.) The database is fully installed </br></br>
## Get the Python application ready
14.) Unpack the py files into the folder you want to run it from </br>
15.) Open the habit_tracking_app.py with an editor and insert your user and password data </br>
for the mySQL- database at line 14
```python
cnx = mysql.connector.connect(user='****', password='*******',
```
16.) Start the anaconda prompt </br>
17.) Now you can use the program with the following commands:

This command provides help for the available subcommands in the program.
```python
python habit_tracking_app.py -h
```
## Subcommands for the application
With this subcommand and the arguments -name, -desc, -per a new habit can be implemented with
set name, description and periodicity.
```python
python habit_tracking_app.py insert_database -name TestHabit -desc Testing -per WEEKLY
```

The subcommand allows to update a habit with the arguments for name, description, periodicity and habit active state.
```python
python habit_tracking_app.py update_database -id 1 -name ChangedHabit -desc Changed -per DAILY -active True
```

The delete_database subcommand allows to delete a given habit.
```python
python habit_tracking_app.py delete_database -id 2
```

The search_id_best_streak subcommand allows to search the best streak of a given habit.
```python
python habit_tracking_app.py search_id_best_streak 1
```

The complete_task subcommand completes the task for a given habit.
```python
python habit_tracking_app.py complete_task -id 4
```

The search_activite_habits subcommand allows to search for all active habits.
```python
python habit_tracking_app.py search_activite_habits -active True
```

The search_overall_best_streak subcommand searches the habit with the streak of all habits.
```python
python habit_tracking_app.py search_overall_best_streak -active True
```

The search_same_periodicities subcommand allows to search for all habits with a given periodicity.
```python
python habit_tracking_app.py search_same_periodicities -per DAILY
```

The show_habit subcommand gives details for habits of the given id.
```python
python habit_tracking_app.py show_habit -id 4
```
## Testing the application 
If you want to test the application you can use the subcommands in the following order: </br>
First show all active habits.
```python
python habit_tracking_app.py search_activite_habits -active True
```
Then create a new habit similar like this.
```python
python habit_tracking_app.py insert_database -name TestHabit -desc Testing -per WEEKLY
```
Try again to show all habits and the new habit should be included in the output.
```python
python habit_tracking_app.py search_activite_habits -active True
```
You can try to update the new habit, you've just created. Take the given ID in the output.
```python
python habit_tracking_app.py update_database -id 6 -name ChangedHabit -desc Changed -per DAILY -active True
```
With the following line you can directly show your habit with using the same ID again.
```python
python habit_tracking_app.py show_habit -id 6
```
Let's complete your new habit for the first time for the given ID.
```python
python habit_tracking_app.py complete_task -id 6
```
Try to get the best streak of your new habit with the ID.
```python
python habit_tracking_app.py search_id_best_streak 6
```
Finally, let's delete the new habit with the ID from before.
```python
python habit_tracking_app.py delete_database -id 6
```
Try to check for all active habits again and your habit should be gone.
```python
python habit_tracking_app.py search_activite_habits -active True
```
At the end let's analyze the habits in the system and </br>
search for the best streak
```python
python habit_tracking_app.py search_overall_best_streak -active True
```
or let's search for all habits with the periodicity DAILY.
```python
python habit_tracking_app.py search_same_periodicities -per DAILY
```

## Pytest program to test the application
The pytest program runs as an own command and tests the HabitTrackingApp.py. The test arguments are predefined.
```python
pytest test_habit_tracking_app.py
```


