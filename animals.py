from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


ANIMALS = {
    "Cat": {
        "name": "Misha",
        "age": "3",
        "timestamp": get_timestamp()
    },
    "Dog": {
        "name": "Peanut Butter",
        "age": "15",
        "timestamp": get_timestamp()
    },
    "Horse": {
        "fname": "BoJack",
        "age": "30",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    
    return [ANIMALS[key] for key in sorted(ANIMALS.keys())]