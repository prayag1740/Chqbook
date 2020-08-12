import logging


class AppLogger(object):

    def __init__(self, logger_type="primary", tag=None):
        self.logger = logging.getLogger(logger_type)
        self.tag = tag

    def info(self, message, tag=None):
        if self.tag:
            self.logger.info("[%s] %s" % (self.tag, message))
        else:
            self.logger.info(message)

    def error(self, message, tag=None):
        if self.tag:

            self.logger.error("[%s] %s" % (self.tag, message))
        else:
            self.logger.error(message)

    def debug(self, message, tag=None):
        if self.tag:
            self.logger.debug("[%s] %s" % (self.tag, message))
        else:
            self.logger.debug(message)
