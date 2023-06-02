class ParkingLot:
    def __init__(self, small, medium, big):
        self.small_slots = [None] * small
        self.medium_slots = [None] * medium
        self.big_slots = [None] * big
        self.car_mapping = {}
        self.revenue = 0

    def add_car(self, registration_number, car_type):
        if car_type == "small":
            if None in self.small_slots:
                slot_index = self.small_slots.index(None)
                self.small_slots[slot_index] = registration_number
                self.car_mapping[registration_number] = ("small", slot_index)
                print("Car parked successfully!")
            else:
                print("No available small slots.")
        elif car_type == "medium":
            if None in self.medium_slots:
                slot_index = self.medium_slots.index(None)
                self.medium_slots[slot_index] = registration_number
                self.car_mapping[registration_number] = ("medium", slot_index)
                print("Car parked successfully!")
            else:
                print("No available medium slots.")
        elif car_type == "big":
            if None in self.big_slots:
                slot_index = self.big_slots.index(None)
                self.big_slots[slot_index] = registration_number
                self.car_mapping[registration_number] = ("big", slot_index)
                print("Car parked successfully!")
            else:
                print("No available big slots.")
        else:
            print("Invalid car type.")

    def remove_car(self, registration_number):
        if registration_number in self.car_mapping:
            car_type, slot_index = self.car_mapping[registration_number]
            if car_type == "small":
                self.small_slots[slot_index] = None
            elif car_type == "medium":
                self.medium_slots[slot_index] = None
            elif car_type == "big":
                self.big_slots[slot_index] = None
            del self.car_mapping[registration_number]
            print("Car removed successfully!")
        else:
            print("Car not found.")

    def get_car_details(self, registration_number):
        if registration_number in self.car_mapping:
            car_type, _ = self.car_mapping[registration_number]
            print(f"Car Type: {car_type}")
            print(f"Entry Time: {self.get_entry_time(registration_number)}")
            if self.is_car_parked(registration_number):
                print("Exit Time: Not available")
            else:
                print("Exit Time: Not applicable")
        else:
            print("Car not found.")

    def get_available_slots(self):
        available_slots = {
            "small": self.small_slots.count(None),
            "medium": self.medium_slots.count(None),
            "big": self.big_slots.count(None),
        }
        return available_slots

    def get_occupied_slots(self):
        occupied_slots = {
            "small": len(self.small_slots) - self.small_slots.count(None),
            "medium": len(self.medium_slots) - self.medium_slots.count(None),
            "big": len(self.big_slots) - self.big_slots.count(None),
        }
        return occupied_slots

    def get_parked_cars(self):
        parked_cars = []
        for registration_number, (car_type, _) in self.car_mapping.items():
            parked_cars.append({"car_type": car_type, "registration_number": registration_number})
        return parked_cars

    def get_total_revenue(self):
        return self.revenue

    def get_entry_time(self, registration_number):
        
        return "09:00 AM"

    def is_car_parked(self, registration_number):
        return registration_number in self.car_mapping

