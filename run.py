import os
try: import tqdm
except:
    os.system(f"python3 -m pip install -r requirements.txt")

from cypherV2_fixed import ParamGenerater
import time
import sys

import argparse

banner = f"""
--------------------------------------------------------
 ______     __     ______     __   __     ______    
/\  ___\   /\ \   /\  ___\   /\ "-.\ \   /\  ___\   
\ \___  \  \ \ \  \ \ \__ \  \ \ \-.  \  \ \ \____  
 \/\_____\  \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\ 
  \/_____/   \/_/   \/_____/   \/_/ \/_/   \/_____/ 
                                                                                           
-----------------------------------------by LongUwU-----
"""

cp = ParamGenerater()
    
if __name__ == "__main__":
    print(banner)
    parser = argparse.ArgumentParser(description="idk write what in here :)))")
    parser.add_argument("mode", choices=["cp", "sign", "unsign"], help="cp is Create Param, for generate parameters, \n sign for start SignCrypt, \n unsign for start Un-SignCrypt (DeCrypt)")
    parser.add_argument('-b', '--bit', type=int, help="bit to generate Q in Param (default: 64)", default="64")
    args = parser.parse_args()
    
    if args.mode == "cp":
        print("now at generate parameter mode!")
        cp.run(args.bit)
    if args.mode == "sign":
        print("now at sign mode!")
        # sign.run(args.inpF)
    if args.mode == "unsign":
        print("now at unSign mode!")
        # unsign.run()

