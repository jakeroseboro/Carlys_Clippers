#Defining a mock scenario to use the function on
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#Sum of all prices
total_price= 0
for i in prices:
  total_price += i
#Average price
average_price= total_price/len(prices)

#Testing the code
print('Average Haircut Price: '+ str(average_price))

#Cutting the prices
new_prices= [price-5 for price in prices]

#Testing the code
print(new_prices)

#Now we calculate revenue
total_revenue = 0 
for i in range(len(hairstyles)):
  total_revenue = prices[i]*last_week[i]

#Testing the code
print('Total Revenue: '+ str(total_revenue))

#Average daily revenue
average_daily_revenue = total_revenue/7

#Cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i]<30 ]

#Testing the code
print(cuts_under_30)