# 5/21/2019
# Written by Corey Stone

# A script that reads from the LinkedIn CSV for finding potential clients,
# (soon to be) providing a GUI to facilitate finding and marking off members.
import csv
import pandas as pd

class LinkedIn():
#    CSV_PATH = 'write_script.csv'

    def __init__(self):
        self.path = str()
        self.row_number = 0
        self.table = pd.read_csv(LinkedIn.CSV_PATH)
        self.status = self.table['Added'].values.tolist()
        self.names = self.table['Full Name'].values.tolist()
        self.companies = self.table['Primary Company'].values.tolist()
        self.company_types = self.table['Primary Company Type'].values.tolist()
        self.positions = self.table['Primary Position'].values.tolist()
        self.path = str()

        self.max_rows = len(self.table)


    # --- Save only columns ---
    # 1. Full Name
    # 2. Primary Company
    # 3. Primary Company Type
    # 4. Primary Position


    def get_persons(self):
        result = []
        for ind, row in enumerate(zip(self.names, self.companies, self.company_types, self.positions)):
            result.append(row)
        return result

    def write_found(self):
        self.table.set_value(self.row_number - 2, 'Added', 'X')
        self.table.to_csv(self.path, index=False)


    def write_not_found(self):
        self.table.set_value(self.row_number - 2, 'Added', 'Not Found')
        self.table.to_csv(self.path, index=False)