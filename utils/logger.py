"""
This module  designed for configure logger.
"""

import logging.config
import sys


default_logconfig = {

    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-22s %(levelname).1s,[%(module)s, line %(lineno)d, in %(funcName)s]:-8s %(message)s',
            'datefmt': '%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        '2file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'logs/confluence2queue.log',  # Default is stderr
        },
    },
    'loggers': {
        '': {  # root logger
            # 'handlers': ['default'],
            'handlers': ['default', '2file'],
            'level': 'INFO',
            'propagate': True
        },
        # 'confluence_2_sdk': {
        #     # 'handlers': ['default'],
        #     'handlers': ['default', '2file'],
        #     'level': 'INFO',
        #     'propagate': True
        # },
    }
}


def init_logger(method='default'):
    """
    Initialize logger.
    :param method: Method name.
    :return:
    """
    logging.config.dictConfig(default_logconfig)
    logger = logging.getLogger(method)
    return logger
