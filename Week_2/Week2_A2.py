ask_user1 = float(input('What is the distance (in km)'))

ask_user3 = float(input('At what speed are you travelling (in km/h)?'))
travelling_time_car = ask_user1/ask_user3
travelling_time_biking = ask_user1/ask_user3
travelling_time_walking = ask_user1/ask_user3

ask_user2 = input('What is your means of travelling - car, bike or walk?').lower()
if ask_user2 == 'car':
    print('The travelling time is '+str(travelling_time_car)+' hours')

elif ask_user2 == 'bike':
    print('The travelling time is '+str(travelling_time_biking)+' hours')

elif ask_user2 == 'walk':
    print('The travelling time is '+str(travelling_time_walking)+' hours')

else: print('I cannot understand you')

ask_user = float(input('How much time do you need to prepare and get to your destination (in h)?'))

preparation_time = ask_user

if  ask_user2 == 'car':
    print(('Your total travelling time including preparation will be '+str(travelling_time_car+preparation_time)+' hours'))

elif ask_user2 == 'bike':
    print(('Your total travelling time including preparation will be '+str(travelling_time_biking+preparation_time)+' hours'))

elif ask_user2 == 'walk':
    print(('Your total travelling time including preparation will be ' + str(travelling_time_walking + preparation_time)+' hours'))

else:
    print('I cannot understand you')