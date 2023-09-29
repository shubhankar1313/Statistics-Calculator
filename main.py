# Libraries

from tabulate import tabulate
import sys
import statistics

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
    print(tabulate(disp, headers = header, tablefmt="pretty"))

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

# Stats - MOCT

def mean(type_data):

    if type_data == 1:
        data = data_input('x')
        data_print(data, 'x')
        mean = sum(int_converter(data[0]))/len(data[0])
        print(f"\nMean (x̄) = {mean} = {round(mean, 2)}")
    
    elif type_data == 2:
        data = data_input('x', 'f')
        data_print(data, 'x', 'f')
        mean = sum(fx(int_converter(data[0]), int_converter(data[1])))/sum(int_converter(data[1]))
        print(f"\nMean (x̄) = {mean} = {round(mean, 2)}")

    elif type_data == 3:
        print("Note - Class Interval should be in X-Y format.\n")
        data = data_input('Class Interval', 'f')

        CI_to_x = []

        for interval in data[0]:
            CI_to_x.append((int(interval.split('-')[0]) + int(interval.split('-')[1]))/2)
        
        data.insert(1, str_converter(CI_to_x))
        data_print(data, 'Class Interval', 'x', 'f')
        
        mean = sum(fx(CI_to_x, int_converter(data[2])))/sum(int_converter(data[2]))
        print(f"\nMean (x̄) = {mean} = {round(mean, 2)}")

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
            median = final[int(len(final)/2)]
            print(f"\nMedian = {median} = {median:.3f}")
        else:
            median = (int_converter(final)[int(len(final)/2) - 1] + int_converter(final)[int((len(final)/2))])/2
            print(f"\nMedian = {median} = {round(median, 2)}")

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

        print(f"\nMedian = {data[0][index]} = {round(data[0][index], 2)}")

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

        median = int((data[0][index].split('-')[0])) + (height(data[0]) / int(data[2][index])) * ((sum(int_converter(data[2])) / 2) - int(data[3][index-1]))
        print(f"\nMedian = {median} = {round(median, 2)}")
        
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
        print("Note - Class Interval should be in X-Y format.\n")
        data = data_input('Class Interval', 'f')

        CI_to_x = []

        for interval in data[0]:
            CI_to_x.append((int(interval.split('-')[0]) + int(interval.split('-')[1]))/2)
        
        data.insert(1, str_converter(CI_to_x))
        data_print(data, 'Class Interval', 'x', 'f')

        if int_converter(data[2]).count(max(int_converter(data[2]))) == 1:
            index = int_converter(data[2]).index(max(int_converter(data[2])))

            # Mode = L + ((f1- f0) / (2f1 - f0 - f2)) x i
            # L = 

            f1 = int(data[2][index])
            f0 = int(data[2][index-1])
            f2 = int(data[2][index+1])
            mode = int(data[0][index].split('-')[0]) + ((f1 - f0) / ((2 * f1) - f0 - f2) * height(data[0]))
            print(f"\nMode = {mode}")
        
        else:
            print("""\nNote - The series is bi-modal and mode is ill-defined.
WORK IN PROGRESS!\n""")
            # print(f"\nMode = {(3 * MEDIAN) - (2 * MEAN)}")


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

# Stats - MOD

def range_calc(type_data):

    if type_data == 1:
        
        data = data_input('x')
        data_print(data, 'x')

        print(f"\nRange = {max(data[0]) - min(data[0])}")
        print(f"Coefficient of Range = {(max(data[0]) - min(data[0])) / (max(data[0]) + min(data[0]))} = {(round(max(data[0]) - min(data[0])) / (max(data[0]) + min(data[0])), 3)}")

    if type_data == 2:
        data = data_input('x', 'f')
        data_print(data, 'x', 'f')

        print(f"\nRange = {max(data[0]) - min(data[0])}")
        print(f"Coefficient of Range = {(max(data[0]) - min(data[0])) / (max(data[0]) + min(data[0])), round((max(data[0]) - min(data[0])) / (max(data[0]) + min(data[0])), 3)}")

    if type_data == 3:
        print("\nNote - Class Interval should be in X-Y format.\n")
        data = data_input('Class Interval', 'f')
        data_print(data, 'Class Interval', 'f')

        print(f"\nRange = {int(data[0][-1].split('-')[1]) - int(data[0][0].split('-')[0])}")
        coeff = (int(data[0][-1].split('-')[1]) - int(data[0][0].split('-')[0])) / (int(data[0][-1].split('-')[1]) + int(data[0][0].split('-')[0]))
        print(f"Coefficient of Range = {coeff} = {round(coeff, 3)}")

    elif type_data == 4:
        sys.exit("\nThank you for using!\n")

    else:
        print("Invalid input!\n")
        range_calc(type_of_data())

def quartile(type_data):

    if type_data == 1:
        
        data = data_input('x')
        data_print(data, 'x')

        q1 = int(data[0][int(((len(data[0]) + 1) / 4)-1)])
        q3 = int(data[0][int(((len(data[0]) + 1) * (3/4))-1)])

        print(f"\nLower Quartile (Q1) = {q1}")
        print(f"Upper Quartile (Q1) = {q3}")
        print(f"Interquartile Range = {q3 - q1}")
        print(f"Quartile Deviation = {(q3 - q1) / 2}")
        print(f"Coefficient of Quartile Deviation = {(q3 - q1) / (q3 + q1)} = {round(((q3 - q1) / (q3 + q1)), 3)}")

def mod():
    
    print("""\nPress 1 for Range
Press 2 for Quartile Deviation
Press 3 for Mean Deviation/Average Deviation
Press 4 to exit program""")

    try:
        choice_mod = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!\n")
        mod()

    if choice_mod == 1:
        range_calc(type_of_data())

    elif choice_mod == 2:
        quartile(type_of_data())

    elif choice_mod == 4:
        sys.exit("\nThank you for using!\n")

    else:
        print("Invalid input!\n")
        mod()

def main():
    print("""\nPress 1 for Measures of Central Tendacy/Averages
Press 2 for Measures of Dispersion
Press 3 to exit program""")
    try:
        choice_main = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!\n")
        main()
    if choice_main == 1:
        moct()

    if choice_main == 2:
        mod()

    elif choice_main == 3:
        sys.exit("\nThank you for using!\n")
    
    else:
        print("Invalid input!\n")
        main()

if __name__ == "__main__":
    main()
