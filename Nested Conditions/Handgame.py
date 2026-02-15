#Abhinav and anjali are playing a game called Rock-Paper-Scissors.Its a hand game usually played b/w
#two people.In this game, they both show their hands in one of three ways.Rock,Paper or Scissors.Ex:
#If Abhinav shows Rock and Anjali shows Scissors,Abhinav wins bcoz Rock blunts Scisscors.
#If Anjali shows Paper and Abhinav shows Scissors,Abhinav wins bocoz Scissors cut Paper.
#If Abhinav shows Paper and Anjali shows Rock,Abhinav wins bocoz Paper wraps Rock.
#If both players show the same thing,Its a tie.For example,if Abhinav and Anjali both show Rock,its a tie.
#i/p:    Rock       o/p: Anjali Wins  i/p:  Scissors    o/p:    Anjali Wins 
#        Paper                              Rock

abhinav_input=input()
anjali_input=input()
if abhinav_input==anjali_input:
    print("Tie")
elif abhinav_input == "Paper" and anjali_input == "Scissors":
    print("Anjali Wins")
elif abhinav_input=="Scissors" and anjali_input=="Paper":
    print("Abhinav Wins")
elif abhinav_input=="Paper" and anjali_input=="Rock":
    print("Abhinav Wins")
elif abhinav_input=="Rock" and anjali_input=="Paper":
    print("Anjali Wins")
elif abhinav_input=="Rock" and anjali_input=="Scissors":
    print("Abhinav Wins")
elif abhinav_input=="Scissors" and anjali_input=="Rock":
    print("Anjali Wins")
