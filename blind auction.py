from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
again=True
bid_dic={}
while again:
  name=input("What is your name: \n")
  bid=int(input("What is your bid?: $ \n"))
  
  bid_dic[name]=bid
  ask=input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if ask=="no":
    again=False

bids=[]    
for key in bid_dic:
  bids.append(bid_dic[key])
max=max(bids)
for key in bid_dic:
  if bid_dic[key]==max:
    key_max=key
  #key=key_max
print(f"The winner is {key_max} with {max} bids")