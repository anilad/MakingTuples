# Write a function that takes in a dictionary and returns a list of tuples.
# The first tuple item is the key and the second is the value. 

def toList(myDict):
    myList =[]
    for key,value in myDict.iteritems():
        tup=()
        tup = tup + (key,)
        tup = tup+ (value,)
        myList.append(tup)
    print myList
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

toList(my_dict)
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
