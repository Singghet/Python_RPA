# Singghet
import numpy as np
import os.path
import pandas as pd

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import pymysql


print(pd.__version__) # 打印pandas版本信息

