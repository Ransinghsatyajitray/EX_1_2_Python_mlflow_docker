from src.IrisData.components.data_ingestion import DataIngestion

import os
import sys
from sys.IrisData.logger import logging
from src.IrisData.exception import customexception
import pandas as pd

obj = DataIngestion()
obj.initiate_data_ingestion()