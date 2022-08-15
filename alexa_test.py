monday = 'you have physics today at 4pm'
tuesday = 'you have maths today at 4pm'
wednesday = 'you have eco today'
thursday = 'you have maths today at 4pm'
friday = 'you have physics today at 4pm'
saturday = 'you have eco today'
sunday = 'you dont have any classes today'

a = input('whats the day today? ')

if a=='monday':
    print (monday)

elif a=='tuesday':
    print (tuesday)

elif a=='wednesday':
    print (wednesday)

elif a=='thursday':
    print (thursday)

elif a=='friday':
    print (friday)

elif a=='saturday':
    print (saturday)

elif a=='sunday':
    print (sunday)

else:
    print ('thats not a day')
