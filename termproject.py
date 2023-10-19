print("Welcome to your personal financial budgeting plan! This plan is based on a month's worth of work and costs.")

total = float(input("How much is your estimated salary? "))

# apply tax bracket percent to estSal
taxed=(total*.85)
homeOwner=input('Do you pay rent or a morgage ')
if homeOwner=='yes' and 'Yes':
    htotal=round(taxed-900,2)
htotal=round(htotal-70,2)
carOwner=input('Do you own your own vehicle ')
if carOwner=='yes' and 'Yes':
    ctotal=round(htotal-200)
    ctotal=(ctotal-78)
    ctotal=(ctotal-150)

#estimated food based on if the user owns their own home
#if so, then food goes up for groceries
#if not then food is based on fast food at $11 per meal 3 times a week
ftotal=(ctotal-132)
if homeOwner=='yes' or 'Yes':
    ftotal=(ftotal-200)

if ftotal<0:
    print('Your final amount remaining after all expected expenses is',ftotal,'. You should kill yourself.')