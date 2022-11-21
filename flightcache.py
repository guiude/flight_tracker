class FlightCache:
    '''
    Template class that defines what a flight information cache must implement
    '''
    def __init__(self):
        self.monitored_flights = []

    def write_data(self, flight_data):
        '''
        Inputs data into the cache
        '''
        raise NotImplementedError()
    
    def clean_data(self):
        '''
        Removes outdated data from the cache
        '''
        raise NotImplementedError()
    
    def retrieve_flight(self, flight_code):
        '''
        Returns a flight from the set of flights whose info will be kept in the cache
        Also returns the time in seconds 
        '''
        raise NotImplementedError()
        
    def add_flight(self, flight_code):
        '''
        Includes a flight in the set of flights whose info will be kept in the cache
        '''
        raise NotImplementedError()

    def remove_flight(self):
        '''
        Removes a flight from the set of flights whose info will be kept in the cache
        '''
        raise NotImplementedError()

class NoCache(FlightCache):
    def write_data(self, flight_data):
        pass

    def clean_data(self):
        pass

    def retrieve_flight(self, flight_code):
        return [None, 1000000]
    
    def add_flight(self, flight_code):
        pass

    def remove_flight(self):
        pass

class TypeError(Exception):
    pass

def create_cache(cache_type):
    if cache_type == 'none':
        return NoCache()
    else:
        raise TypeError(f'Unknown cache type {cache_type}.')