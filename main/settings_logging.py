import os


LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING')
HANDLER = ['console']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'production': {
            'format': '{asctime} {name} {levelname} - In {pathname} function {funcName} line {lineno} - {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'production',
        },
    },
    'loggers': {
        'root': {
            'handlers': HANDLER,
            'level': LOG_LEVEL,
        },
        'django': {
            'handlers': HANDLER,
            'level': LOG_LEVEL,
        },
        'django.request': {
            'handlers': HANDLER,
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
