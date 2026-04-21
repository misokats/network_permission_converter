distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

if not distance <= 0:
    print(False)
elif distance_mi <= 1 and is_raining:
    print(True)
elif 6 >= distance_mi > 1 and has_bike and not is_raining:
    print(True)
elif distance_mi > 6 and (has_car or has_ride_share _app):
    print(True)
else:
    print(False) 
