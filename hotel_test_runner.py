from csv_parser import CSVParser
from hotel_test_result import HotelResultTest
from model.hotel_struct_output import HotelStructOutput
from hotel_info_collector import HotelInfoCollector


class HotelTestRunner:

    def __init__(self, input_file_name):
        self.csv_parser = CSVParser(input_file_name)
        self.hotel_info_collector = HotelInfoCollector()
        self.hotel_output = HotelResultTest()

    def start(self):
        for record in self.csv_parser.hotel_data:
            hotel_info = self.hotel_info_collector.\
                get_hotel_info(url=record.hotel_url)
            output_record = HotelStructOutput(hotel_name=record.hotel_name,
                                              hotel_url=record.hotel_url,
                                              current_hotel_name=hotel_info[0],
                                              hotel_review=hotel_info[1])
            self.hotel_output.write_line_csv(str(output_record))
        self.hotel_output.close_file()
