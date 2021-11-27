from room import Roommate,Hotel
roommate1=Roommate()
roommate2=Roommate()
hotel=Hotel()
hotel.calculate_rent(roommate1.total_time(),roommate2.total_time())
hotel.bill(roommate1.guest_name(),roommate2.guest_name())