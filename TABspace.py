#!/usr/bin/env python3

import os
import sys
import json
import passhash
import check_connections
import time
import getpass

# Lets a user view their own profile
def viewProfile(user):
    os.system("clear")
    print("TABspace\n\n")
    profile = database["profiles"][user]
    print("Your current profile:\n")
    print("Your Username: ", user)
    print("Your Favorite Editor: ", profile["editor"])
    print("Your Choice of Tabs or Spaces: ", profile["tabsorspaces"])
    print("Your Favorite Data Structure: ", profile["structure"])
    print("Your Favorite Shell: ", profile["shell"])
    print("Your Favorite Operating System: ", profile["os"])
    print("Your Favorite Cowsay: ", profile["cowsay"])
    input("\nReturn to Main Menu? (Press any key, then ENTER): ")
    os.system("clear")


# Lets a user change their own profile
def changeProfile(user):
    os.system("clear")
    editing = True
    profile = database["profiles"][user]
    print("TABspace\n\n")
    print("Your current profile:")
    print("Your Username: ", user)
    print("0. Your Editor: ", profile["editor"])
    print("1. Your Choice of Tabs or Spaces: ", profile["tabsorspaces"])
    print("2. Your Favorite Data Structure: ", profile["structure"])
    print("3. Your Favorite Shell: ", profile["shell"])
    print("4. Your Favorite Operating System: ", profile["os"])
    print("5. Your Favorite Cowsay: ", profile["cowsay"])

    while (editing):
        change = input("\nWhich field would you like to edit?(number, or \"done\"): ")
        if (change == "0"):
            new_editor = input("What would you like your favorite editor to be set as? ")
            profile["editor"] = new_editor
            print("Field successfully updated!\n")
            time.sleep(1)
        elif (change == "1"):
            tors = input("What would you like your preference for tabs or spaces to be set as? ")
            profile["tabsorspaces"] = tors
            print("Field successfully updated!\n")
            time.sleep(1)
        elif (change == "2"):
            ds = input("What would you like your favorite data structure to be set as? ")
            profile["structure"] = ds
            print("Field successfully updated!\n")
            time.sleep(1)
        elif (change == "3"):
            new_shell = input("What would you like your favorite shell to be set as? ")
            profile["shell"] = new_shell
            print("Field successfully updated!\n")
            time.sleep(1)
        elif (change == "4"):
            new_os = input("What would you like your favorite operating system to be set as? ")
            profile["os"] = new_os
            print("Field successfully updated!\n")
            time.sleep(1)
        elif (change == "5"):
            cow = input("What would you like your favorite cowsay to be set as? ")
            profile["cowsay"] = cow
            print("Field successfully updated!\n")
            time.sleep(1)
        elif (change == "done"):
            print("\nYour profile has been successfully updated!\n")
            time.sleep(2)
            os.system("clear")
            editing = False
            continue
        else:
            print("Please choose a valid option.\n")


# Lets a user view their current friends
def viewFriends(user):
    os.system("clear")
    print("TABspace\n\n")
    friends = database["profiles"][user]["friends"]
    print("Your current friends:\n")
    if not friends:
        print("You currently have no friends :(\n")
    for friend in friends:
        print(friend)
    input("\nReturn to Main Menu? (Press ENTER): ")
    os.system("clear")


# Shows people who are similar to the user
# Lets a user send another user a friend request
def addFriends(user, first_call=True):
    os.system("clear")
    print("TABspace\n\n")
    matches = check_connections.make_connections(user)
    print("Here are some people you have a lot in common with:")
    for match in matches:
        if (len(match) > 5):
            print(match, ":\t", round(matches[match]/.08, 2), " percent similar")
        else:
            print(match, ":\t\t", round(matches[match]/.08, 2), " percent similar")
    print("")
    add = "y"
    if (first_call):
        add = input("Would you like to add anyone? (y/n): ")
    if (add == "y"):
        new_friend = input("Who would you like to add? (Please enter a valid username): ")
        if new_friend not in database["profiles"]:
            print("Sorry, but they do not appear to be using TABspace\n")
        elif new_friend in database["profiles"][user]["friends"]:
            print("This person is already in your friends list!")
        elif new_friend == user:
            print("You can't add yourself as a friend!")
        else:
            database["profiles"][new_friend]["requests"].append(user)
            print("You have successfully sent ", new_friend, " a friend request!\n")
        bad_input = True
        while (bad_input):
            answer = input("\nWould you like to add someone else?(y/n): ")
            if (answer == "y"):
                bad_input = False
                addFriends(user, False)
            elif (answer == "n"):
                bad_input = False
                os.system("clear")
                return
            else :
                print("Please choose a valid option")
    elif (add == "n"):
        os.system("clear")
        return
    else:
        print("Please choose a valid option")
        time.sleep(2)
        addFriends(user)


# Lets a user view their current friend requests and choose to accept or reject them
def viewRequests(user):
    os.system("clear")
    print("TABspace\n\n")
    for request in database["profiles"][user]["requests"]:
        adding = True
        while adding:
            print(request)
            string = "Would you like to accept " + request + "'s friend request?(y/n): "
            decision = input(string)
            if (decision == "y"):
                database["profiles"][user]["friends"].append(request)
                database["profiles"][request]["friends"].append(user)
                database["profiles"][user]["requests"].remove(request)
                print(request, " has been successfully added to your friends list!\n")
                adding = False
            elif (decision == "n"):
                database["profiles"][user]["requests"].remove(request)
                print(request, " has not been added to your friends list.\n")
                adding = False
            else:
                print("Please choose a valid option.")
    input("\nReturn to Main Menu? (Press ENTER): ")
    os.system("clear")
    return


