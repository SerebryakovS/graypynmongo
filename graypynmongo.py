import graypy
import logging


my_logger = logging.getLogger("test_logger")


my_logger.setLevel(logging.DEBUG)


handler = graypy.GELFUDPHandler("monitoring.igor.kz", 5555)
handler.facility = "stepan";

my_logger.extra_fields = True
my_logger.level_names = True
my_adapter = logging.LoggerAdapter(logging.getLogger('test_logger'),{'username': 'Stepan'})

my_logger.addHandler(handler)

my_logger.debug('custom_logging_level')
