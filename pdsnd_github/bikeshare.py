import time
import pandas as pd
import numpy as np

# loading files from .csv
CITY_DATA = {
    'chicago':'chicago.csv',
    'new york city':'new_york_city.csv',
    'washington':'washington.csv'
}

def get_city():
    '''
    This function starts the user interface by introduction and
    asking the user with the city he/she wants to analyze
    '''
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Please select the city you would like to explore:\n')
    city = input(' For Chicago, type 1\n for New York City, type 2\n For Washington type 3\n --> Type here: ').lower()
    while True:     # for handling the unexpected input by user
            if city == '1' or city == 'chicago':
                print('You have selected Chicago')
                return 'chicago'
            if city == '2' or city == 'new york city':
                print('You have selected New York City')
                return 'new york city'
            elif city == '3' or city == 'washington':
                print('You have selected Washington')
                return 'washington'
            # error handled by implementing 'else' and provided another option to input data
            else:
                city = input('No city was selected.\n  For Chicago, type 1\n for New York City, type 2\n For Washington type 3\n --> Type here: ')
                if city == '1':
                    return 'chicago'
                if city == '2':
                    return 'new york city'
                if city == '3':
                    return 'washington'
                else:
                    print('Default was chosen, displaying data for Chicago')
                    return 'chicago'
    return city

def get_filter():
# get user input for month (all, january, february, ... , june)
    data_filter = input('Would you like to filter the data by month, day, both or not at all?\n For month, type 1\n For day, type 2\n For both, type 3\n for no filter, type 4\n -->Type Here').lower()
    while True:
        if data_filter == '1' or data_filter == 'month':
            return 'month'
        if data_filter == '2' or data_filter == 'day':
            return 'day'
        if data_filter == '3' or data_filter == 'both':
            return 'both'
        elif data_filter == 'none' or data_filter == 'no' or data_filter == '4':
            return 'none'
        else:
            data_filter = input('No filter was selected\n For month, type 1\n For day, type 2\n For both, type 3\n for no filter, type 4\n -->Type Here ')
            if data_filter == '1':
                return 'month'
            if data_filter == '2':
                return 'day'
            if data_filter == '3':
                return 'both'
            if data_filter == '4':
                return 'none'
            else:
                print('No filter was selected, displaying default data for both month and day')
                return 'both'
    return data_filter
def get_month():
    MONTHS = {'january': '1', 'february': '2', 'march': '3', 'april': '4', 'may': '5', 'june': '6'}
    month = ''
    while month not in MONTHS.keys():
        month = input(" Please select the month you would like to explore\n For January, type january\n For February, type february\n For March, type march, For April, type april\n For May, type may\n For June, type june\n Or type all for full months data").lower()
        if month not in MONTHS.keys():
            print("Month value was out of scope.\ndefault value was selected, displaying data for January")
            return 'january'
    return month
def get_day():
        DAYS = {'all': '0', 'sunday': '1', 'monday': '2', 'tuesday': '3', 'wednesday': '4', 'thursday': '5', 'friday': '6', 'saturday': '7'}
        day = ''
        while day not in DAYS.keys():
            day = input("Please select the day of the week you would like to explore\n For all week, type all\n For Sunday, type sunday\n For Monday, type monday\n For Tuesday, type tuesday\n For Wednesday, type wednesday\n For Thursday, type thursday\n For Friday, type friday \n For Saturday, type saturday" ).lower()
            if day not in DAYS.keys():
                print("Day value was out of scope.\ndefault value was selected, displaying data for all week")
                return 'all'
        return day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading...")
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Filter by day of the week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month:" ,common_month)
    #  display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nMost common Day: ", common_day)
    #  display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("\nMost common hour: ", common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nMost common start station: ", common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nMost common end station: ", common_end_station)
    #  display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' , ')
    combination = df['Start To End'].mode()[0]
    print("\nMost frequent combination of start station and end station trip: ", combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #  display total travel time
    total_travel_duration = df['Trip Duration'].sum()
    # Covert time to hours, minutes and seconds
    minutes, seconds = divmod(total_travel_duration, 60)
    hours, minutes= divmod(minutes, 60)
    print("Total trip duration is", hours , "hours," , minutes , "minutes and" , seconds,  "seconds")
    #  display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    minutes_mean, seconds_mean = divmod(average_duration, 60)
    hours_mean, minutes_mean= divmod(minutes, 60)
    print("Avarge trip duration is", hours_mean , "hours," , minutes_mean , "minutes and" , seconds_mean,  "seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("User type:", user_type)
    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Gender count ", gender)
    except:
        print("No gender info")
    # Display earliest, most recent, and most common year of birth
    try:
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest birth year is ", earliest)
        latest = np.max(df['Birth Year'])
        print ("\nThe latest birth year is ", latest)
        frequent_year = df['Birth Year'].mode()[0]
        print ("\nThe most frequent year of birth is ", frequent_year)
    except:
        print('No birth info.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    #Drop but don't save
    df = df.drop(['month', 'day_of_week'], axis = 1)
    row_index = 0
    show_data = input("\nWowuld you like to view the raw data? 'yes' or 'no' \n").lower()
    while True:
        if show_data == 'no':
            return
        if show_data == 'yes':
            print(df[row_index: row_index + 5])
            row_i = row_index + 5
        show_data = input("\n Would you like to view five more rows of the raw data? 'yes' or 'no' \n").lower()
        #Calling the functions
def main():
    city = get_city()
    filter = get_filter()
    month = get_month()
    day = get_day()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    raw_data(df)
    # Restarting option
    restart = input('\n * Would you like to do it again and perform another analysis? Type \'yes\' or \'no\'.\n')
    if restart.upper() == 'YES' or restart.upper() == 'Y':
        main()

if __name__ == '__main__':
    main()
