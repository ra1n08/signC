# Usage
run "python3 run.py -h" to show help
# For Generate new param
run "python3 run.py cp -b [bits, ex: 160] (if you not use -b so default is 64 bits)
# For Signing a text file
run "python3 run.py sign -i [text file path] -o [output path]" 
# For un-Signing signed file
run "python3 run.py unsign -i [path of folder contain signed text file and signature files] -o [output of file un-Signed (decrypted)]"