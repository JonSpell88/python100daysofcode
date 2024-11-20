"""
Take 10 stocks and do a mean reversion strategy and simple moving average strategy
over the course of a year. 
Store the results in a dictionary, save the dictionary into a JSON file called results.json

Create a function called meanReversionStrategy which takes a list called “prices” as an argument.  
    The function runs a mean reversion strategy, and outputs to the console the buys and sells of the strategy (like you did in HW4).  
    The function returns the profit and final returns percentage.  
    
Create a function called simpleMovingAverageStrategy which takes a list called “prices” as an argument.  
    The function runs a Simple Moving Average strategy, and outputs to the console the buys and sells of the strategy.  The function returns the profit and final returns percentage.
    
Create a function called saveResults which takes a dictionary as an argument.  Save the dictionary to a json file called “results.json”.
"""
import json

# Step 1: read in the text files, open into a file variable
aapl_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/aapl.txt", "r")
adbe_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/adbe.txt", "r")
djt_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/djt.txt", "r")
goog_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/goog.txt", "r")
lcid_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/lcid.txt", "r")
rddt_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/rddt.txt", "r")
rivn_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/rivn.txt", "r")
rklb_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/rklb.txt", "r")
soun_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/soun.txt", "r")
sxc_file = open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/sxc.txt", "r")

# Step 2: read those objects into a list
aapl_lines = aapl_file.readlines()
adbe_lines = adbe_file.readlines()
djt_lines = djt_file.readlines()
goog_lines = goog_file.readlines()
lcid_lines = lcid_file.readlines()
rddt_lines = rddt_file.readlines()
rivn_lines = rivn_file.readlines()
rklb_lines = rklb_file.readlines()
soun_lines = soun_file.readlines()
sxc_lines = sxc_file.readlines()

# Step 2.5 : close the files now, we don't need them after Step 2
aapl_file.close()
adbe_file.close()
djt_file.close()
goog_file.close()
lcid_file.close()
rddt_file.close()
rivn_file.close()
rklb_file.close()
soun_file.close()
sxc_file.close()


# Step 3: define functions

def meanReversionStrategy(prices):
    # initialize variables
    current_price = 0.00
    avg_5_days = 0.00
    price_list = []
    first_buy = 0.00
    buy_it = 0.00
    sell_it = 0.00
    profit = 0.00
    final_profit_percentage = 0.00
    
    print("Mean Reversion Strategy Output:")
    
    for line in prices:

        current_price = line.strip() # removes excess spaces
        current_price = float(current_price) # changes it from a string to a float
        # current_price = round(current_price, 2) # round the price to 2 decimals
        price_list.append(current_price)
        
    # mean reversion strategy        
    for i in range(4, len(price_list)):
    # calculate the 5 day average
        avg_5_days = (price_list[i] + price_list[i-1] + price_list[i-2] + price_list[i-3] + price_list[i-4]) / 5.00
        if price_list[i] < (avg_5_days * 0.98) and buy_it == 0: # without checking the buy_it amount, it tries to keep buying
            buy_it = price_list[i] # buy if average is low
            print(f"buying at:\t {buy_it}")
            # set first buy value the first time a buy is made
            if first_buy == 0:
                first_buy = buy_it
        elif price_list[i] > (avg_5_days * 1.02) and buy_it > 0: # can't sell if there's no buy amount!
            sell_it = price_list[i]
            profit += round((sell_it - buy_it), 2)
            print(f"selling at:\t {sell_it}")
            print(f"trade profit:\t {round((sell_it - buy_it), 2)}")
            # reset these variables after profit is added
            sell_it = 0
            buy_it = 0
        else:
            pass   

    final_profit_percentage = round((( profit / first_buy ) * 100), 2)        
    print("-----------------------")
    print(f"Total profit: \t {round(profit,2)}")
    print(f"First buy: \t {first_buy}")
    print(f"Percent return:\t {final_profit_percentage}")

    # return 2 values, the profit and profit percentage
    return round(profit, 2), final_profit_percentage



