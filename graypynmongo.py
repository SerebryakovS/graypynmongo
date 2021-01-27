#!/usr/bin/python3


import graypy
import logging
from pymongo import MongoClient
# https://docs.mongodb.com/manual/reference/operator/aggregation/
mydb_name = "pymongobd_usage";
client = MongoClient("mongodb://localhost:27017");
if mydb_name in client.list_database_names():
    client.drop_database(mydb_name);
    print("database has been dropped");
dtbase = client[mydb_name];
countries = dtbase["countries"];
one_country_data = \
    { "country_name" : "Mongolia"  ,"off_language"  : "Mongolian", "million_sq_km" :  1.55};
insert_result = countries.insert_one(one_country_data);
print('single insertion: {0}\n'.format(insert_result.inserted_id));
countries_data = [
    { "country_name" : "Russia"    ,"off_language"  : "Russian"  , "million_sq_km" : 16.38},
    { "country_name" : "Canada"    ,"off_language"  : "English"  , "million_sq_km" :  9.09},
    { "country_name" : "Australia" ,"off_language"  : "English"  , "million_sq_km" :  7.68},
    { "country_name" : "China"     ,"off_language"  : "Mandarin" , "million_sq_km" :  9.33},
    { "country_name" : "Kazakhstan","off_language"  : "Kazakh"   , "million_sq_km" :  2.70}];
insert_result = countries.insert_many(countries_data);
print('multiple insertion: {0}\n'.format(insert_result.inserted_ids));
print('------------------------------------------------------------');
eng_lang = countries.find({"off_language"  : "English"});
print('countries found: {0}\n'.format(eng_lang.count()));
for country in eng_lang: 
    print(country);
# Field Update Operators!!!
countries.update({"country_name":"Russia"}, {"$set": { "million_sq_km": 16.37 }})
print(countries.find_one({"country_name":"Russia"}));
countries.update({"country_name":"Russia"}, {"$inc": { "million_sq_km": 10.00 }})
print(countries.find_one({"country_name":"Russia"}));
print('------------------------------------------------------------');
myquery = { "million_sq_km": { "$gt": 7.00 } };
for country in countries.find(myquery):
    print(country)
    
my_logger = logging.getLogger("test_logger")
handler = graypy.GELFUDPHandler("monitoring.igor.kz", 5555)
handler.facility = "stepan";
handler.level_names = True;
my_adapter = logging.LoggerAdapter(logging.getLogger('test_logger'),{'username': 'Stepan'})
my_logger.addHandler(handler);
#my_logger.setLevel(logging.WARNING);
#my_logger.setLevel(logging.INFO);
#my_logger.setLevel(logging.ERROR);
#my_logger.setLevel(logging.DEBUG);

c_begin_countries = countries.find({"country_name":{"$regex":"^C"}});
if (c_begin_countries.count() > 1):
    my_logger.setLevel(logging.INFO);
    my_logger.info('several countires were found');









