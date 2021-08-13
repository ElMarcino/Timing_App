import pandas as pd
import func
import sys

track_length = 3900
filename = 'Times.csv'
df = pd.read_csv(filename)
print('Type "help" to see available commands')
user_input = input('').upper()
while True:
    df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
    if user_input == 'HELP':
        df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
        func.help_info()
        user_input = input('Write a command: ').upper()
    elif user_input == 'ADD':
        df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
        func.new_entry()
        # df = df.to_csv(filename)
        user_input = input('Write a command: ').upper()
    elif user_input == 'DEL':
        func.delete_entry()
        user_input = input('Write a command: ').upper()
        df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
    elif user_input == 'EXIT':
        sys.exit()
    elif user_input == 'ALL':
        df = pd.read_csv(filename)
        df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
        func.calc_diff()
        func.calc_avg_speed(track_length)
        df = pd.read_csv(filename)
        df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
        func.calc_diff()
        func.calc_avg_speed(track_length)
        print(df)
        user_input = input('Write a command: ').upper()
    elif user_input == 'XLSX':
        xlsx_filename = input('Please enter file name fe. filename.xlsx: ')
        func.convert_to_xlsx(xlsx_filename)
        user_input = input('Write a command: ').upper()
    elif user_input == 'CLEAR':
        func.clear_data()
        user_input = input('Write a command: ').upper()
    else:
        print('Invalid command, try again')
        user_input = input('Write a command: ').upper()

