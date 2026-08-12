

import os
from assistant.logger import get_logger
from assistant import config
logger = get_logger(__name__)

def check_tracing():
    """
    Check if tracing is enabled in the current environment.

    Returns:
        bool: True if tracing is enabled, False otherwise.
    """
    logger.info("Checking if tracing is enabled...")
    tracing = os.getenv('LANGSMITH_TRACING').lower() == 'true'

    if tracing=='true' and config.LNGSMITH_API_KEY:
        logger.info("Tracing is enabled.")
    else:
        logger.info("Tracing is not enabled.plz turn it on")

    

    
    # This function should check the environment or configuration to determine if tracing is enabled
    return False