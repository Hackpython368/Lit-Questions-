import json

text_lst = []

with open('alphabet.json', 'r') as file:
    json_data = json.load(file)



def print_letter_in_patter(lst):
    for i in lst:
        if i in json_data.keys():            
            text_lst.append(json_data[i])
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    fifth_line = ""
    count = 0
    while count < 5:
        for i in text_lst:
            for j in i[count]:
                for k in j:
                    if count == 0:
                        first_line += k
                    elif count == 1:
                        second_line += k
                    elif count == 2:
                        third_line += k
                    elif count == 3:
                        fourth_line += k
                    elif count == 4:
                        fifth_line += k
                    
        count += 1
    
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)
            

    
    
if __name__ == "__main__":
    letters = list(input("Enter letters: ").upper())
    print_letter_in_patter(letters)