import os
import utils as ut

files = ["data/"+file for file in os.listdir("data")]

ut.write_file(map(ut.retrieve_info,files))

