import requests
import json
import statistics


# old_ticker_list = ['AAPL', 'GOOG', 'ADBE', 'RIVN', 'RDDT', 'RKLB', 'SXC', 'DJT', 'LCID', 'SOUN']
ticker_list = ['ASPI', 'DMYY', 'GCT', 'RIVN', 'RDDT', 'RKLB', 'BLCO', 'DJT', 'LCID', 'SOUN']
# I had to get rid of some long running stocks because they took hours to run on bollinger bands


def initial_pull(ticker):
    file_location = '/home/ubuntu/environment/final_project/data/' + ticker + '.csv' # set the file path and name

    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    print("Pulling initial files from Web API into saved CSVs.")
    # print(url)
    file_request = requests.get(url)
    
    request_dictionary = json.loads(file_request.text)
    
    key1 = "Time Series (Daily)"
    key2 = '4. close'
    
    # Debug: print(request_dictionary)
    
    # for the initial pull, open the file for writing/overwriting
    csv_file = open(file_location, "w")
    
    # this list will hold the contents of the date and closing price in order to reverse the order
    working_list = []
    
    # loop through each date key in the dictionary and append the item to the working list
    for date in request_dictionary[key1]:
    	working_list.append(date + "," + request_dictionary[key1][date][key2] + "\n")
    
    working_list.reverse() # sort backwards
    # we want list sorted in date order so we can append new values to list

    csv_file.writelines(working_list) # writes the reverse sorted list back to file
    
    csv_file.close() # closes the file
    
def append_new_data(ticker):
    file_location = '/home/ubuntu/environment/final_project/data/' + ticker + '.csv' # set the file path and name

    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    # print(url)
    file_request = requests.get(url)
    
    request_dictionary = json.loads(file_request.text)
    
    key1 = "Time Series (Daily)"
    key2 = '4. close'
    
    # Debug: print(request_dictionary)
    
    # for the append pull, open the file for reading
    csv_file = open(file_location, "r")
    
    # read the csv into a list
    lines = csv_file.readlines()
    last_element_date = lines[-1].split(",")[0] # grabs the date (split[0]) of the last element (-1)
    
    # this list will hold the contents of the date and closing price in order to reverse the order
    working_list = []
    
    # loop through each date key in the dictionary and append the item to the working list
    for date in request_dictionary[key1]:
        if date == last_element_date:
            break
        working_list.append(date + "," + request_dictionary[key1][date][key2] + "\n")
        
    	
    
    working_list.reverse() # sort backwards
    # we want list sorted in date order so we can append new values to list
    
    # For the append action, open the file as "append"
    csv_file = open(file_location, "a")

    # write just the new rows to the end of the file
    csv_file.writelines(working_list) # writes the reverse sorted list back to file
    
    csv_file.close() # closes the file   
    
def convertFileToList(ticker):
    # this function takes a CSV file, opens it, and converts it into a list
    file_location = '/home/ubuntu/environment/final_project/data/' + ticker + '.csv'
    open_file = open(file_location, "r")
    lines_list = open_file.readlines()
    new_list = []
    for line in lines_list:
        # just grab the price
        price = line.split(",")[1].strip()
        new_list.append(float(price)) 
        # ok, this takes the item in the list, which looks like a string containing a date, a comma, and a price
        # first, it splits on the comma and takes the 2nd element, the price, strips off the newline character
        # and then converts that string into a float and appends that to the new list

    return new_list
    
    

