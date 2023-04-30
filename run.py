# import os
# try: import tqdm
# except:
#     os.system(f"python3 -m pip install -r requirements.txt")

from cypherV2_fixed import ParamGenerater, Sign, unSign
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
sign = Sign()
unsign =unSign()
    
if __name__ == "__main__":
    print(banner)
    parser = argparse.ArgumentParser(description="idk write what in here :))))")
    # parser.add_argument("mode", choices=["cp", "sign", "unsign"], help="cp is Create Param, for generate parameters, \n sign for start SignCrypt, \n unsign for start Un-SignCrypt (DeCrypt)")
    commands = parser.add_subparsers(dest="command")
    # tạo group cho lệnh tạo tham số
    cp_parser = commands.add_parser("cp", help="generate keys")
    cp_parser.add_argument('-b', '--bit', dest="bit", type=int, help="bit to generate Q in Param (default: 64)", default=64)
    
    # tạo group cho lệnh sign
    sign_parser = commands.add_parser("sign", help="signCrypt file")
    sign_parser.add_argument('-i', '--input', dest="sign_in", type=str, help="input file for sign")
    sign_parser.add_argument('-o', '--output', dest="sign_out", type=str, help="output PATH for signed file and r,s signature (default: ./c.r.s/)", default="./c.r.s")

    # tạo group cho lệnh unSign
    unsign_parser = commands.add_parser("unsign", help="unSigncrypt Signed file")
    unsign_parser.add_argument('-i', '--input', dest="unsign_in", type=str, help="input FILE for unSignCryption", default="./c.r.s")
    unsign_parser.add_argument('-o', '--output', dest="unsign_out", type=str, help="output PATH for unSignCryption")
    
    args = parser.parse_args()
    print(args)
    if args.command == "cp":
        print("now at generate parameter mode!")
        cp.run(args.bit)
    if args.command == "sign":
        print("now at sign mode!")
        sign.run(args.sign_in, args.sign_out)
    if args.command == "unsign":
        print("now at unSign mode!")
        unsign.run(args.unsign_in, args.unsign_out)
        # print(args.unsign_in, args.unsign_out)

