import csv

class StocklistParser(object):

    def __init__(self, csv_file, constraint_country=None, constraint_exchange=None, constraint_industry=None):
        self.csv_file = csv_file
        self.const_co = constraint_country
        self.const_ex = constraint_exchange
        self.const_ind = constraint_industry

        self.sl_symbols = []
        self.sl_names = []
        self.sl_inds = []
        self.sl_cos = []
        self.sl_exs = []

        self.parse_csv()

    def parse_csv(self):
        f = open(self.csv_file, 'r')
        reader = csv.reader(f)
        for row in reader:
            flag_include = True
            if self.const_ind:
                if row[2].upper() != self.const_ind.upper(): flag_include = False
            if self.const_co:
                if row[3].upper() != self.const_co.upper(): flag_include = False
            if self.const_ex:
                if row[4].upper() != self.const_ex.upper(): flag_include = False

            if flag_include:
                self.sl_symbols.append(row[0])
                self.sl_names.append(row[1])
                self.sl_inds.append(row[2])
                self.sl_cos.append(row[3])
                self.sl_exs.append(row[4])

    def get_symbols(self):
        return self.sl_symbols

    def get_company_names(self):
        return self.sl_names

    def get_industries(self):
        return self.sl_inds

    def get_countries(self):
        return self.sl_cos

    def get_exchanges(self):
        return self.sl_exs