from model.hotel_struct_input import HotelStructInput


class HotelStructOutput(HotelStructInput):

    def __init__(self, hotel_name, hotel_url,
                 current_hotel_name, hotel_review):
        super().__init__(hotel_name, hotel_url)
        self.current_hotel_name = current_hotel_name
        self.hotel_review = hotel_review
        self.add_validity()

    def add_validity(self):



        if not str(self.hotel_url).startswith("https://www.booking.com") or \
                (self.current_hotel_name is None and self.hotel_review is None):
            self.valid_record = "Invalid URL"
            self.current_hotel_name = 'N/A'
            self.hotel_review = 'N/A'
        elif not (str(self.current_hotel_name).replace("Hotel ", "")) == self.hotel_name:
            self.valid_record = "Invalid hotel name"
        else:
            self.valid_record = "Valid"

    def __repr__(self):

        print(" , ".join([self.hotel_name,
                         self.hotel_url,
                         self.valid_record,
                         self.current_hotel_name,
                         self.hotel_review]))

        return self.hotel_name+","+\
                         self.hotel_url+","+\
                         self.valid_record+","+\
                         self.current_hotel_name+","+\
                         self.hotel_review

