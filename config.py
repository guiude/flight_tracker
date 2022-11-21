# File containing configuration parameters for the flight tracker application

# Standard API to use
STANDARD_API = 'airlabs'

# Airlabs API access info
AIRLABS_API_KEY = '2b18073f-2764-4e9c-a654-c59450d78f34'

# Aviation Stack API access info
AVSTACK_API_KEY = '921d686a59f0184d930e7494d2e40611'

# Cache settings
# The possible choices for caching methods are: 'none'
# So far, the cache class is only a template for a future implementation
CACHING_METHOD = 'none' 
TIME_TO_FORGET = 300 #maximum time in seconds for which the cached data will be used
