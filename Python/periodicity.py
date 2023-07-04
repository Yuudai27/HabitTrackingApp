from enum import Enum
'''The Periodicity class provides Enum values. The attributes DAILY and WEEKLY
holding similar named values for the periodicities used by other modules.'''
class Periodicity(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    
    Periodicity = Enum('Periodicity', ['DAILY', 'WEEKLY'])
