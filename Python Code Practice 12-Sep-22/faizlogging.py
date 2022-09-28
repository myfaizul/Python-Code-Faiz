import logging

logging.basicConfig(filename="d:\\faizlogging2.txt", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("Debug Message")

logger.info("Just an information")

logger.warning("Its a Warning")

logger.error("Some function not successfull")

logger.critical("Internet is down")