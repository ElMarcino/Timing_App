import pandas as pd

filename = 'Times.csv'
track_length = 3900


def new_entry():
    df = pd.read_csv(filename)
    car = input('Enter car name: ')
    while True:
        race_time = input('Enter time in MM:SS:MSMS format: ')
        if race_time[2] == ':' and race_time[5] == ':' and race_time[0:2].isnumeric() \
                and race_time[3:5].isnumeric() and race_time[6:9].isnumeric():
            break
        else:
            print('Invalid time format')
    drivetrain = input('Enter drivetrain type: ')

    new_data = pd.DataFrame({'Car': [car],
                             'Time': [race_time],
                             'Drivetrain': [drivetrain]})

    df = df.append(new_data, ignore_index=True)
    df = df.sort_values('Time')
    df = df.reset_index(drop=True)
    df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
    df.to_csv(filename)


def help_info():
    print(f'"all" - show all entries to the {filename} file')
    print('"add" - add new entry to the file')
    print('"del" - delete an entry from a file')
    print('"exit" - exit the program')
    print('"xlsx" - convert a csv to xlsx file')
    print(f'"clear" - clear data from {filename} file')


def delete_entry():
    car_to_delete = int(input('Please enter an entry number to delete: '))
    df = pd.read_csv(filename)
    df = df.drop(index=car_to_delete)
    df = df.sort_values('Time')
    df = df.reset_index(drop=True)
    df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
    df = df.to_csv(filename)


def calc_diff():
    df = pd.read_csv(filename)
    df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
    for x in range(len(df.index)):
        df.iloc[x, 3] = millis_diff(time_to_millis(df.iloc[x, 1]), time_to_millis(df.iloc[x - 1, 1])) / 1000
        if df.iloc[x, 3] < 0:
            df.iloc[x, 3] = 0

    df = df.to_csv(filename)


def time_to_millis(value):
    split_value = value.split(':')
    min_to_millis = int(split_value[0]) * 60 * 1000
    sec_to_millis = int(split_value[1]) * 1000
    millis = int(split_value[2])
    millis_sum = min_to_millis + sec_to_millis + millis
    return millis_sum


def millis_diff(val1, val2):
    return int(val1) - int(val2)


def avg_speed(time, distance):
    speed = round(distance / time, 2)
    return speed


def calc_avg_speed(length):
    df = pd.read_csv(filename)
    df.drop(df.filter(regex="Unnamed: "), axis=1, inplace=True)
    for x in range(len(df.index)):
        df.iloc[x, 4] = avg_speed(time_to_millis(df.iloc[x, 1]) / 1000, length) * 18 / 5
    df = df.to_csv(filename)


def convert_to_xlsx(filename_xlsx):
    df = pd.read_csv(filename)
    df.to_excel(filename_xlsx, index=None, header=True)


def clear_data():
    df = pd.read_csv(filename)
    for x in range(len(df.index)):
        df = df.drop(index=0)
        df = df.reset_index(drop=True)
    df = df.to_csv(filename)