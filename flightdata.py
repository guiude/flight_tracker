import config
import requests
import flightcache

FLIGHT_CACHE = flightcache.create_cache(config.CACHING_METHOD)

class FlightExternalData():
    '''
    Class template for gathering and parsing flight External data
    '''
    def __init__(self):
        self.raw_data = None
        self.parsed_data = None
    
    def fetch_data(self, flight_code):
        raise NotImplementedError()
    
    def parse_data(self):
        raise NotImplementedError()

class AirlabsAPIData(FlightExternalData):
    '''
    Implementation to obtain external data from the Airlabs API
    '''
    def fetch_data(self, flight_code):
        '''
        Retrieves data from airlabs and stores it in the object
        '''
        api_base = 'http://airlabs.co/api/v9/'
        endpoint = 'flight'
        params = {'api_key': config.AIRLABS_API_KEY, 'flight_iata': flight_code}

        
        response = requests.get(api_base+endpoint,
                                params=params)
        
        response = response.json()
        
        FLIGHT_CACHE.write_data(response)
        self.raw_data = response
    
    def parse_data(self):
        '''
        Parses the raw data obtained externally into the format that is friendly for the other parts of the application
        '''
        self.parsed_data = self.raw_data
        FLIGHT_CACHE.write_data(self.parsed_data)

class APIError(Exception):
    pass

def create_API_bot(api_name):
    if api_name == 'airlabs':
        return AirlabsAPIData()
    else:
        raise APIError(f'Unknown API {api_name}.')

#Our orchestrator function so far. there is still tons of work to do
def get_flight_data(flight_code):
    '''
    This function receives an IATA flight code and returns a dictionary with all the info that the app could find online.
    An IATA code is composed by two letters identifying the airline and 4 digits identifying the flight
    '''
    flight_data = {}

    #Start by searching the cache for the flight
    cached_results = FLIGHT_CACHE.retrieve_flight(flight_code)
    if (cached_results[0] != None) and (cached_results[1] < config.TIME_TO_FORGET):
        flight_data = cached_results[0]
        return flight_data
    
    #If the cache doesn't contain the data we're searching for, obtain it externally
    external_data = create_API_bot('airlabs')
    external_data.fetch_data(flight_code)
    external_data.parse_data()
    return external_data.parsed_data