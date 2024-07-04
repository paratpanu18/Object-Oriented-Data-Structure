bidding_price_list = [int(price) for price in input("Enter All Bid : ").split()]

bidding_price_list.sort()

if len(bidding_price_list) < 2:
    print("not enough bidder")
    quit()

if bidding_price_list[-1] == bidding_price_list[-2]:
    print("error : have more than one highest bid")
    quit()

print(f'winner bid is {bidding_price_list[-1]} need to pay {bidding_price_list[-2]}')
