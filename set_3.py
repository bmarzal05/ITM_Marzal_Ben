'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def find_IG_from(from_member):
        if from_member.find(" ") < 0:
            if from_member in social_graph:
                return from_member
            else:
                return "Instagram handle not found."
        if from_member.find(" ")>0:
            name=list(from_member.split(" "))
            first_name=name[0]
            first_name=first_name.title()
            last_name=name[1]
            last_name=last_name.title()

            matches = [
                handle for handle, details in social_graph.items()
                if details['first_name'].title() == first_name and details['last_name'].title() == last_name
            ]
            if matches:
                return ''.join(matches)
            else:
                return "No matching Instagram handle found."
    find_IG_from=str(find_IG_from(from_member))
    def find_IG_to(to_member):
        if to_member.find(" ") < 0:
            if to_member in social_graph:
                return to_member
            else:
                return "Instagram handle not found."
        if to_member.find(" ")>0:
            name=list(to_member.split(" "))
            first_name=name[0]
            first_name=first_name.title()
            last_name=name[1]
            last_name=last_name.title()

            matches = [
                handle for handle, details in social_graph.items()
                if details['first_name'].title() == first_name and details['last_name'].title() == last_name
            ]
            if matches:
                return ''.join(matches)
            else:
                return "No matching Instagram handle found."
    find_IG_to=str(find_IG_to(to_member))

    def check_following(find_IG_from, find_IG_to):
        if find_IG_from in social_graph:
            from_details = social_graph[find_IG_from]
            if 'following' in from_details and find_IG_to in from_details['following']:
                return True
            else: 
                return False
    check_following=check_following(find_IG_from, find_IG_to)
    
    if check_following is True: 
        if find_IG_to in social_graph: 
            to_details=social_graph[find_IG_to]
            if 'following' in to_details and find_IG_from in to_details['following']:
                return "friends"
            else: 
                return "follower"
    elif check_following is False:
        if find_IG_to in social_graph: 
            to_details=social_graph[find_IG_to]
            if 'following' in to_details and find_IG_from in to_details['following']:
                return "followed by"
            else: 
                return "no relationship"
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@eeebeee"
                  ]
    },
}

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def check_horizontals(board):
        for row in board:
            if row[0] != '' and all(cell == row[0] for cell in row):
                return row[0]
        return None
    check_horizontals=check_horizontals(board)

    def check_verticals(board):
        checker=""
        index=0
        while index<len(board):
            for lists in board:
                checker+=lists[index]
            if str(checker) == "O"*len(board) or str(checker)== "X"*len(board):
                return lists[index]
                break
            else:
                index+=1
                checker=""
                continue
    check_verticals=check_verticals(board)

    def check_diagonals(board):
        n = len(board) 
        diagonal_winner1 = board[0][0]
        for i in range(1, n):
            if board[i][i] != diagonal_winner1:
                diagonal_winner1 = None
                break
        if diagonal_winner1 and diagonal_winner1 != '':
            return diagonal_winner1
        diagonal_winner2 = board[0][n-1]
        for i in range(1, n):
            if board[i][n-1-i] != diagonal_winner2:
                diagonal_winner2 = None
                break
        if diagonal_winner2 and diagonal_winner2 != '':
            return diagonal_winner2
        return None

    check_diagonals=check_diagonals(board)

    if check_horizontals =="X": 
        return "X"
    elif check_horizontals=="O":
        return "O"
    elif check_verticals =="X": 
        return "X"
    elif check_verticals=="O":
        return "O"
    elif check_diagonals=="X":
        return "X"
    elif check_diagonals=="O":
        return "O"
    else: 
        return "NO WINNER"
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_time=0
    current_stop=first_stop
    while True:
        found_next_stop=False
        for (stop1, stop2), time_travelled in route_map.items():
            if stop1== current_stop:
                total_time+= time_travelled["travel_time_mins"]
                current_stop= stop2
                found_next_stop= True
                if stop2== second_stop:
                    return total_time
        if not found_next_stop:
            return None