import time


class HotelOutputResult:

    def __init__(self):
        ts = time.time()
        self.file_output_pointer=open(str(ts)+"__result.csv","w")
        self.write_line_csv("hotel name,Booking.com link,Valid record,Current hotel name,Hotel review")

    def write_line_csv(self, out_put_obj):
        self.file_output_pointer.write(str(out_put_obj)+"\n")

    def close_file(self):
        self.file_output_pointer.close()
