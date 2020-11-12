import os
import pymongo


user = os.environ.get('MONGOUSER')
password = os.environ.get('MONGOPASSWORD')

myclient = pymongo.MongoClient(
    f'mongodb+srv://{user}:{password}@cluster0.r3yxj.mongodb.net/booking-db?retryWrites=true&w=majority')
booking_schema = myclient['booking-db']['booking-schema']


def add_unit(data):
    """Add a unit"""
    new_unit = {'_id': data['_id'].upper(), 'booker': data['booker'],
                'comment': data['comment'], 'date': data['date']}
    result = booking_schema.insert_one(new_unit)
    return result.inserted_id


def delete_unit(unit_id):
    """Delete a unit"""
    result = booking_schema.delete_one({'_id': unit_id.upper()})
    return result.deleted_count


def empty_unit(unit_id):
    """Delete all information but the _id for the specified unit"""
    empty_data = {'$set': {'booker': ' ', 'comment': ' ', 'date': ' '}}
    return booking_schema.update_one({'_id': unit_id.upper()}, empty_data).matched_count


def find_all_units():
    """Find all units"""
    result = []
    for unit in booking_schema.find():
        result.append(unit)
    return result


def find_unit(unit_id):
    """Find specific unit"""
    return [booking_schema.find_one({'_id': unit_id.upper()})]


def update_unit(data):
    """Update specified unit"""
    data_copy = data.copy()
    id = data_copy.pop('_id')
    new_data = {'$set': data_copy}
    return booking_schema.update_one({'_id': id.upper()}, new_data).matched_count


if __name__ == "__main__":
    print(delete_unit('a'))
    print(add_unit({'_id': 'a', 'booker': 'b', 'comment': 'c', 'date': 'd'}))
    print(delete_unit('a'))
