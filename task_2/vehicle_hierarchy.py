from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Vehicle(ABC):
    """Abstract base class for all vehicles"""

    make: str
    model: str
    number_of_wheels: int

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def honk(self) -> None:
        pass


@dataclass
class PassengerVehicle(Vehicle):
    """Abstract class for vehicles that carry passengers"""

    passenger_capacity: int

    def board(self, n: int) -> None:
        pass

    def alight(self, n: int) -> None:
        pass


@dataclass
class UtilityVehicle(Vehicle):
    """Abstract class for utility vehicles"""

    payload_volume_capacity: float  # in liters
    payload_weight_capacity: float  # in kilograms

    def load(self, weight_kg: float, volume_liters: float) -> None:
        pass

    def unload(self, weight_kg: float, volume_liters: float) -> None:
        pass


@dataclass
class Car(PassengerVehicle):
    """Abstract class for cars"""

    trunk_volume_liters: float
    doors: int
    number_of_wheels: int = field(default=4)

    def open_trunk(self) -> None:
        pass

    def close_trunk(self) -> None:
        pass


@dataclass
class Sedan(Car):
    """Sedan car implementation"""

    doors: int = field(default=4)
    passenger_capacity: int = field(default=5)
    trunk_volume_liters: float = field(default=500.0)


@dataclass
class Convertible(Car):
    """Convertible car implementation"""

    roof_type: str
    roof_open: bool = field(default=False)
    doors: int = field(default=4)
    passenger_capacity: int = field(default=4)

    def toggle_roof(self) -> None:
        pass


@dataclass
class Motorcycle(PassengerVehicle):
    """Motorcycle implementation"""

    has_sidecar: bool
    number_of_wheels: int = field(default=2)
    passenger_capacity: int = field(default=2)

    def kickstand_down(self) -> None:
        pass

    def kickstand_up(self) -> None:
        pass


@dataclass
class Truck(UtilityVehicle):
    """Abstract class for trucks"""

    towing_capacity_kg: float
    axles: int
    dual_rear_wheels: bool
    number_of_wheels: int = field(default=6)

    def attach_trailer(self) -> None:
        pass

    def detach_trailer(self) -> None:
        pass


@dataclass
class FireEngine(Truck):
    """Fire engine implementation"""

    water_capacity_liters: float
    has_ladder: bool
    sirens: bool

    def toggle_sirens(self) -> None:
        pass

    def toggle_water_pump(self) -> None:
        pass

    def toggle_ladder(self) -> None:
        pass
