# Libraries

from tabulate import tabulate
import sys

# Functionality

def int_converter(data):

    return list(map(int, data))

def str_converter(data):

    return list(map(str, data))

def data_input(*args):

    data_list = []

    for i in range(len(args)):
        data_list.append(input(f"\nEnter values of {args[i]} separated by space:\n").split())

    return data_list

def type_of_data():

    print("""\nPress 1 for a set of observations (x)
Press 2 for frequency distribution (x, f)
Press 3 for frequency distribution (Class Interval, f)
Press 4 to exit program""")
    
    return int(input("Enter choice: "))

def data_print(data, *args):
    
    print("\n")
    header = []

    for arg in args:
        header.append(arg)
    
    disp = []

    for i in range(len(data[0])):
        entry = []
        for j in range(len(data)):
            entry.append(data[j][i])
        disp.append(entry)

    # TESTING
    # print(data, disp, header)
    print(tabulate(disp, headers = header))

def fx(x, f):
    """
    Named fx but the order of arguments is x followed by f.
    """

    fx = []

    for i in range(len(x)):
        fx.append(x[i]*f[i])
    
    return fx

def cf(frequencies):

    cf, sum = [], 0

    for f in frequencies:
        sum += f
        cf.append(sum)

    return cf

def height(data):
    return int(data[0].split('-')[1]) - int(data[0].split('-')[0])

# Stats

def mean(type_data):

    if type_data == 1:
        data = data_input('x')
        data_print(data, 'x')
        mean = sum(int_converter(data[0]))/len(data[0])
        print(f"\nMean (x̄) = {mean} = {mean:.3f}")
    
    elif type_data == 2:
        data = data_input('x', 'f')
        data_print(data, 'x', 'f')
        mean = sum(fx(int_converter(data[0]), int_converter(data[1])))/sum(int_converter(data[1]))
        print(f"\nMean (x̄) = {mean} = {mean:.3f}")

    elif type_data == 3:
        print("Note - Class Interval should be in X-Y format.\n")
        data = data_input('Class Interval', 'f')

        CI_to_x = []

        for interval in data[0]:
            CI_to_x.append((int(interval.split('-')[0]) + int(interval.split('-')[1]))/2)
        
        data.insert(1, str_converter(CI_to_x))
        data_print(data, 'Class Interval', 'x', 'f')
        
        mean = sum(fx(CI_to_x, int_converter(data[2])))/sum(int_converter(data[2]))
        print(f"\nMean (x̄) = {mean} = {mean:.3f}")

    elif type_data == 4:
        sys.exit("\nThank you for using!\n")

    else:
        print("Invalid input!\n")
        mean(type_of_data())

def median(type_data):
    
    if type_data == 1:
        data = data_input('x')
        data_print(data, 'x')
        final = int_converter(data[0])
        final.sort()
        
        if len(data[0]) % 2 == 1:
            print(f"\nMedian = {final[int(len(final)/2)]}")
        else:
            print(f"\nMedian = {(int_converter(final)[int(len(final)/2) - 1] + int_converter(final)[int((len(final)/2))])/2}")

    elif type_data == 2:

        data = data_input('x', 'f')
        data.append(cf(int_converter(data[1])))
        data_print(data, 'x', 'f', 'c.f.')
        
        for f in data[2]:
            if f < (sum(int_converter(data[1]))/2):
                continue
            else:
                index = int_converter(data[2]).index(f)
                break

        print(f"\nMedian = {data[0][index]}")

    elif type_data == 3:
        print("Note - Class Interval should be in X-Y format.\n")
        data = data_input('Class Interval', 'f')

        CI_to_x = []

        for interval in data[0]:
            CI_to_x.append((int(interval.split('-')[0]) + int(interval.split('-')[1]))/2)
        
        data.insert(1, str_converter(CI_to_x))
        data.append(cf(int_converter(data[2])))
        data_print(data, 'Class Interval', 'x', 'f', 'c.f.')
            
        for f in data[3]:
            if int(f) < (sum(int_converter(data[2]))/2):
                continue
            else:
                index = int_converter(data[3]).index(f)
                break
        
        # Median = l + (h/f)((N/2) - c.f.)
        # l = data[0][index].split('-')[0]
        # h = int(data[0][0].split('-')[1]) - int(data[0][0].split('-')[0])
        # f = int(data[2][index]
        # N = sum(int_converter(data[2]))

        print(f"\nMedian = {int((data[0][index].split('-')[0])) + (height(data[0]) / int(data[2][index])) * ((sum(int_converter(data[2])) / 2) - int(data[3][index-1]))}")
        
    elif type_data == 4:
        sys.exit("\nThank you for using!\n")

    else:
        median(type_of_data())

def mode(type_data):

    if type_data == 1:
        data = data_input('x')
        data_print(data, 'x')
        
        print(f"\nMode = {max(data[0], key = data[0].count)}")

    elif type_data == 2:

        print("\nWORK IN PROGRESS!")

    elif type_data == 3:
        pass

    elif type_data == 4:
        sys.exit("\nThank you for using!\n")

    else:
        mode(type_of_data())

def moct():

    print("""\nPress 1 for Mean
Press 2 for Median
Press 3 for Mode
Press 4 to exit program""")
    try:
        choice_moct = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!\n")
        moct()
    
    if choice_moct == 1:
        mean(type_of_data())

    elif choice_moct == 2:
        median(type_of_data())

    elif choice_moct == 3:
        mode(type_of_data())

    elif choice_moct == 4:
        sys.exit("\nThank you for using!\n")

    else:
        print("Invalid input!\n")
        moct()

def main():
    print("""\nPress 1 for Measures of Central Tendacy/Averages
Pres 3 to exit program""")
    try:
        choice_main = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!\n")
        main()
    if choice_main == 1:
        moct()

    elif choice_main == 3:
        sys.exit("\nThank you for using!\n")
    
    else:
        print("Invalid input!\n")
        main()

if __name__ == "__main__":
    main()
