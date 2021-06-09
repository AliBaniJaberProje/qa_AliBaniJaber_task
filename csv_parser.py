from model.hotel_struct_input import HotelStructInput
import csv


class CSVParser:

    def __init__(self,file_csv_name):
        self.file_csv_name=file_csv_name


    def load_data(self,procces_fun):
        try:
            with open(self.file_csv_name, newline='\n') as csvfile:
                file_pointer = csv.reader(csvfile, delimiter=',', quotechar='|')
                index=True
                for row in file_pointer:
                    if index:
                        index = False
                        continue
                    procces_fun(HotelStructInput(row[0], row[1]))
                    #self.hotel_data.append(HotelStructInput(row[0], row[1]))
                # self.hotel_data.pop(0)
        except:
            print(f" file  {self.file_csv_name}not found")
            exit(0)
