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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #while true is used to check every condition in infinite loop till it is true.
        
        
        city = input("select city name (chicago, new york city,washington) : ").lower()
        if city in CITY_DATA.keys():#keys() usedto get keys from dictionary file
            
            break
        else:
            print("please enter correct city name")
    


    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    
    
    while True:
        month = input("select month name (all,january,february,march,april,may,june) : ").lower()
        if month in months:
            break
        else:
            print("please enter correct month")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days =['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
        
    while True:
        day = input("choose a day(sunday,monday,tuesday,wednesday,thursday,friday,saturday,all) : ").lower()
        if day in days :
            break
        else:
            print("please enter correct day")
            


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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #converting the data to date time format
    
    df['month'] = df['Start Time'].dt.month 
    #creating new column from start time column
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    #day_of_week column created
    df['start hour'] = df['Start Time'].dt.hour 
    
    if month != 'all':
        
        
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1 
         
        
        
        df = df[df['month'] == month] 
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
     most_common_month = df['month'].mode()[0] 
     
    
    print("The most common month is :" , most_common_month)




    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
        
    print("The most common day is : ", most_common_day)


    # display the most common start hour
    most_common_start_hour = df['start hour'].mode()[0] 
    
    
    print("The most common start hour is : ", most_common_start_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    # TO DO: display most commonly used start station
    
    most_common_start_station = df['Start Station'].mode()[0]
    
    
    print("The most common start station is :", most_common_start_station )
    


    # TO DO: display most commonly used end station
    
    most_common_end_station = df['End Station'].mode()[0] 
    
    
    print("The most common end station is :", most_common_end_station )


    # TO DO: display most frequent combination of start station and end station trip
    
    df['frequent_com_sta'] = df['Start Station']+","+df['End Station']
    #will combine both the columns to take input
    
    
    most_frequent_combination = df['frequent_com_sta'].mode()[0]
      
    
    print("The most frequent combination of start and end station is : ", most_frequent_combination )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = (df['Trip Duration'].sum()).round()
     
    
    print("Total travel time is  : " , total_travel_time)


    # TO DO: display mean travel time
    
    mean_travel_time = (df['Trip Duration'].mean()).round() 
    #round()will give the rounded off float
       
    print("Average travel time is : ",mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts().to_frame()
    #.value_counts will count unique values in a column
    
    print(user_types)


    # TO DO: Display counts of gender
    
    #try and except is used to avoid exceptional error during run 
    
    try:
        gender = df['Gender'].value_counts()
         
        
        print("counts of gender type : ",gender)
    except:
        print("There is no 'Gender' column in this file.")
   


    # TO DO: Display earliest, most recent, and most common year of birth
    
    
    
    
    try:
        earliest_year = int(df['Birth Year'].min()) 
        
        
        
        
        recent_year = int(df['Birth Year'].max())
        
        
        common_year = int(df['Birth Year'].mode()[0])
        
        
        print("The earliest year of birth: ",earliest_year)
        
        print("The most recent year of birth: " ,recent_year)
        
        print("The most common year of birth: ", common_year)
              
    except:
        print("There are no birth year details in this file.")
       


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_display(df):
    #it will display first 5 rows of raw data upon asked by user.

    i = 0
    while True:
        raw_data = input("if you like to see raw data type yes else no : ").lower()
        if raw_data != 'yes'

        break
    else:
        i = i+5
        print(df.iloc[i:i+5])




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
