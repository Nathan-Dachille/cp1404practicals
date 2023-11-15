"""Program for testing SilverServiceTaxi class."""

from silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi("Hummer", 100, fanciness=2)
print(silver_service_taxi)
silver_service_taxi.start_fare()
silver_service_taxi.drive(18)
print(silver_service_taxi)
print(f"Current fare: {silver_service_taxi.get_fare()}")

