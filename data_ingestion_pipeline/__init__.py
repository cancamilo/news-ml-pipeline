import os
import sys


root = os.path.abspath(os.path.dirname(__file__))
print("Init data ingestion pipeline", root)
sys.path.insert(0, root)