# Lets a user view another user's profile
# If the other user is their friend they can see everything and if not they can only see their favorite editor
def viewOther(user):
    os.system("clear")
    print("TABspace\n\n")
    view = input("Whose profile would you like to view? ")
    if view not in database["profiles"]:
        print("Sorry, but they do not appear to be using TABspace!\n")
        input("\nReturn to Main Menu? (Press ENTER): ")
        os.system("clear")
        return
    if view == user:
        viewProfile(user)
    elif (view in database["profiles"][user]["friends"]): # If friends
        profile = database["profiles"][view]
        print(view, "'s Favorite Editor: ", profile["editor"])
        print(view, "'s Choice of Tabs or Spaces: ", profile["tabsorspaces"])
        print(view, "'s Favorite Data Structure: ", profile["structure"])
        print(view, "'s Favorite Shell: ", profile["shell"])
        print(view, "'s Favorite Operating System: ", profile["os"])
        print(view, "'s Favorite Cowsay: ", profile["cowsay"])
        input("\nReturn to Main Menu? (Press ENTER): ")
        os.system("clear")
    else: # If not friends
        profile = database["profiles"][view]
        print(view, "'s Favorite Editor: ", profile["editor"])
        print("Add ", view, " as a friend to learn more about them!")
        badResponse = True
        while badResponse:
            seeMutual = input("Would you like to see your mutual friends?(y/n): ")
            if (seeMutual == "y"):
                badResponse = False
                mutualFriends = check_connections.mutual_friends(user, view)
                if mutualFriends:
                    print("Your Mutual Friends:")
                else:
                    print("You have no mutual friends with ", view, ".")
                for mutual in mutualFriends:
                    print(mutual)
            elif (seeMutual == "n"):
                badResponse = False
            else:
                print("Please choose a valid option")

        input("\nReturn to Main Menu? (Press ENTER): ")
        os.system("clear")

# Lets a user send a message to another user
def sendMessage(user):
    os.system("clear")
    print("TABspace\n\n")
    sendTo = input("Who would you like to send a message to? ")
    if sendTo not in database["profiles"]:
        print("Sorry, but they do not appear to be using TABspace!\n")
        input("\nReturn to Main Menu? (Press ENTER): ")
        os.system("clear")
        return
    message = input("What would you like to send?\nYour message: ")
    string = (user + ": " + message)
    database["profiles"][sendTo]["messages"].insert(0, string)
    print("Message sent!\n")
    input("\nReturn to Main Menu? (Press ENTER): ")
    os.system("clear")


# Lets a user view messages they have been sent
def viewMessages(user):
    os.system("clear")
    print("TABspace\n\n\nCurrent Messages:\n")
    counter = 0
    for message in database["profiles"][user]["messages"]:
        print(str(counter) + ".", message)
        counter = counter + 1
    input("\nReturn to Main Menu? (Press ENTER): ")
    os.system("clear")


# Lets a user choose what they want to do when they are logged in
def online(user):
    logged_in = True
    while logged_in:
        print("TABspace\n\n\nWhat would you like to do?")
        action = input("0. View Profile\n1. Edit Profile\n2. View Friends\n3. Add Friends\n4. View Friend Requests\n5. View Another Profile\n6. Send Message\n7. View Messages\n8. Log Off\nChoice: ")
        print("")
        if (action == "0"):
            viewProfile(user)
        if (action == "1"):
            changeProfile(user)
        if (action == "2"):
            viewFriends(user)
        if (action == "3"):
            addFriends(user)
        if (action == "4"):
            viewRequests(user)
        if (action == "5"):
            viewOther(user)
        if (action == "6"):
            sendMessage(user)
        if (action == "7"):
            viewMessages(user)
        if (action == "8"):
            with open("newdatabase.json", 'w') as f:
                f.write(json.dumps(database, sort_keys=True, indent=4))
            print("You are now logged out.\n")
            time.sleep(2)
            logged_in = False # Probably don't need, can just exit the whole program instead
            exit()



# Beginning of main program
database = {}
#database = json.loads(open("database.json").read())
with open("newdatabase.json", 'r') as f:
    database = json.load(f)
print("\nWelcome to TABspace, a social networking program for comp sci nerds.\n")


logged_in = False
while (not logged_in):
    print("What would you like to do?\n")
    choice = input("0. Login\n1. Create a new account\nChoice: ")

    if (choice == "0"): # Logging in
        username = input("\nPlease enter your username: ")
        if (username not in database["profiles"]):
            print("That does not appear to be a valid username.\n")
            continue

        password = getpass.getpass("Please enter your password: ")
        if (database["profiles"][username]["password"] != passhash.hash(password)):
            print("That is an incorrect password.\n")
            continue

        logged_in = True
        os.system("clear")
        online(username)

    elif (choice == "1"): # Creating account
        invalid_username = True
        while invalid_username:
            new_username = input("Please enter a username: ")
            if (new_username in database["profiles"]):
                print("That username is already taken!\n")
                continue
            else:
                invalid_username = False
                new_password = getpass.getpass("Please enter a password: ")
                database["profiles"][new_username] = {"editor": "", "messages": [], "password": passhash.hash(new_password), "shell": "", "structure": "", "tabsorspaces": "", "os": "", "cowsay": ""}
        print("Your account has been created, make sure to update all of your preferences. We hope you enjoy TABspace!\n")
        time.sleep(4)
        os.system("clear")
        online(new_username)
        continue

    else:
        print("Please enter a valid option.\n")
        time.sleep(2)
        os.system("clear")
