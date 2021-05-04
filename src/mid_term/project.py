# THE PROGRAM WILL COMPUTE AND DISPLAY INFORMATION FOR A UTILITY COMPANY WHICH SUPPLIES WATER TO IT'S CUSTOMERS'
def waterbilling():
    billing = 0
    while True:
        try:

            # INPUT SECTION
            code = input("Enter customers code: ").lower()
            if code == "c" or code == "r" or code == "i":
                while True:
                    begin = int(input("Enter beginning meter reading: "))
                    if begin < 0:
                        print('Please enter positive value')
                    else:
                        break
                while True:
                    end = int(input('Enter ending meter reading'))
                    if end < 0:
                        print('Please enter positive value')
                    else:
                        break
                if end > begin:
                    gallons_of_water_used = (end - begin) / 10
                else:
                    gallons_of_water_used = ((1000000000 - begin) + end) / 10

                # BILLING CALCULATION SECTION
                if code == "r":
                    billing = 5 + (0.0005 * gallons_of_water_used)
                elif code == "c":
                    if gallons_of_water_used <= 4000000:
                        billing = 1000.00
                    else:
                        billing = 1000.00 + (0.00025 * (gallons_of_water_used - 4000000))
                elif code == "i":
                    if gallons_of_water_used <= 4000000:
                        billing = 1000.00
                    elif not gallons_of_water_used <= 4000000 and gallons_of_water_used <= 1000000:
                        billing = 2000.00
                    else:
                        billing = 2000.00 + (0.00025 * (gallons_of_water_used - 1000000))
                else:
                    pass

                # OUTPUT SECTION FOR THE INFORMATION DISPLAY
                print(f""" 
Customer code: {code}
Beginning meter reading: {begin}
Ending meter reading: {end}
Gallons of water used: {gallons_of_water_used}
Amount billed: ${round(billing, 2)}
                    """)
            else:
                print(">>>>>")
                break
        except ValueError:
            print("invalid input")


waterbilling()
