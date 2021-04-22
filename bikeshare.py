import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    while True :
        try:
            valid_cities = ['chicago', 'new york', 'washington']
            city = input("Would you like to see data for Chicago, New York, or Washington:\n").lower()
            if city in valid_cities:
                break
            else:
                print("Your input city is invalid it most be from three cities that mentioned above ... Try again !\n")
        except:
            print("Your input is not valid please check the name of city you entered\n")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        try:
            valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
            month = input("Which month? January, February, March, April, May, June or all:\n").lower()
            if month in valid_months:
                break
            else:
                print("The month you entered is invalid. Your input must be from the first six months ... Try again !\n")
                continue
        except:
            print("Your input is not valid please check the name of month you entered and try again !\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        try:
            print("Do not use any abbreviations when you enter the day name\n")
            valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all:\n").lower()
            if day in valid_days:
                break
            else:
                print("Your input day is invalid ... Try again !")
        except:
            print("Your input is not valid please check the name of day you entered")



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
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert "Start Time" cloumn type to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['month'] = df['Start Time'].dt.month # This line to add new column "month" that contains the months from "Start Time" column
    df['day_of_week'] = df['Start Time'].dt.weekday_name # This line to add new column "day_of_week" that contains the days name from "Start Time" column
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 # This assignment statment to get the index of the month that user entered
        df = df[df['month'] == month] #Filter By Month
    else:
        pass
    
    if day != 'all':
        day = day.title() #This line of code to make the name of the day matches with the day's name in our DataFrame
        df = df[df['day_of_week'] == day] #Filter By Day Of Week
    else:
        pass
    
    return df



def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is {}".format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print("The most common day of week is {}".format(df['day_of_week'].mode()[0]))

          
    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    print("The most common start hour is {}".format(df['Start Hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: {}".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("The most commonly used end station is: {}".format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "|" + df['End Station']
    list_combination = df['combination'].mode()[0].split("|")
    print("The most frequent combination of start station and end station trip is:")
    print("Start Station --> {} and End Station --> {}".format(list_combination[0], list_combination[1]))
    
    df = df.drop(["combination"], axis = 1) # Drop this column from our dataset
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    print("Total Travel Time is --> {}".format(df['Travel Time'].sum()))


    # TO DO: display mean travel time
    # mean = df['Travel Time'].sum() / len(df['Travel Time'])
    print("The mean of Travel Time is --> {}".format(df['Travel Time'].sum() / len(df['Travel Time'])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of Subscribers --> {}".format(df['User Type'].value_counts()[0]))
    print("Counts of Customers --> {}".format(df['User Type'].value_counts()[1]))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Counts of Males --> {}".format(df['Gender'].value_counts()[0]))
        print("Counts of Femals --> {}".format(df['Gender'].value_counts()[1]))
    else:
        print("This Dataset has not Gender criteria")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The Earliest year of birth is --> {}".format(df['Birth Year'].min()))
        print("The Most Recent year of birth is --> {}".format(df['Birth Year'].max()))
        print("The Most common year of birth is --> {}".format(df['Birth Year'].mode()))
    else:
        print("This Dataset has not Birth Year criteria")
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def get_sample(df, start=0, end=5):
    """Displays a sample of number of rows that specified from the user.
    Args:
        df --> DataFrame of a city and filters that applied by month and day.
        start --> start index that the sample will start from it
        end --> end index that the sample will end at it
    
    Return:
        It returns a sample of data with n_sample.
    """
    s_index = start
    e_index = end

    print("\nYour Sample:\n{}".format(df.iloc[s_index : e_index]))
            
    while True:
            
        more_sample = input("\nWould you want to take another sample ?\n").lower()

        if more_sample == 'yes':
            s_index += 5
            e_index += 5
            print("\nYour Sample:\n{}".format(df.iloc[s_index : e_index]))
        elif more_sample == 'no':
            break
        else:
            print("Your answer is invalid please answer wit yes or no !")
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            q = input("\nWould you want to see a sample from data after your applied filters?\n")
            if q == 'yes':
                get_sample(df)
                break
            elif q == 'no':
                break
            else:
                print("\nYour answer is invalid, please answer with yes or no\n")
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()