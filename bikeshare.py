import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nEnter city name: New York, Chicago or Washington?\n").title()
      if city not in ('New York', 'Chicago', 'Washington'):
        print("Please enter a valid city name and try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nEnter a month: January, February, March, April, May, June or 'All'?\n").title()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        print("Please enter valid month and try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nEnter a particular day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'All'?\n").title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print("Please enter valid day and try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]
    print('Most common month is:', popular_month)


    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most common day is:', popular_day)



    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour is:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station is:', Start_Station)


    #display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station is:', End_Station)


    #display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost commonly used combination of start station trip is {} and end station trip is {}'.format(Start_Station, End_Station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time is:', Total_Travel_Time/86400, " Days")


    #display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Average travel time is:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    #Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data.")

    #Display earliest, most recent, and most common year of birth

    try:
      earliest_year_of_birth = df['Birth Year'].min()
      print('\nEarliest Year of Birth:', earliest_year_of_birth)
    except KeyError:
      print("\nEarliest Year of Birth:\nNo data.")

    try:
      most_recent_year_of_birth = df['Birth Year'].max()
      print('\nMost Recent Year of Birth:', most_recent_year_of_birth)
    except KeyError:
      print("\nMost Recent Year of Birth:\nNo data.")

    try:
      most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year of Birth:', most_common_year_of_birth)
    except KeyError:
      print("\nMost Common Year of Birth:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    """Displays 5 lines of raw data."""
    x=0
    y=5
    
    display_data = input("\nWould you like to see first five rows of raw data? Yes or No?\n").title()
    
    if display_data == 'Yes':
       while True:
        print(df.iloc[x:y,:])
        x+=5
        y+=5
        
        next_display_data = input("\nWould you like to see next five rows of raw data?\n").title()
        if next_display_data == 'No':
            break         

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').title()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()