def meanReversionStrategy(price_list, ticker):
    # initialize variables
    current_price = 0.00
    avg_5_days = 0.00
    first_buy = 0.00
    buy_it = 0.00
    sell_it = 0.00
    profit = 0.00
    final_profit_percentage = 0.00
    strategy_dictionary = {}
    prefix = "mr"
    

    # print("Mean Reversion Strategy Output:")
    
    # mean reversion strategy        
    for i in range(4, len(price_list)):
    # calculate the 5 day average
        avg_5_days = (price_list[i] + price_list[i-1] + price_list[i-2] + price_list[i-3] + price_list[i-4]) / 5.00
        if price_list[i] < (avg_5_days * 0.98) and buy_it == 0: # without checking the buy_it amount, it tries to keep buying
            buy_it = price_list[i] # buy if average is low
            #print(f"buying at:\t {buy_it}")
            # set first buy value the first time a buy is made
            if first_buy == 0:
                first_buy = buy_it
        elif price_list[i] > (avg_5_days * 1.02) and buy_it > 0: # can't sell if there's no buy amount!
            sell_it = price_list[i]
            profit += round((sell_it - buy_it), 2)
            #print(f"selling at:\t {sell_it}")
            #print(f"trade profit:\t {round((sell_it - buy_it), 2)}")
            # reset these variables after profit is added
            sell_it = 0
            buy_it = 0
        else:
            pass   

    # set final dictionary values
    if first_buy == 0:
        final_profit_percentage = 0
    else:        
        final_profit_percentage = round((( profit / first_buy ) * 100), 2) 
    strategy_dictionary[prefix + "_" + "strategy" + "_" + ticker] = "Mean Reversion"
    strategy_dictionary[prefix + "_" + "total_profit" + "_" + ticker] = round(profit,2)
    strategy_dictionary[prefix + "_" + "first_buy" + "_" + ticker] = first_buy
    strategy_dictionary[prefix + "_" + "final_profit_percentage" + "_" + ticker] = final_profit_percentage

    return strategy_dictionary
    # end mean reversion strategy

def simpleMovingAverageStrategy(price_list, ticker):
        # initialize variables
    current_price = 0.00
    avg_5_days = 0.00
    # price_list = [] #AUUUUGHHHHHH!!!!!! So much grief! this function originally read a text file and then converted it to this list
                      # but then when I switched to passing in the list, I forgot about this line, which wiped it out. Challenging bug.
    first_buy = 0.00
    buy_it = 0.00
    sell_it = 0.00
    profit = 0.00
    final_profit_percentage = 0.00
    strategy_dictionary = {}
    prefix = "sma"
    
    # print("Simple Moving Average Strategy Output:")
    
    # simple moving average strategy        
    for i in range(4, len(price_list)):
    # calculate the 5 day average
        avg_5_days = (price_list[i] + price_list[i-1] + price_list[i-2] + price_list[i-3] + price_list[i-4]) / 5.00
        if price_list[i] > (avg_5_days) and buy_it == 0: # without checking the buy_it amount, it tries to keep buying
            buy_it = price_list[i] # buy if current price is above 5 day average
            # print(f"buying at:\t {buy_it}")
            # set first buy value the first time a buy is made
            if first_buy == 0:
                first_buy = buy_it
        elif price_list[i] < (avg_5_days) and buy_it > 0: # can't sell if there's no buy amount!
            sell_it = price_list[i]
            profit += round((sell_it - buy_it), 2)
            # print(f"selling at:\t {sell_it}")
            # print(f"trade profit:\t {round((sell_it - buy_it), 2)}")
            # reset these variables after profit is added
            sell_it = 0
            buy_it = 0
        else:
            pass   

    if first_buy == 0:
        final_profit_percentage = 0.00
    else:
        final_profit_percentage = round((( profit / first_buy ) * 100), 2)   
        
    # set final dictionary values
    strategy_dictionary[prefix + "_" + "strategy" + "_" + ticker] = "Simple Moving Average"
    strategy_dictionary[prefix + "_" + "total_profit" + "_" + ticker] = round(profit,2)
    strategy_dictionary[prefix + "_" + "first_buy" + "_" + ticker] = first_buy
    strategy_dictionary[prefix + "_" + "final_profit_percentage" + "_" + ticker] = final_profit_percentage        

    # return 2 values, the profit and profit percentage
    # return round(profit, 2), final_profit_percentage
    return strategy_dictionary
    

