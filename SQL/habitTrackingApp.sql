
CREATE DATABASE HabitTrackingApp; 
USE HabitTrackingApp;
/*
Creates a table with the name habits and
the following attributes:
habit_ID as primary key, type int
habit_name as VARCHAR, which holds the habit name
habit_description as VARCHAR, which holds the habit description
creation_date as date, which holds the date of the creation date
periodicity as enum with the value of the periodicity
last_finishing as date holding the last completion date
last_streak as int, which holds the last streak of the habit
best_streak as int, which holds the best streak of the habit
habit_active as bool, which holds the active status of the habit
*/

CREATE TABLE IF NOT EXISTS `habits` (
  `habit_ID` INT AUTO_INCREMENT, 
  `habit_name` VARCHAR(100) NOT NULL,
  `habit_description` VARCHAR(100) NOT NULL,
  `creation_date` DATE NOT NULL,
  `periodicity` ENUM('daily','weekly') DEFAULT 'daily',
  `last_finishing` DATE NOT NULL,
  `last_streak` INT NOT NULL,
  `best_streak` INT NOT NULL,
  `habit_active` BOOL DEFAULT TRUE,
  PRIMARY KEY (habit_ID)
) ENGINE=InnoDB DEFAULT CHARSET=LATIN1;

/*
Creates a table with the name habitCalendar and
the following attributes:
calendar_ID as primary key, type int
habit_ID as foreign key, type int
completion_date as date holding the last completion date
*/
CREATE TABLE IF NOT EXISTS `habitCalendar` (
  `calendar_ID` INT AUTO_INCREMENT,
  `habit_ID` INT NOT NULL, 
  `completion_date` DATE NOT NULL,
  PRIMARY KEY (calendar_ID),
  FOREIGN KEY (habit_ID) REFERENCES `habits`(habit_ID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=LATIN1;

