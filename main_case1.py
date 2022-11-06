import csv
from pathlib import Path
from pprint import pprint
from cases.case1.case_one import CaseOne

transactions1 = list(csv.reader(Path('files/transactions1.csv').open()))
transactions2 = list(csv.reader(Path('files/transactions2.csv').open()))

out1, out2 = CaseOne().reconcile_accounts(transactions1, transactions2)
pprint(out1)
print('\n')
pprint(out2)
