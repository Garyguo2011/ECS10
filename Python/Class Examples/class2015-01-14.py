PhoneBook = {}
PhoneBook['cs phone'] = '(530) 752-7004'
PhoneBook['cs fax'] = '(530) 752-4767'
PhoneBook['ece phone'] = '(530) 752-0583'
PhoneBook['ucd phone'] = '(530) 752-1011'
PhoneBook['ee phone'] = '(530) 752-0583'

SearchName = input("Enter name> ")
if SearchName.lower() in PhoneBook:
    print("Phone number of",SearchName,"is",PhoneBook[SearchName.lower()])
else:
    print(SearchName,"is not in phone book!")

ReversePhoneBook = {'(530) 752-7004':'CS Phone', '(530) 752-4767':'CS Fax', '(530) 752-0583': 'ECE Phone','(530) 752-1011':'UCD Phone' }

SearchNumber = input("Enter number> ")
if SearchNumber in ReversePhoneBook:
    print("Name of",SearchNumber,"is",ReversePhoneBook[SearchNumber])
else:
    print(SearchNumber,"is not in phone book!")
    if (len(PhoneBook[SearchName.lower()]) - len(SearchNumber)) == PhoneBook[SearchName.lower()].find(SearchNumber):
        print(SearchNumber,"is same as",PhoneBook[SearchName.lower()])
    else:
        print(SearchNumber,"is not the same as",PhoneBook[SearchName.lower()])
