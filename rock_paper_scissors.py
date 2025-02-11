import random
import time
 





rock = '''
         _______
     ---'   ____)
           (_____)
           (_____)
           (____)
     ---.__(___)
     ''',
     
paper = '''
                 _______
     ---'   ____)____
               ______)
               _______)
              _______)
     ---.__________)
     
     ''',
     
     
scissors = '''
            _______
     ---'   ____)____
               ______)
            __________)
           (____)
     ---.__(___)
     '''

while True:
    user_choice = int(input("Type 0 for rock , 1 for paper and 2 for scissors and 3 to exit"))
    cases = {
      0 : '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      ''',
      1 : '''
                  _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
      
      ''',
      2: '''
             _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
      ''',
      3: "finished"
      
      }

    print(cases.get(user_choice , "Not valid"))
    
    
   
    
    positions = [rock , paper ,scissors]
    n = random.randint(0 , len(positions) - 1)
    computer_choice = positions[n]
    time.sleep(2)
    print(f"computer choice : {computer_choice} ")
    if user_choice == 3:
        break
    elif n == user_choice:
        print("it's a draw")
    elif user_choice == 0 and n == 2:
        print("You win")
    elif n > user_choice:
        print("You lose")
    
    
    



