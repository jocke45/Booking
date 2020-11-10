import os
import pymongo


user = os.environ.get("MONGOUSER")
password = os.environ.get("MONGOPASSWORD")

myclient = pymongo.MongoClient(
    f'mongodb+srv://{user}:{password}@cluster0.r3yxj.mongodb.net/booking-db?retryWrites=true&w=majority')
booking_schema = myclient['booking-db']['booking-schema']


def add_data(data):
    """Add a unit"""
    # TODO
    new_unit = {"_id": data[0].upper(), "booker": data[1], "comment": data[2]}
    result = booking_schema.insert_one(new_unit)
    return result.inserted_id


def find_unit(unit_id):
    """Find specific unit"""
    return [booking_schema.find_one({"_id": unit_id.upper()})]


def find_all_units():
    """Find all units"""
    result = []
    for unit in booking_schema.find():
        result.append(unit)
    return result


def update_unit(data):
    """Update specified unit"""
    data_copy = data.copy()
    id = data_copy.pop('_id')
    new_data = {"$set": data_copy}
    return booking_schema.update_one({"_id": id.upper()}, new_data).matched_count


if __name__ == "__main__":
    print(find_unit('UNIT01'))
