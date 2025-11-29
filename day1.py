def get_input(infile):
    with open(infile) as file:
        output = [line.strip() for line in file]
    return output

def process_list(input_list):
    output_list = []
    for st in input_list:
        new_list = []
        for char in st:
            if char.isdigit() == True: new_list.append(int(char))
        output_list.append(new_list)
    return output_list

def process_list_part2(input_list):
    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    output_list = []
    
    for st in input_list:
        new_list = []
        for i,c in enumerate(st):
            if st[i].isdigit() == True: new_list.append(int(st[i]))
            else:
                for k in values.keys():
                    if st[i:].startswith(k):
                        new_list.append(values[k])
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
    output_datapart2 = process_list_part2(input_data)
    print('Part 1: ',sum((get_calibration_values(output_data))))
    print('Part 2:', sum(get_calibration_values(output_datapart2)))
    