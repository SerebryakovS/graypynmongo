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


posts = dtbase.posts;
post_data = {
        "author_name"   : "Stepan Serebryakov",
        "project_title" : "hello, mongoDB",
    };

result = posts.insert_one(post_data);
print("one post: {0}".format(result.inserted_id));


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
