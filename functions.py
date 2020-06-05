def createFlightFolder():
    # Create new folder to store all flight data in
    currentDir = os.path.dirname(__file__)
    flightName = rocket.name + '-' + \
        date.strftime('%m.%d.%y') + '-' + time.strftime('%H:%M')
    flightPath = './Flights/' + flightName
    os.mkdir(flightPath)

    # currentDir + '/' +


def createCSV():
    # Create CSV to store raw flight data in
    with open('rawFlightData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["#", "Status", "accelX", "accelY", "accelZ",
                         "velocity", "altitude", "gyroX", "gyroY", "gyroZ"])
