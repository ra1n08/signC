import os
try: import tqdm
except:
    os.system(f"python3 -m pip install -r requirements.txt")

from cypherV2_fixed import ParamGenerater
import time
import sys

import argparse

app = ParamGenerater()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="signing a text file!")
    parser.add_argument('-b', '--bit', type=int, help="bit to generate Q in Param", default="64")
    args = parser.parse_args()
    
    app.run(args.bit)

