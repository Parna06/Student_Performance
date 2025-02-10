import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
import dill

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)  # ✅ Correct
        os.makedirs(dir_path, exist_ok=True)   # ✅ Now it works

        with open(file_path, "wb") as file:
            dill.dump(obj, file)

    except Exception as e:
        raise CustomException(e, sys)
