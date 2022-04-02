class dictionary_parser:
    def __init__(self, d):
        if type(d) != dict:
            raise Exception('Not a dictionary, please enter a dictionary')
        self.d = d
        
    def getDictKeys(self):
        return self.d.keys()
    
    def getDictValues(self):
        return self.d.values()
    
    def insertKeyValue(self, key, value):
        self.d[key] = value
        
class Car1:
    def __init__(self, body_type, engine, fuel_type):
        # Self is just a convention to take a pointer as the first argument of the function
        # Self acts as aa pointer to the class NOTHING MUCH. Self is not a keyword REMEMBER
        # Init is like a constructor
        self.body_type = body_type
        self.engine = engine
        self.fuel_type = fuel_type

    def test(self):
        print("This is my first method in car class", self.engine)

    def isPetrol(self):
        return self.fuel_type != 'Diesel'

    def mileage(self):
        if self.isPetrol():
            return "15-25 KMPL"
        return "16-30 KMPL"