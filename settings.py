"""
Commom settings to all applications
"""
from decouple import config

RINEX_FOLDER = config('RINEX_FOLDER', default='/embrace/cosme/rinex/301/ango_2014/')
PATH_DCB = config('PATH_DCB', default='/embrace/tec/dcb/')
PATH_ORBIT = config('PATH_ORBIT', default='/embrace/tec/orbit/')
PATH_GLONASS_CHANNEL = config('PATH_GLONASS_CHANNEL', default='/embrace/tec/glonasschannel/')

MIN_REQUIRED_VERSION = config('MIN_REQUIRED_VERSION', default=2.11)
CONSTELATIONS = config('CONSTELATIONS', default=['G', 'R', 'E', 'C'])
TEC_RESOLUTION = config('TEC_RESOLUTION', default='hours')
TEC_RESOLUTION_VALUE = config('TEC_RESOLUTION_VALUE', default=1)
KEYS_SAVE = config('KEYS_SAVE', default=['time', 'slant-dtec', 'slant', 'detrended', 'bias', 'quality', 'vertical'])