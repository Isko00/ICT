print("Enter fuel consumption in USA measurement: ")
fuelConsumptionInUSAMeasurement = float(input())
fuelConsumptionInCanadaMeasurement = fuelConsumptionInUSAMeasurement / 2.352
print("Fuel consumption: " + "%.2f" % fuelConsumptionInCanadaMeasurement 
		+ "L/100km")