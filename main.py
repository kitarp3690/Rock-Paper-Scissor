"""
    Tic-Tac-Toe Game

    This program demostrate a simple GUI Tic-Tac-Toe game using python with tkinter toolkit

    Developer: Pratik Shrestha

    Date: 2024/ 03/ 23

"""

import tkinter as tk
import random
from tkinter import PhotoImage


# I  have used staticmethod decorator becuase i dont need instance ( since the value of attributes are not changed in this program)
class RPS:
    @staticmethod
    def front_page():
        """This method generates the 1st page of the game"""
        root = tk.Tk()
        root.title("Rock Paper Scissor")
        root.geometry("700x600")
        root.resizable(False, False)

        # loading images for buttons
        rock_image = PhotoImage(file="rock.png")
        paper_image = PhotoImage(file="paper.png")
        scissor_image = PhotoImage(file="scissor.png")

        tictactoe=tk.Label(root,text="  Tic-Tac-Toe  ",font=("Times New Roman",30,"bold"),padx=10,pady=5,fg="#509AEE")
        tictactoe.grid(row=0,column=1)

        message=tk.Label(root,text="Choose : ",font=("vogan",30,"bold"),fg="#25F344")
        message.grid(row=1,column=1)

        # creating buttons
        rock_button = tk.Button(root,padx=10 ,width=150, height=150, image=rock_image, command=lambda: RPS.on_button_click(root, "rock"), borderwidth=2, relief="solid", cursor="hand2")
        paper_button = tk.Button(root, padx=10,width=150, height=150, image=paper_image, command=lambda: RPS.on_button_click(root, "paper"), borderwidth=2, relief="solid", cursor="hand2")
        scissor_button = tk.Button(root, padx=10,width=150, height=150, image=scissor_image, command=lambda: RPS.on_button_click(root, "scissor"), borderwidth=2, relief="solid", cursor="hand2")

        # creating buttons name using label
        rock_name=tk.Label(root,text="Rock",font=("Gotham", 16,"bold"),fg="#D72D2D")
        paper_name=tk.Label(root,text="Paper",font=("Gotham", 16,"bold"),fg="#D72D2D")
        scissor_name=tk.Label(root,text="Scissor",font=("Gotham", 16,"bold"),fg="#D72D2D")


        # placing buttons
        rock_button.grid(row=2, column=0)
        paper_button.grid(row=2, column=1)
        scissor_button.grid(row=2, column=2)

        # placing names of button
        rock_name.grid(row=3,column=0)
        paper_name.grid(row=3,column=1)
        scissor_name.grid(row=3,column=2)

        root.mainloop()

    @staticmethod
    def on_button_click(root, player_choice):
        """This method is used when a button is clicked in the front_page"""
        # generating computer's choice
        computer_choice = RPS.generate_computer_choice()
        # checking winner 
        RPS.check_winner(root, player_choice, computer_choice)

    @staticmethod
    def generate_computer_choice():
        """This method generates the random choice for computer"""
        choices = ["rock", "paper", "scissor"]
        return random.choice(choices)

    @staticmethod
    def check_winner(root, player_choice, computer_choice):
        """This method is used to check the winner"""
        if player_choice == computer_choice:
            msg = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissor") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissor" and computer_choice == "paper"):
            msg = "You win!"
        else:
            msg = "Computer wins!"
        RPS.display_result(root, player_choice, computer_choice, msg)

    @staticmethod
    # Function to change button color on hover
    def on_enter(event,butt):
        """This method is used to show bg(background) color when mouse cursor is hovered in that button"""
        butt.config(bg="#35E375")

    # Function to change button color back when mouse leaves
    def on_leave(event,butt):
        """This method is used to change the bg color to normal state color when mouse cursor leaves that button"""
        butt.config(bg="SystemButtonFace")

    @staticmethod
    def display_result(root, player_choice, computer_choice, msg):
        """This method is used to create new window to show output and asks whether to continue program or not"""
        # Close the previous window
        root.destroy()
        
        # Create a new window to display result
        new_root = tk.Tk()
        new_root.title("Rock Paper Scissor")
        new_root.geometry("700x600")
        new_root.resizable(False, False)

        # Load images for new window
        rock_image = PhotoImage(file="rock.png")
        paper_image = PhotoImage(file="paper.png")
        scissor_image = PhotoImage(file="scissor.png")

        # display player's choice
        player_label = tk.Label(new_root, text="Your choice", font=("Helvetica", 16), relief="solid", padx=10)
        player_label.grid(row=0, column=0)
        if player_choice == "rock":
            player_image = tk.Label(new_root, image=rock_image)
        elif player_choice == "paper":
            player_image = tk.Label(new_root, image=paper_image, width=150,height=150)
        elif player_choice == "scissor":
            player_image = tk.Label(new_root, image=scissor_image, width=150, height=150)
        player_image.grid(row=1, column=0)
        # display player's choice in text
        pl_choice=tk.Label(new_root,text=player_choice,font=("Gotham",16,"bold"))
        pl_choice.grid(row=2,column=0)

        # display computer's choice in picture
        computer_label = tk.Label(new_root, text="Computer's choice", font=("Helvetica", 16), relief="solid", padx=10)
        computer_label.grid(row=0, column=1)
        if computer_choice == "rock":
            computer_image = tk.Label(new_root, image=rock_image, width=150, height=150)
        elif computer_choice == "paper":
            computer_image = tk.Label(new_root, image=paper_image, width=150, height=150)
        elif computer_choice == "scissor":
            computer_image = tk.Label(new_root, image=scissor_image, width=150, height=150)
        computer_image.grid(row=1, column=1)
        # display player's choice in text
        pl_choice=tk.Label(new_root,text=computer_choice,font=("Gotham",16,"bold"))
        pl_choice.grid(row=2,column=1)

        # Display result (showing light green if won and light red if loss or draw)
        if msg=="You win!": 
            result_label = tk.Label(new_root, text=msg, font=("Helvetica", 16), relief="solid", padx=10,bg="#3FED54")
        else:
            result_label = tk.Label(new_root, text=msg, font=("Helvetica", 16), relief="solid", padx=10,bg="#F22929")
        result_label.grid(row=1, column=2)

        question=tk.Label(new_root,text="Do you want to play again?",font=("Helvetica", 16),relief="solid")
        # question.grid(row=7,column=0)
        question.place(x=200,y=280)
        yes_button=tk.Button(new_root,text="Yes",font=("Helvetica", 16,"bold"), relief="solid",padx=20,pady=10,cursor="hand2",command=lambda: RPS.if_yes(new_root))
        # yes_button.bind("<Enter>",RPS.on_enter(event=RPS,butt=yes_button))
        yes_button.bind("<Enter>", lambda event: RPS.on_enter(event,yes_button))
        yes_button.bind("<Leave>", lambda event: RPS.on_leave(event,yes_button))
        yes_button.place(x=180,y=360)
        no_button=tk.Button(new_root,text="No",font=("Helvetica", 16,"bold"), relief="solid",padx=20,pady=10,cursor="hand2",command=lambda: RPS.if_no(new_root))
        # no_button.bind("<Leave>",RPS.on_leave(event=RPS,butt=no_button))
        no_button.bind("<Enter>", lambda event: RPS.on_enter(event,no_button))
        no_button.bind("<Leave>", lambda event: RPS.on_leave(event,no_button))
        no_button.place(x=380,y=360)
        new_root.mainloop()
    
    @staticmethod
    def if_yes(newroot):
            """This method is used when user chooses to continue. It recreates the home page(i.e. frontpage)"""
            newroot.destroy()
            RPS.front_page()
    
    @staticmethod
    def if_no(newroot):
            """This method is used when user chooses not to continue program. It ends(quits) the program"""
            newroot.destroy()

if __name__ == "__main__":
    RPS.front_page()