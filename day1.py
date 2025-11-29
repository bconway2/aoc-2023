def get_input(infile):
    with open(infile) as file:
        output = [line.strip() for line in file]
    return output

def process_list(input_list):
    output_list = []
    for st in input_list:
        l_string = list(st)
        new_list = []
        for item in l_string:
            if item.isdigit() == True: new_list.append(int(item))
        output_list.append(new_list)
    return output_list

def get_calibration_values(refined_list):
    calibration_values = []
    for list in refined_list:
        calibration_values.append(int(str(list[0]) + str(list[-1])))
    return calibration_values

if __name__ == "__main__":
    input_data = get_input("./inputs/day1.txt") 
    output_data = process_list(input_data)
    print('Part 1: ',sum((get_calibration_values(output_data))))
    print('aha')
    