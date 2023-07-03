# HabitTrackingApp

In this README it will be explained how to install all the necessary components</br>
for the Python application.
##Installing Python
1.) Download the Python Anaconda installer </br>
2.) Install Python Anaconda </br>
3.) Start the Anaconda Prompt </br>
4.) install the mysql-connector-python with the following command:
```python
pip install mysql-connector-python
``` </br>
##Installing mySQL
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
15.) Start the anaconda prompt </br>
16.) Now you can use the program with the following commands:

This command provides help for the available subcommands in the program.
```python
python HabitTrackingApp.py -h
```
## Subcommands for the application
With this subcommand and the arguments -name, -desc, -per a new habit can be implemented with
set name, description and periodicity.
```python
python HabitTrackingApp.py insertDatabase -name TestHabit -desc Testing -per WEEKLY
```

The subcommand allows to update a habit with the arguments for name, description, periodicity and habit active state.
```python
python HabitTrackingApp.py updateDatabase -id 1 -name ChangedHabit -desc Changed -per DAILY -active True
```

The deleteDatabase subcommand allows to delete a given habit.
```python
python HabitTrackingApp.py deleteDatabase -id 2
```

The searchIDBestStreak subcommand allows to search the best streak of a given habit.
```python
python HabitTrackingApp.py searchIDBestStreak 1
```

The complete Task subcommand completes the task for a given habit.
```python
python HabitTrackingApp.py completeTask -id 4
```

The searchActiviteHabits subcommand allows to search for all active habits.
```python
python HabitTrackingApp.py searchActiveHabits -active True
```

The searchOverallBestStreak subcommand searches the habit with the streak of all habits.
```python
python HabitTrackingApp.py searchOverallBestStreak -active True
```

The searchSamePeriodicties subcommand allows to search for all habits with a given periodicity.
```python
python HabitTrackingApp.py searchSamePeriodicities -per DAILY
```

The showHabit subcommand gives details for habits of the given id.
```python
python HabitTrackingApp.py showHabit -id 4
```
## Pytest program to test the application
The pytest program runs as an own command and tests the HabitTrackingApp.py. The test arguments are predefined.
```python
pytest test_HabitTrackingApp.py
```
