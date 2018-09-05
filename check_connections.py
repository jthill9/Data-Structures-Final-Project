#!/usr/bin/env python3

# Checks connections between users to recommend friends

import sys
import os
import json

# Finds the 10 people that someone is the most similar to but not friends with
def make_connections(user):
    database = {}
    with open("newdatabase.json", 'r') as f:
        database = json.load(f)

    people = database["profiles"]
    recommendations = {}
    scores = []

    for other_user in people:
        if (user == other_user):
            continue
        if (other_user in people[user]["friends"]):
            continue

        score = 0;
        if (people[user]["editor"].lower() == people[other_user]["editor"].lower()):
            score = score + 1;
        if (people[user]["shell"].lower() == people[other_user]["shell"].lower()):
            score = score + 1;
        if (people[user]["structure"].lower() == people[other_user]["structure"].lower()):
            score = score + 2;
        if (people[user]["tabsorspaces"].lower() == people[other_user]["tabsorspaces"].lower()):
            score = score + 1;
        if (people[user]["os"].lower() == people[other_user]["os"].lower()):
            score = score + 1;
        if (people[user]["cowsay"].lower() == people[other_user]["cowsay"].lower()):
            score = score + 2;

        if (len(recommendations) < 10):
            recommendations[other_user] = score;
            scores.append(score)

        elif scores:
            if (score > min(scores)):
                lowest_score = min(scores)
                for match in recommendations:
                    if (recommendations[match] == lowest_score):
                        del recommendations[match]
                        recommendations[other_user] = score
                        for index in range(len(scores)):
                            if (scores[index] == lowest_score):
                                scores.remove(scores[index])
                                break
                        break

    return recommendations


# Returns all the mutual friends between two users
def mutual_friends(user, other):
    database = {}
    with open("newdatabase.json", 'r') as f:
        database = json.load(f)

    user_friends = set()
    other_friends = set()
    mutualFriends = set()
    for friend in database["profiles"][user]["friends"]:
        user_friends.add(friend)
    for mutual in database["profiles"][friend]["friends"]:
        other_friends.add(mutual)

    for friend in user_friends:
        if friend in other_friends:
            mutualFriends.add(friend)

    return mutualFriends


# Generates an adjacency list of all friends
def friends_adjacency_list():
    database = {}
    with open("newdatabase.json", 'r') as f:
        database = json.load(f)

    friends_list = {}
    for user in database["profiles"]:
        friends_list[user] = database["profiles"][user]["friends"]

    return friends_list
