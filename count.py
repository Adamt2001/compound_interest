# Ive been learning trading stocks, forex and crypto, so i wanted to create a small program to understand compound
# interest. this program is very simple and the instructions are below. It will show the portfolio balance each month
# as well as the total profits from interest earned over the time period

def compound(start, duration, mAmount, percentage):
    counting = start
    workingPercent = ((percentage / 100) / 12) + 1
    print(str(duration), " months with an initial investment of ", str(start), " a monthly contribution of £",
          str(mAmount), " and an annual rate of ", str(percentage), "%")
    for i in range(duration + 1):
        print(str(i), "months, £", str(counting), " at ", str(percentage), "% per year")
        counting += mAmount
        counting *= workingPercent
    profit = counting - start - (mAmount * duration)
    print("Profit of: £", str(profit))


# to run it will need 4 variables, starting amount, duration in months, the monthly contributions, and the annual
# percentage gain expected.

# (starting amount, duration in months or years*12, monthly contributions, % gain per year expected)
# (below would be £10,000 starting amount, for 2 years/ 24 months, £150 additions each month at 6% gain a year)
compound(10000, 2 * 12, 150, 6)
