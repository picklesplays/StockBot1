#Packing for the trip
import alpaca_trade_api as tradeapi
#Getting on the plane
api = tradeapi.REST('PK4BT6QP0N09XHS8OWXI', 'mnRZ7DGmlOx2I7EcbwpIPS41y7FnESsz0d6dMsq6', base_url='https://paper-api.alpaca.markets')
account = api.get_account()


account.status
result = api.get_last_trade("LMT")
print(result)