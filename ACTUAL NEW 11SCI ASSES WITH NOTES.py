def quiz():

    print ("Your goal is to score 60% or over otherwise you fail")
    # This is where the code will get their information to use as a quiz
    quiz1= {"What movie has Julian Dennison and Ryan Ryenolds. \n a) Finding Nemo \n b) Green Lantern \n c) Oppenheimer \n d) Deadpool 2 \n ":'d',
            "What country is Julian Dennison from? \n a) Canada \n b) Russia \n c) Moldova \n d) New Zealand \n ":'d',
            "Who is Julian Dennison’s mum? \n a) Mabelle Dennison \n b) Dwayne Johnson \n c) Tony Stark \n d) Wonder Woman \n":'a',
            "When was Julian Dennison born? \n a) 30th of February 2008 \n b) 19 September 2002 \n c) 26 October 2054 \n d) 26 October 26 2002":'d',
            "What ethnicity is Julian Dennison? \n a) Chinese \n b) Maori \n c) Hawaiian \n d) Chicken BBQ Sausage":'b',}
    play ="y"
    while play == "y":
      score = 0
      for x in  quiz1:
        print(x)
        # Takes the user input the match with the dictionary to see if their answer is valid or invalid
        user_input = input("Please answer the question using a, b, c or d.\n Enter Answer: "). lower(). strip()
        # If user input matches the dictionary then the code will say "Correct!"
        if user_input == (quiz1[x]):
          print("Correct!")
          score = score + 20
          # If the input doesn't match the dictionary then the code will think it's wrong and will print "Incorrect!"
        else:
          print("Incorrect!")
        print (quiz1[x])
      # By making a variable labeled as score and for each time the user gets an answer right they get +20 score that gets added up at the end as a percentage
      print("You scored", score, "%")
      # This code makes it so if you have below or 60 and above you will either pass or fail.
      if score >= 60:
        print ("You have passed this test")
      else:
        print ("You have failed this test")
        # This asks the user if they would like to redo the test again.
      play = input("Would you like to play again? y/n \n Enter: "). lower(). strip()
quiz()
