# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Input: prices = [7,1,5,3,6,4]

# Output: 5

'''
    stock_price = current_profit = nums[0]

    for stock in stocks:
    
    current_profit = max(current_profit, current_profit - stock_price)

    min_value = float('inf')
    max_value = 0

    for stock_price in stocks:

        min_value = min(stock_price, min_value)
        
        calculation =  stock_price - min_val

        # store the highest profit

        max_profit = max(max_profit, calculation)

'''

def solve_easy(stocks):

    if not stocks or len(stocks) is 1:
        return 0

    max_value = 0
    min_value = float('inf')

    for stock_price in stocks:

        # select the min prices from all stocks
        min_value = min(min_value, stock_price)

        # subtract the current value of the stock with the minimum value
        calculcation = stock_price - min_value

        # get the max profit
        max_value = max(max_value, calculcation)

    return max_value

def main():

    nums = [7,1,5,3,6,4]

    res = solve_easy(nums)

    print(res)


main()