"""
This is the animals module and supports all the ReST actions for the
animals collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
animals = {
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


def read_all():
    """
    This function responds to a request for /api/animals
    with the complete lists of animals
    :return:        json string of list of animals
    """
    # Create the list of animals from our data
    return [animals[key] for key in sorted(animals.keys())]


def read_one(age):
    """
    This function responds to a request for /api/animals/{age}
    with one matching person from animals
    :param age:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in animals?
    if age in animals:
        person = animals.get(age)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {age} not found".format(age=age)
        )

    return person


def create(person):
    """
    This function creates a new person in the animals structure
    based on the passed in person data
    :param person:  person to create in animals structure
    :return:        201 on success, 406 on person exists
    """
    age = person.get("age", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if age not in animals and age is not None:
        animals[age] = {
            "age": age,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{age} successfully created".format(age=age), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Peron with last name {age} already exists".format(age=age),
        )


def update(age, person):
    """
    This function updates an existing person in the animals structure
    :param age:   last name of person to update in the animals structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in animals?
    if age in animals:
        animals[age]["fname"] = person.get("fname")
        animals[age]["timestamp"] = get_timestamp()

        return animals[age]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {age} not found".format(age=age)
        )


def delete(age):
    """
    This function deletes a person from the animals structure
    :param age:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if age in animals:
        del animals[age]
        return make_response(
            "{age} successfully deleted".format(age=age), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {age} not found".format(age=age)
        )