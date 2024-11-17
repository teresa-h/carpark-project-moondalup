from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

moon_carpark = CarPark("moondalup", 100, log_file="moondalup.txt")
entry_sensor = EntrySensor(1, True, moon_carpark)
exit_sensor = ExitSensor(2, True, moon_carpark)
display = Display(1, moon_carpark, "Welcome to Moondalup", True)

for car in range(10):
    entry_sensor.detect_vehicle()
    print(display.message)
    print(f"Available bays: {moon_carpark.available_bays}")
for car in range(2):
    exit_sensor.detect_vehicle()
    print(f"Available bays: {moon_carpark.available_bays}")



