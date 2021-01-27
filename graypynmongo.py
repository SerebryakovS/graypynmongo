#!/usr/bin/python3


import graypy
import logging
from pymongo import MongoClient

mydb_name = "pymongobd_usage";
client = MongoClient("mongodb://localhost:27017");
if mydb_name in client.list_database_names():
    client.drop_database(mydb_name);
    print("database has been dropped");
dtbase = client[mydb_name];
countries = dtbase["countries"];
one_country_data = \
    { "country_name" : "Mongolia"  ,"off_language"  : "Mongolian", "million_sq_km" :  "1.55"};
insert_result = countries.insert_one(one_country_data);
print('single insertion: {0}'.format(insert_result.inserted_id))
countries_data = [
    { "country_name" : "Russia"    ,"off_language"  : "Russian"  , "million_sq_km" : "16.38"},
    { "country_name" : "Canada"    ,"off_language"  : "English"  , "million_sq_km" :  "9.09"},
    { "country_name" : "Australia" ,"off_language"  : "English"  , "million_sq_km" :  "7.68"},
    { "country_name" : "China"     ,"off_language"  : "Mandarin" , "million_sq_km" :  "9.33"},
    { "country_name" : "Kazakhstan","off_language"  : "Kazakh"   , "million_sq_km" :  "2.70"}];
insert_result = countries.insert_many(countries_data);
print('multiple insertion: {0}'.format(insert_result.inserted_ids))




exit();

my_logger = logging.getLogger("test_logger")
my_logger.setLevel(logging.DEBUG)


handler = graypy.GELFUDPHandler("monitoring.igor.kz", 5555)
handler.facility = "stepan";


my_logger.extra_fields = True
my_logger.level_names = True
my_adapter = logging.LoggerAdapter(logging.getLogger('test_logger'),{'username': 'Stepan'})

my_logger.addHandler(handler)

my_logger.debug('custom_logging_level')
