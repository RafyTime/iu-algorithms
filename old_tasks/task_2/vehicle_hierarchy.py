from dataclasses import dataclass


@dataclass
class Vehicle:
    make: str
    model: str
    number_of_wheels: int

    def start(self):
        pass

    def stop(self):
        pass


@dataclass
class PassengerVehicle(Vehicle):
    passenger_capacity: int

    def board(self, passengers: int):
        pass

    def offboard(self, passengers: int):
        pass


@dataclass
class Motorcycle(PassengerVehicle):
    number_of_wheels: int = 2
    passenger_capacity: int = 2


@dataclass
class Car(PassengerVehicle):
    number_of_wheels: int = 4


@dataclass
class Sedan(Car):
    passenger_capacity: int = 5


@dataclass
class Convertible(Car):
    passenger_capacity: int = 2
    is_roof_open: bool = False

    def toggle_roof(self, is_roof_open: bool):
        pass


@dataclass
class UtilityVehicle(Vehicle):
    payload_capacity: int
    utility_type: str

    def load(self, payload: int):
        pass

    def unload(self, payload: int):
        pass


@dataclass
class Truck(UtilityVehicle):
    utility_type: str = "truck"
    cargo_type: str
    has_trailer: bool = False

    def toggle_trailer(self, has_trailer: bool):
        pass


@dataclass
class FireEngine(UtilityVehicle):
    utility_type: str = "fire engine"
    is_ladder_open: bool = False
    water_capacity: int

    def fill_water(self, water_amount: int):
        pass

    def drain_water(self, water_amount: int):
        pass

    def spray_water(self, water_amount: int):
        pass

    def toggle_ladder(self, is_ladder_open: bool):
        pass