def simpleMovingAverageStrategy(prices):
        # initialize variables
    current_price = 0.00
    avg_5_days = 0.00
    price_list = []
    first_buy = 0.00
    buy_it = 0.00
    sell_it = 0.00
    profit = 0.00
    final_profit_percentage = 0.00
    
    print("Simple Moving Average Strategy Output:")
    
    for line in prices:

        current_price = line.strip() # removes excess spaces
        current_price = float(current_price) # changes it from a string to a float
        # current_price = round(current_price, 2) # round the price to 2 decimals
        price_list.append(current_price)
        
    # mean reversion strategy        
    for i in range(4, len(price_list)):
    # calculate the 5 day average
        avg_5_days = (price_list[i] + price_list[i-1] + price_list[i-2] + price_list[i-3] + price_list[i-4]) / 5.00
        if price_list[i] > (avg_5_days) and buy_it == 0: # without checking the buy_it amount, it tries to keep buying
            buy_it = price_list[i] # buy if current price is above 5 day average
            print(f"buying at:\t {buy_it}")
            # set first buy value the first time a buy is made
            if first_buy == 0:
                first_buy = buy_it
        elif price_list[i] < (avg_5_days) and buy_it > 0: # can't sell if there's no buy amount!
            sell_it = price_list[i]
            profit += round((sell_it - buy_it), 2)
            print(f"selling at:\t {sell_it}")
            print(f"trade profit:\t {round((sell_it - buy_it), 2)}")
            # reset these variables after profit is added
            sell_it = 0
            buy_it = 0
        else:
            pass   

    final_profit_percentage = round((( profit / first_buy ) * 100), 2)        
    print("-----------------------")
    print(f"Total profit: \t {round(profit,2)}")
    print(f"First buy: \t {first_buy}")
    print(f"Percent return:\t {final_profit_percentage}")
    
    # return 2 values, the profit and profit percentage
    return round(profit, 2), final_profit_percentage


def saveResults(results_dictionary):
    json.dump(results_dictionary, open("/home/ubuntu/environment/DATA3500_FA_24/data3500/hw5/results.json", "w"))

'''        
ticker_list = ['aapl', 'adbe', 'djt', 'goog', 'lcid', 'rddt', 'rivn', 'rklb', 'soun', 'sxc']

for ticker in ticker_list:
    tick_line = ticker + '_lines'
    results_dict[ticker] = tick_line
# can't figure out how to make this part work so that it calls the function    
'''

# initialize the results dictionary
results_dict = {}

# because I couldn't make the ticker loop work, here are manual calls for each ticker
results_dict["aapl"] = aapl_lines
results_dict["aapl_mr_profit"], results_dict["aapl_mr_returns"] =  meanReversionStrategy(aapl_lines)
results_dict["aapl_sma_profit"], results_dict["aapl_sma_returns"] =  simpleMovingAverageStrategy(aapl_lines)

results_dict["adbe"] = adbe_lines
results_dict["adbe_mr_profit"], results_dict["adbe_mr_returns"] =  meanReversionStrategy(adbe_lines)
results_dict["adbe_sma_profit"], results_dict["adbe_sma_returns"] =  simpleMovingAverageStrategy(adbe_lines)


results_dict["djt"] = djt_lines
results_dict["djt_mr_profit"], results_dict["djt_mr_returns"] =  meanReversionStrategy(djt_lines)
results_dict["djt_sma_profit"], results_dict["djt_sma_returns"] =  simpleMovingAverageStrategy(djt_lines)

results_dict["goog"] = goog_lines
results_dict["goog_mr_profit"], results_dict["goog_mr_returns"] =  meanReversionStrategy(goog_lines)
results_dict["goog_sma_profit"], results_dict["goog_sma_returns"] =  simpleMovingAverageStrategy(goog_lines)

results_dict["lcid"] = lcid_lines
results_dict["lcid_mr_profit"], results_dict["lcid_mr_returns"] =  meanReversionStrategy(lcid_lines)
results_dict["lcid_sma_profit"], results_dict["lcid_sma_returns"] =  simpleMovingAverageStrategy(lcid_lines)

results_dict["rddt"] = rddt_lines
results_dict["rddt_mr_profit"], results_dict["rddt_mr_returns"] =  meanReversionStrategy(rddt_lines)
results_dict["rddt_sma_profit"], results_dict["rddt_sma_returns"] =  simpleMovingAverageStrategy(rddt_lines)

results_dict["rivn"] = rivn_lines
results_dict["rivn_mr_profit"], results_dict["rivn_mr_returns"] =  meanReversionStrategy(rivn_lines)
results_dict["rivn_sma_profit"], results_dict["rivn_sma_returns"] =  simpleMovingAverageStrategy(rivn_lines)

results_dict["rklb"] = rklb_lines
results_dict["rklb_mr_profit"], results_dict["rklb_mr_returns"] =  meanReversionStrategy(rklb_lines)
results_dict["rklb_sma_profit"], results_dict["rklb_sma_returns"] =  simpleMovingAverageStrategy(rklb_lines)

results_dict["soun"] = soun_lines
results_dict["soun_mr_profit"], results_dict["soun_mr_returns"] =  meanReversionStrategy(soun_lines)
results_dict["soun_sma_profit"], results_dict["soun_sma_returns"] =  simpleMovingAverageStrategy(soun_lines)

results_dict["sxc"] = sxc_lines
results_dict["sxc_mr_profit"], results_dict["sxc_mr_returns"] =  meanReversionStrategy(sxc_lines)
results_dict["sxc_sma_profit"], results_dict["sxc_sma_returns"] =  simpleMovingAverageStrategy(sxc_lines)

# finally, save the results dictionary to a json file
saveResults(results_dict)


# debug: print(results_dict)