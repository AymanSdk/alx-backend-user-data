#!/usr/bin/python3
"""A Module for filtering and logging messages.
"""
import os
import re
import logging
import mysql.connector
from typing import List

patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """Filters a log line.
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


def get_logger() -> logging.Logger:
    """Returns a logging object.
    """
    logger = logging.getLogger('user_data')
    stream_handler = logging.setFormatter(RedactingFormatter(PII_FIELDS))
    stream_handler.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


if __name__ == "__main__":
    main()
