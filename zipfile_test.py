import os, zipfile

with zipfile.ZipFile(r'D:\Test', "w") as zf:
    zf.write('zip_name.zip')

