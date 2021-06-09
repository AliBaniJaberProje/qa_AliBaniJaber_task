from hotel_test_runner import HotelTestRunner

if __name__ == '__main__':
    runner = HotelTestRunner("Booking_Url_validation.csv")
    try:
        runner.start()
    except Exception as ex:
        print("gggg")

