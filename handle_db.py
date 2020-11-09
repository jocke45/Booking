import os
import pymongo


user = os.environ.get("MONGOUSER")
password = os.environ.get("MONGOPASSWORD")

myclient = pymongo.MongoClient(
    f'mongodb+srv://{user}:{password}@cluster0.r3yxj.mongodb.net/booking-db?retryWrites=true&w=majority')
booking_schema = myclient['booking-db']['booking-schema']


def add_data(data):
    """Used for adding a store"""
    new_store = {"_id": data[0], "booker": data[1], "comment": data[2]}
    result = booking_schema.insert_one(new_store)
    return result.inserted_id


def find_store(store_id):
    """Used for finding one specific store"""
    return [booking_schema.find_one({"_id": store_id.upper()})]


def find_all_stores():
    """Used for finding all stores"""
    result = []
    for store in booking_schema.find():
        result.append(store)
    return result


def update_store(data):
    new_data = {"$set": {"booker": data[1], "comment": data[2]}}
    return booking_schema.update_one({"_id": data[0].upper()}, new_data).matched_count
    


if __name__ == "__main__":
    print(find_store('UNIT01'))
    print(update_store(['UNIT01', 'någon', 'gfd']))
    print(find_store('UNIT01'))
    #print(find_all_stores())

