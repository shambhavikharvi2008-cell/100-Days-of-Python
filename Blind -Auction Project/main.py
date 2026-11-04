import art
print(art.logo)
dictionary={}
should_continue=True
while should_continue:


    user_name=input("What is your name? : ")
    user_bid=input("whats your bid?: $")


    dictionary[user_name]=user_bid

    

    user_input=input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if user_input=="no":
        should_continue=False
    print("\n"*100)


bid=[]
for key in dictionary:
     bid.append(dictionary[key])
new_bid=[]
for value in bid:
    if value.isdigit():
        new_bid.append(int(value))



maximum_bid=max(new_bid)

for key in dictionary:
    if dictionary[key].isdigit():
        if int(dictionary[key])==maximum_bid:
            print(f"The winner is {key} with a bid of ${maximum_bid}.")


