def bollingerBandsStrategy(price_list, ticker):
        # initialize variables
    current_price = 0.00
    avg_5_days = 0.00
    first_buy = 0.00
    buy_it = 0.00
    sell_it = 0.00
    profit = 0.00
    final_profit_percentage = 0.00
    middle_band_list = []
    middle_band = 0.00
    upper_band = 0.00
    lower_band = 0.00
    stdev = 0.00
    strategy_dictionary = {}
    prefix = "bb"
    num_std_deviations = 1  # 2 is the recommended number, but that would require some high volatility
    
    # print("Bollinger Bands Strategy Output:")
    
   
    # bollinger bands strategy        
    for i in range(20, len(price_list)):
        for j in range(19, -1, -1):
            middle_band_list.append(price_list[i-j]) # put those 20 values into a list
        
        middle_band = statistics.mean(middle_band_list)
        stdev = statistics.stdev(middle_band_list)
        upper_band = middle_band + (num_std_deviations * stdev)
        lower_band = middle_band - (num_std_deviations * stdev)
        
        if price_list[i] <= lower_band and buy_it == 0:
            buy_it = price_list[i]
            if first_buy == 0:
                first_buy = buy_it
        elif price_list[i] >= upper_band and buy_it > 0:
            sell_it = price_list[i]
            profit += round((sell_it - buy_it), 2)
            sell_it = 0
            buy_it = 0
        else:
            pass
        if i % 100 == 0:
            print(f"On day {i}....")
        

    if first_buy == 0:
        final_profit_percentage = 0.00
    else:
        final_profit_percentage = round((( profit / first_buy ) * 100), 2)   
        
    # set final dictionary values
    strategy_dictionary[prefix + "_" + "strategy" + "_" + ticker] = "Bollinger Bands"
    strategy_dictionary[prefix + "_" + "total_profit" + "_" + ticker] = round(profit,2)
    strategy_dictionary[prefix + "_" + "first_buy" + "_" + ticker] = first_buy
    strategy_dictionary[prefix + "_" + "final_profit_percentage" + "_" + ticker] = final_profit_percentage        

    return strategy_dictionary



'''
# This step is commented out because running it doesn't allow the append data to run
# Step 1: pull all data and throw it into CSVs
for company in ticker_list:
    initial_pull(company)

'''
    
# Step 2: pull new data and append to files
print("Appending data from Web API to existing CSV files...")
for company in ticker_list:
    append_new_data(company)
    
print("Done appending data.")    
   

# initialize variables
price_list = [] 
results_dictionary = {}
sma_dictionary = {}
mr_dictionary = {}
bb_dictionary = {}
best_profit_percentage = 0.00
best_profit_strategy = ''
best_profit_ticker = ''

# Step 3: Run analyses
print("Preparing to run 3 analysis strategies...")
for company in ticker_list:
    print(f"Analyzing {company}'s stock")
# Debug: company = 'DJT'
    price_list = convertFileToList(company)
    
    # pulls results of analysis into a dictionary which the function returns
    sma_dictionary = simpleMovingAverageStrategy(price_list, company)
    mr_dictionary =  meanReversionStrategy(price_list, company)
    bb_dictionary =  bollingerBandsStrategy(price_list, company)
    
    # adds the results of each analysis into the final results
    results_dictionary.update(sma_dictionary)
    results_dictionary.update(mr_dictionary)
    results_dictionary.update(bb_dictionary)

print(f"Done running strategies for {company}.\n")
# to see the results
print("\nresults ", results_dictionary)

# browse through the final profits in the dictionary to find the one with the best return
for tick in ticker_list:
    for strat in ['sma', 'mr', 'bb']:
        profit_percentage = results_dictionary[strat + '_' + 'final_profit_percentage_' + tick]
        if profit_percentage >= best_profit_percentage:
            best_profit_percentage = profit_percentage
            best_profit_strategy = strat
            best_profit_ticker = tick
        else:
            pass
        
print(f"\nThe best strategy was {best_profit_strategy} on stock {best_profit_ticker} with a profit percentage of: {best_profit_percentage}")        

# convert the dictionary into JSON 
print("Writing results to file.")
# json.dumps(results_dictionary, open("results.json", "w"))
json_string = json.dumps(results_dictionary)

# write out the file and close it
file1 = open("/home/ubuntu/environment/final_project/results.json", "w") 
file1.write(json_string)
file1.close()
print("File write is complete.")



    
    