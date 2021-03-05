import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What city do you want? Select chicago, new york city, or washington: ').lower()  #(D., 2021)
    while city not in CITY_DATA.keys(): #(A. H., 2020)
        print('Incorrect city')
        city = input('What city do you want? Select chicago, new york city, or washington: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('What month do you want? Select all, january, february, march, april, may, or june: ').lower()
    while month not in month_list:
        print('Incorrect month')
        month = input('What month do you want? Select all, january, february, march, april, may, or june: ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('What month do you want? Select all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday: ').lower()
    while day not in day_list:
        print('Incorrect day')
        day = input('What day do you want? Select all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday: ').lower()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):  #('Load Data', n.d.)
	#this is a comment
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file into the dataframe
    df = pd.read_csv(CITY_DATA[city])
	
	#convert Start-time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
	
	#extract day and month
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
	
	#filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 #indexing starts at 0 so add 1 to get the correct month number
		
		#filter by month to create new dataframe
        df = df[df['month'] == month]
		
	#filter by day, 
    if day != 'all':   #(T. , n.d.)
		#filter by day of week to create new dataframe
        df = df[df['weekday'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]  #('Most Common', 2020)
    #print('{} is the most common month'.format(common_month))
    print('{} is the most common month'.format(months[common_month-1]))
    #print(most_common_month)

    # display the most common day of week
    common_day = df['weekday'].mode()[0]
    print('{} is the most common day of the week'.format(common_day))
    #print(most_common_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour  #(O., 2020)
    common_hour = df['hour'].mode()[0]
    print('{} is the most common start hour'.format(str(common_hour)))
    #print(most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	#this is a comment


def station_stats(df):  #(A., 2020).
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0] 
    print('{} is the most commonly used start station'.format(common_start))
    #print(common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('{} is the most commonly used end station'.format(common_end))
    #print(common_end)
    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('{} is the most frequent combination of start station and end station trip'.format(common_trip))
    #print(common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df): #(H., 2020)
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time in days
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = total_travel_time / (60*60*24)
    print("This trip lasts {} days".format(total_travel_time))

    # TO DO: display mean travel time in minutes
    average_travel_time = df['Trip Duration'].sum()
    average_travel_time = average_travel_time / 60
    print("The average travel time is {} minutes".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subscribers = df[df['User Type']=='Subscriber']
    subscriber_count = len(subscribers)
    customers = df[df['User Type']=='Customer']
    customer_count = len(customers)
    print('There are {} subscribers'.format(subscriber_count))
    print('There are {} customers'.format(customer_count))
    # TO DO: Display counts of gender
    if 'Gender' in df.columns: #(D., 2020)
        males = df[df['Gender']=='Male']
        male_count = len(males)
        females = df[df['Gender']=='Female']
        female_count = len(females)
        print('There are {} males'.format(male_count))
        print('There are {} females'.format(female_count))
    else:
        print('No gender count exists')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: #(M., n.d.b), (A. C., 2020)
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        common_year_of_birth = df['Birth Year'].mode()[0]
        print('{} is the earliest year of birth'.format(int(earliest_year_of_birth)))
        print('{} is the most recent year of birth'.format(int(most_recent_year_of_birth)))
        print('{} is the most common year of birth'.format(int(common_year_of_birth)))
    else:
        print('No birth year available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df)
        df_input = input('\n Would you like to display the next five lines?\nEnter yes or no\n').lower() #(M., n.d.a)
        if df_input in ('yes', 'y'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_df_input = input('Would you like to see more? Enter yes or no: ').lower()
                if more_df_input not in ('yes','y'):
                    break
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
