# Task 2

a. Design a hierarchy of classes of vehicles based on the following information:

1. a vehicle class with the following fields: make, model, and number of wheels.
2. classes: PassengerVehicle, UtilityVehicle, FireEngine, Motorcycle, Cars, Trucks, Sedans, and Convertibles.

b. Describe the contents of each class and appropriate inheritance relations.

c. Describe another set of classes and inheritance hierarchy that could be defined for vehicles.

## Solution

### Part A & B: Main Vehicle Hierarchy

**Class Contents and Inheritance Relations:**

1. **Vehicle** (Base Class)
   - Fields: `make`, `model`, `number_of_wheels`
   - Purpose: Common attributes for all vehicles

2. **PassengerVehicle** (inherits from Vehicle)
   - Additional field: `number_of_seats`
   - Purpose: Vehicles designed to carry passengers

3. **UtilityVehicle** (inherits from Vehicle)
   - Additional field: `cargo_capacity`
   - Purpose: Vehicles designed for utility/work purposes

4. **Motorcycle** (inherits from Vehicle)
   - Fixed to 2 wheels, typically 1-2 seats
   - Purpose: Two-wheeled vehicle (distinct category)

5. **Car** (inherits from PassengerVehicle)
   - Additional field: `number_of_doors`
   - Fixed to 4 wheels
   - Purpose: Four-wheeled passenger vehicle

6. **Truck** (inherits from UtilityVehicle)
   - Additional field: `cargo_capacity`
   - Purpose: Utility vehicle for cargo transport

7. **FireEngine** (inherits from UtilityVehicle)
   - Additional field: `water_capacity`
   - Purpose: Specialized utility vehicle for firefighting

8. **Sedan** (inherits from Car)
   - Fixed to 4 doors, typically 5 seats
   - Purpose: Four-door car with separate trunk

9. **Convertible** (inherits from Car)
   - Fixed to 2 doors, typically 4 seats
   - Additional field: `roof_type`
   - Purpose: Car with retractable roof

**Inheritance Hierarchy:**
```
Vehicle
├── Motorcycle
├── PassengerVehicle
│   └── Car
│       ├── Sedan
│       └── Convertible
└── UtilityVehicle
    ├── Truck
    └── FireEngine
```

### Part C: Alternative Vehicle Hierarchy

**Alternative Classification Based on Propulsion Type and Environment:**

The alternative hierarchy classifies vehicles by:
1. **Propulsion Type**: Motorized vs Human-Powered
2. **Operational Environment**: Road, Off-Road, Water
3. **Specific Vehicle Types**: Motorcycle, Car, Truck, ATV, Boat, Bicycle

**Alternative Inheritance Hierarchy:**
```
Vehicle
├── MotorizedVehicle
│   ├── RoadVehicle
│   │   ├── Motorcycle
│   │   ├── Car
│   │   └── Truck
│   ├── OffRoadVehicle
│   │   └── ATV
│   └── WaterVehicle
│       └── Boat
└── HumanPoweredVehicle
    └── Bicycle
```

This alternative approach groups vehicles by their power source and operational environment rather than passenger/utility classification, providing a different perspective on vehicle categorization.