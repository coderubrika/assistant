from dotenv import dotenv_values
import os

__mode = os.getenv('PY_ENV')
__config = dotenv_values(f"{__mode}.env")

model_path = __config['model_path']