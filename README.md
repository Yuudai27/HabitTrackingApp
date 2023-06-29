# HabitTrackingApp

1.) Download the Python Anaconda installer
2.) Install Python Anaconda
3.) Start the Anaconda Prompt
4.) install the mysql-connector-python with the following command:
    pip install mysql-connector-python
5.) Unpack the sql files into your root- folder of the MySQL server 
6.) Open the terminal and enter the following command: “mysql -u root -p < habittrackingapp.sql” 
7.) The root password will be requested. After entering the command will be executed 
8.) Enter the following command: “mysql -u root -p < habits.sql” 
9.) The root password will be requested. After entering the command will be executed 
10.) Enter the following command: “mysql -u root -p < habitcalendar.sql” 
11.) The root password will be requested. After entering the command will be executed 
12.) The database is fully installed
13.) Unpack the py files into the folder you want to run it from
14.) Start the anaconda prompt 
15.) Now you can use the program with the following commands:

This command provides help for the available subcommands in the program.
The subcommand line have to be written instead the -h.
> python HabitTrackingApp.py -h

With this subcommand and the arguments -name, -desc, -per a new habit can be implemented with
set name, description and periodicity.
> insertDatabase -name value1(name) -desc value2(description) -per value3(DAILY/WEEKLY)

The subcommand allows to update a habit with the arguments for name, description, periodicity and habit active state.
> updateDatabase -id value1(id) -name value2(name) -desc value3(description) -per value4(DAILY/WEEKLY) -active value5(active boolean)

The deleteDatabase subcommand allows to delete a given habit.
> deleteDatabase -id value1(id)

The searchIDBestStreak subcommand allows to search the best streak of a given habit.
> searchIDBestStreak -id value1(id)

The complete Task subcommand completes the task for a given habit.
> completeTask -id value1(id)

The searchActiviteHabits subcommand allows to search for all active habits.
> searchActiveHabits -active value1(boolean)

The searchOverallBestStreak subcommand searches the habit with the streak of all habits.
> searchOverallBestStreak -active value1(boolean)

The searchSamePeriodicties subcommand allows to search for all habits with a given periodicity.
> searchSamePeriodicities -per value1(DAILY/WEEKLY)

The showHabit subcommand gives details for habits of the given id.
> showHabit -id value1(id)

The pytest program runs as an own command and tests the HabitTrackingApp.py. The test arguments are predefined.
> pytest test_HabitTrackingApp.py
