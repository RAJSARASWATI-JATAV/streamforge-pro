"""Advanced Logger"""
import logging
from pathlib import Path

def setup_logger(name="streamforge", log_file="streamforge.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    Path("logs").mkdir(exist_ok=True)
    
    fh = logging.FileHandler(f"logs/{log_file}")
    fh.setLevel(logging.INFO)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger
