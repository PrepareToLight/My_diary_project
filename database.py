import datetime
import sqlite3

#common comands
# CREATE TABLE IF NOT EXISTS <table_name> (val1 type, val2 type, ...);
# INSERT INTO <table_name> (vals);

entries = []

def add_entries(text):
    current_time = datetime.datetime.now()
    data = {"content": text, "date": str(current_time)}
    entries.append(data) 

def view_entries():
    return entries

class DataBase:
    def __init__(self, title:str) -> None:
        self.title = title
        #if the file dosen't exists this command will create one
        self.connection = sqlite3.connect(self.title + ".db")
        #if it exists, than it will be just connected
        self.tables = {}

    def table_vals(self, dic_:dict) -> str:
        vals = ""
        for key in dic_:
            vals += str(key) + " " + str(dic_[key]).upper() + ", "

        return vals[:-2]    

    def create_table(self, table_name, VALS:dict) -> None:
        vals = self.table_vals(VALS)
        with self.connection:
            self.connection.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({vals})")
        self.tables[table_name + " num_VALS"] = len(VALS)

    def input_to_table(self, *INPUTS, table_name) -> None:
        with self.connection:
            self.connection.execute(f"INSERT INTO {table_name} VALUES {str(INPUTS)}")


    def close(self) -> None:
        self.connection.close()



