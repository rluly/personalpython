import time
import random
import mysql.connector
#order for atts are username,password,highscore,lowest_attempts,total_attempts

f = open("english3.txt")
dictionary = f.read().split()
f.close()
wordlist = []

for ii in dictionary:
    if len(ii)>3 and len(ii)<8:
        wordlist.append(ii)

status = True
print("Your objective in Word Guess is to guess the mystery word each round.\nAfter each guess, you will be told whether the mystery word comes before or after your guess.\nYou will be scored based off both time and number of attempts.")
usercheck = True
newcheck = 0
while(usercheck):
    username = input("Please enter a username to keep track of your highscores: ")

    try:
        #for the .connect() options, fill in the *'s with your own SQL server information
        connection = mysql.connector.connect(host='***',
                                             user='***',
                                             password='***',
                                             database='wordguess')

        sql_select_Query = "select * from user where user.username = \"" + username +"\";"
        #print(sql_select_Query)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = []
        records = cursor.fetchall()
        if len(records)==0:
            password = input("Please enter a password for your new username: ")
            sql_select_Query = "insert into user values(\"" + username + "\",\""+ password + "\",0.0,0,0);"
            cursor.execute(sql_select_Query)
            connection.commit()
            cursor.execute("select * from user where username =\"" + username + "\";")
            records = cursor.fetchall()
            usercheck = False
            newcheck = 1
        else:
            for row in records:
                print("username = ", row[0])
                print("password  = ", row[1])
                print("highscore  = ", row[2], "\n")
                print("lowest_attempts = ", row[3])
                print("total_attempts = ", row[4])
                passcheck = row[1]
                highscore = row[2]
                lowest_attempts = row[3]
                total_attempts = row[4]
            passcheck2 = input("Please enter your password.")
            if passcheck==passcheck2:
                usercheck  = False

    #print("Total number of rows in Laptop is: ", cursor.rowcount)

    #print("\nPrinting each laptop record")
        if(newcheck==1):
            for row in records:
                print("username = ", row[0])
                print("password  = ", row[1])
                print("highscore  = ", row[2], "\n")
                print("lowest_attempts = ", row[3])
                print("total_attempts = ", row[4])
                highscore = row[2]
                lowest_attempts = row[3]
                total_attempts = row[4]

#except Error as e:
    #print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            #print("MySQL connection is closed")

count = 0
while(status):
    starting_point = input("Type any word to start: ")
    index = random.randrange(0,len(wordlist))
    answer = wordlist[index]
    #index2 = random.randrange(0,len(wordlist))
    #compare = wordlist[index2]
    if starting_point>answer:
        print("The mystery word is before your starting word. Your time starts now, good luck!")
    else:
        print("The mystery word is after your starting word. Your time starts now, good luck!")
    status2 = True
    start = time.time()
    while(status2):
        guess = input("Insert your guess: ")
        count += 1
        if guess==answer:
            status2 = False
        elif guess>answer:
            print("Before")
        else:
            print("After")
    end = time.time()
    difference = end-start
    if difference<highscore and total_attempts>0:
        highscore = difference
    elif total_attempts<1:
        highscore = difference
    if count<lowest_attempts and total_attempts>0:
        lowest_attempts = count
    elif total_attempts<1:
        lowest_attempts = count
    total_attempts += 1
    print("You guessed the mystery word, ",answer,"! Your time elapsed was: ",difference, "seconds.")
    status3 = True
    try:
        connection = mysql.connector.connect(host='192.168.150.129',
                                            database='wordguess',
                                            user='superman',
                                             password='DatabaseSystems2!')

        sql_select_Query = "update user set highscore=" + str(highscore) + ",lowest_attempts=" + str(lowest_attempts) + ",total_attempts=" + str(total_attempts) + " where username =\"" + username + "\";"
        print(sql_select_Query)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        connection.commit()
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    while(status3):
        cont = input("Would you like to continue?(Y/N): ")
        cont = cont.upper()
        count = 0
        if cont=="Y":
            status3 = False
        elif cont=='N':
            status = False
            status3 = False
            print("Thank you for playing!")
        else:
            print("Your input was invalid. Please enter either a Y or an N.")
