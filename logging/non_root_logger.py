import logging

# This will configure the root logger which is configured only once
# If you configure it somewhere else, that will not be effective/executed
# logging.basicConfig(level=logging.WARNING)

# So we do not create root logger, instead we create individual logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
fh = logging.FileHandler('basic.log')
fh.setFormatter(f)
logger.addHandler(fh)

logger.info("This is info log")