import yaml

class Generator(object):

    def parse(self, yml_file):
        with open(yml_file) as f:
            db = yaml.safe_load(f)
        return db

    def generate_sql_table(self, yml_file):
        db = self.parse(yml_file)
        tables = []
        for i in range(0, len(db)):
            table_name = db.keys()[i]
            tables.append('CREATE TABLE ' + table_name + ' (\n')
            tables[i] += ('    ' + table_name + '_id  : INT PRIMARY KEY,\n')
            table_fields = db.values()[i].values()
            table_fields_names = table_fields[0].keys()
            table_fields_type = table_fields[0].values()
            for k in range(0, len(table_fields_names)):
                tables[i] += ('    ' + table_name + '_' + table_fields_names[k] + ' : ' + table_fields_type[k] + ',\n')
            tables[i] += ')\n'
            tables[i] += '\n'
        return tables


if __name__ == '__main__':
    generator = Generator()
    sql_tables = generator.generate_sql_table('db.yml')
    for i in range(0, len(sql_tables)):
        print (sql_tables[i])
