import  csv

csv_path = "python-challenge/PyBank/Resources/budget_data.csv"

#finding profit or loss and assigning to month

months = 0
total_profit = 0

is_first_row = True
last_month_profit = 0
changes = []

# Finding month with largest increase
max_change = -99999999999
max_month = ""

# Finding month with largest decrease
min_change = 999999999999999999
min_month = ""

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row) - this is to look at data

        row_profit = int(row[1])

        # check if first row (no change in first month but need to init last_month_profit)
        if is_first_row:
            last_month_profit = row_profit
            is_first_row = False
        else:
            change = row_profit - last_month_profit
            changes.append(change)

            # reset for the next month
            last_month_profit = row_profit

            # comparing current month profit/loss and determining if it's a greatest increase or decrease
            if change > max_change:
                 max_change = change
                 max_month = row[0]

            if change < min_change:
                min_change = change
                min_month = row[0]

        months += 1
        total_profit += int(row[1])

    print("**********************************************")
    print("============= Financial Analysis =============")
    print("Total Months: " + str(months))
    print("Total amount of Profit/Loss over " +str(months)+ " months: "+ str(total_profit))

    avg_changes = sum(changes) / len(changes)
    print("Average Profit/Loss change per month: " + str(avg_changes))

    print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_change)+ ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_change)+ ")")
