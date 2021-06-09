from model.hotel_struct_input import HotelStructInput
import csv



class CSVParser:
    def __init__(self,file_csv_name):
        self.file_csv_name=file_csv_name
        self.file_pointer=open(self.file_csv_name)
        self.hotel_data=[]
        self.load_data()

    def load_data(self):
        with open(self.file_csv_name, newline='\n') as csvfile:
            file_pointer = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in file_pointer:
                print(row[1])
                self.hotel_data.append(HotelStructInput(row[0], row[1]))
        self.hotel_data.pop(0)

    def colse_file(self):
        self.file_pointer.close()

    def is_next_valid(self):
        pass
    def get_next_row(self):
        pass


