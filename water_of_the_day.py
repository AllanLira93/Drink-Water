

def water_of_the_day():
    while True:
        try:
            weight = float(
                input("Please enter your weight in kg. Use '.' instead of ','if the number is not an integer:  "))
            required_water = weight * 35
            ml_for_l = required_water / 1000
            print(f"The recommendation is {ml_for_l:.2f}L of water per day or {required_water:.2f}ml. ")
        except ValueError:
            continue
        break

water_of_the_day()

