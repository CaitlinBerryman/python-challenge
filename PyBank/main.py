# import modules
import os
import csv

# file path
csvpath = os.path.join("Resources", "budget_data.csv")

# read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip header
    next(csvreader,None)

    # month count
    months = 0

    # total count
    nettotal = 0

    #create list to store profit change between months, calculate average monthly change
    monthchange_list = []

    #store previous row's profit for calculating change between months
    prev = 0

    # def average function
    def average(monthchange):
        length = len(monthchange_list)
        changetotal = 0
        for num in monthchange_list:
            changetotal += num
        return changetotal / length
    
    # value of greatest profit and loss, rows below store month/year
    maxchangeval = 0
    minchangeval = 0


    for row in csvreader:
        # increase month count
        months = months + 1

        # new profit
        profit = int(row[1])

        # add to net total
        nettotal = nettotal + profit

        #calcluate monthly change and add it to list
        monthchange = profit - prev
        monthchange_list.append(monthchange)

        # new previous value
        prev = profit

        # check if new min/max values found
        if monthchange > maxchangeval:
            maxchangeval = monthchange
            maxchangerow = str(row[0])
        if monthchange < minchangeval:
            minchangeval = monthchange
            minchangerow = str(row[0])

    # remove the first value, which has no previous month and thus messes up the average
    monthchange_list.pop(0)
    
    print("Financial Analysis")
    print("-----------------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${nettotal}")
    print(f"Average Change: ${round(average(monthchange),2)}")
    print(f"Greatest Increase in Profits: {maxchangerow} (${maxchangeval})")
    print(f"Greatest Decrease in Profits: {minchangerow} (${minchangeval})")

# export results to txt    
output_path = os.path.join("analysis", "output.txt")

# w for write, \n for new line
with open(output_path, "w") as txt:
    txt.write("Financial Analysis")
    txt.write("\n")
    txt.write("-----------------------------------------------")
    txt.write("\n")
    txt.write(f"Total Months: {months}")
    txt.write("\n")
    txt.write(f"Total: ${nettotal}")
    txt.write("\n")
    txt.write(f"Average Change: ${round(average(monthchange),2)}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: {maxchangerow} (${maxchangeval})")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: {minchangerow} (${minchangeval})")

