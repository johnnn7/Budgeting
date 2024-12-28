ver-1.1-command-line
Very much beginner and version one of this project. With ability for take in a budget then give you a balance aft you log in your expenses.

VERSION 1.1:

    Added the number of current categories from 3 to 5.  
        "🍟 Food",
        "🔟 Tithe",
        "🚗 Transportation",
        "📚 Schooling",
        "💩 Unnessesary"
    
    Updated so users are able to set their own budget. this happens by first the user themself runing "python3 expense_tracker.py start" and they will be prompted to in their budget which will be saved as a str in a txt file now. 
    
    Then additionally, once the user runs "expense_tracker.py log" they will be able to log a new expense that will be subtracted from their budget in the backend.

    When "python3 expense_tracker.py summarize" summarize is run, if there has been to budget established the user will be told to make a budget first and given the command to run in order to get the code to work. if a budget was already set then the program will give out the totals of each category, the total that has been spent, the remaining budget, and the max you could spend each day and stay in budget.


