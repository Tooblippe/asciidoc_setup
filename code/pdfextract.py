import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool  # <1>


pool = ThreadPool(16)

files = !ls /Users/tobie/Documents/johan_pdf/*.pdf
files = files[2:-1]

def pt(filename):
    a = !pdf2txt.py $filename			# <2>
    for j,i in enumerate(a):			# <3>
        if "ACCOUNT MONTH" in i:		# <4>
                print filename, a[j+2]	# <5>
                return a[j+2]			# <6>
                
results = pool.map(pt, files)			# <7>

df = pd.DataFrame( {'filename':files,'month':results})
df.to_excel('/Users/tobie/Documents/johan_pdf/dates_1st_pass.xls')