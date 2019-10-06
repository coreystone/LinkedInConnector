# 5/21/2019
# Written by Corey Stone

# A script that reads from the LinkedIn CSV for finding potential clients,
# (soon to be) providing a GUI to facilitate finding and marking off members.
import csv
import os, glob
import pandas as pd

class LinkedIn():
#    CSV_PATH = 'write_script.csv'

    def __init__(self, path, template):
        print('PATH = ', path)
        print('template = ', template)

        if path == '':
            os.chdir('C:/Users/itadmin/PycharmProjects/LinkedIn Program')
            files = [file for file in glob.glob('*.csv')]
            if len(files) == 1:
                self.path = files[0]
            else:
                raise FileExistsError

        if os.path.exists(path):
            self.path = path

        else:
            raise FileNotFoundError

        self.template = template

    # --- Save only columns ---
    # 1. Full Name
    # 2. Primary Company
    # 3. Primary Company Type
    # 4. Primary Position


    def generate_pdtable(self):
        self.table = pd.read_csv(self.path)
        self.status = self.table['Added'].values.tolist()
        self.names = self.table['Full Name'].values.tolist()
        self.companies = self.table['Primary Company'].values.tolist()
        if self.template == 'Default':
            self.company_types = self.table['Primary Company Type'].values.tolist()
            self.positions = self.table['Primary Position'].values.tolist()

        self.max_rows = len(self.table)


    def get_persons(self):
        result = []
        if self.template == 'Default':
            for row in zip(self.names, self.companies, self.company_types, self.positions):
                result.append(row)
        else:
            for row in zip(self.names, self.companies):
                result.append(row)

        return result


    def write_found(self):
        self.table.set_value(self.row_number - 2, 'Added', 'X')
        self.table.to_csv(self.path, index=False)


    def write_not_found(self):
        self.table.set_value(self.row_number - 2, 'Added', 'Not Found')
        self.table.to_csv(self.path, index=False)