def averageCelsius(fReadings):
    """
    converts all the readings from Fahrenheit to Celsius. Then, it calculates
    the mean average of all the Celsius numbers.Time complexity is O(N).
    NOTE: Nested loops often give O(N^2) time BUT Nested loops that result in
    O(N^2) occur when each loop revolves around N"""
    celsiusNumbers = []
    for reading in fReadings:
        celsiusConversion = (reading - 32) / 1.8
        celsiusNumbers.append(celsiusConversion)

    sumOfCelsius = 0.0
    for number in celsiusNumbers:
        sumOfCelsius += number
    return sumOfCelsius / len(celsiusNumbers)
