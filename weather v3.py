import csv
import plotly as plt
import plotly.graph_objs as graf

# Extract the month from a date string e.g. '01/02/1988 05:00' will return 2
def getMM(dateStr):
    return int(dateStr[3:5])


with open('weather data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    monthly_avg_temps = []
    total_temp = 0
    prev_month = 1
    number_of_readings = 0
    
    for row in csv_reader:

        this_month = getMM(row[0])
        if this_month == prev_month:
            number_of_readings = number_of_readings + 1
            total_temp = total_temp + float(row[4])
        else:
            # save the average temperature for the month
            monthly_avg_temps.append(total_temp/number_of_readings)
            # The month has changed so reset the total to be the first temp reading of the next month 
            total_temp = float(row[4])
            # reset the number of readings to one
            number_of_readings = 1

        # save the value of this month
        prev_month = this_month

    monthly_avg_temps.append(total_temp/number_of_readings)


# Create an populate a list of values for the x-axis
months = []
for i in range(len(monthly_avg_temps)):
    months.append(i)

# Compute annual averages
annual_avg_temps = []
total_temp = 0
for i in range(1, len(monthly_avg_temps)+1):
    if i%12 == 0:
        for j in range(13):
            annual_avg_temps.append(total_temp/12)
        total_temp = 0
    else:
        total_temp += monthly_avg_temps[i-1]
        

# plot both sets of data  
plotData1 = graf.Scatter(name = "Monthly Averages", x = months, y = monthly_avg_temps)
plotData2 = graf.Scatter(name = "Annual Averages", x = months, y = annual_avg_temps)
plotData = [plotData1, plotData2]
layoutSettings = graf.Layout(title = "Temperature Data")
plt.offline.plot(plotData, filename='Hourly.html')


'''
#plot the data  
plotData = graf.Scatter(name = "model1", x = months, y = monthly_avg_temps)
layoutSettings = graf.Layout(title = "Temperature Data")
plt.offline.plot({
    "data" : [plotData],
    "layout" : layoutSettings  })
'''
