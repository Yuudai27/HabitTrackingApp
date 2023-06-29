USE habittrackingapp;

INSERT INTO `habits`(habit_name, habit_description, creation_date, periodicity, last_finishing, last_streak, best_streak, habit_active)
VALUES ('Brush teeth', 'Brush the teeth for at least 3 minutes!', '2023-05-01','daily','2023-05-31',31,31,true),
		 ('Go for a walk', 'Get out of the home office and go for a walk!', '2023-05-01','daily','2023-06-14',0,4,true),
		 ('Laundry', 'Do the laundry of the whole week!', '2023-05-01','weekly','2023-06-11',4,4,true),
		 ('Eat a healthy meal', 'Eat at least one healthy meal a day!', '2023-05-01','daily','2023-06-16',0,6,true),
		 ('Go to gym', 'Do some sports in the gym!', '2023-05-01','weekly','2023-06-12',4,4,true);
		 

