from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel,QButtonGroup)
from random import *

class Question():
    def __init__ (self,question,right_answer,wrong_1,wrong_2,wrong_3 ):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

questions_list = []
questions_list.append(Question("When was Indonesia's independance day",'1945','1745','1990','1946'))
questions_list.append(Question("what is the most important organ in the body(from the list)",'Heart','leg','finger','teeth'))
questions_list.append(Question("what is the most popular phone brand in america",'Apple','xiomi','samsung','oppo'))
questions_list.append(Question("what food is most known for in alaska",'King crab','chilli','fish','potato'))
questions_list.append(Question("how much is the convertion rate of usd to idr(in june of 2026)",'18000','18999','17000','19460'))
# General Knowledge & Geography
questions_list.append(Question("What is the capital city of Australia", 'Canberra', 'Sydney', 'Melbourne', 'Brisbane'))
questions_list.append(Question("Which country is completely surrounded by South Africa", 'Lesotho', 'Swaziland', 'Botswana', 'Namibia'))
questions_list.append(Question("What is the smallest country in the world", 'Vatican City', 'Monaco', 'San Marino', 'Maldives'))
questions_list.append(Question("Which river is the longest in the world", 'Nile', 'Amazon', 'Yangtze', 'Mississippi'))
questions_list.append(Question("In which ocean is the Mariana Trench located", 'Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean'))

# Science & Nature
questions_list.append(Question("What is the chemical symbol for gold", 'Au', 'Ag', 'Gd', 'Go'))
questions_list.append(Question("Which planet in our solar system is known for its prominent rings", 'Saturn', 'Jupiter', 'Neptune', 'Mars'))
questions_list.append(Question("What is the hardest natural substance on Earth", 'Diamond', 'Graphene', 'Ruby', 'Quartz'))
questions_list.append(Question("How many bones are there in an adult human body", '206', '186', '216', '256'))
questions_list.append(Question("Which gas do plants absorb from the atmosphere for photosynthesis", 'Carbon dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'))

# Pop Culture & Tech
questions_list.append(Question("Who directed the movie 'Inception'", 'Christopher Nolan', 'Steven Spielberg', 'Quentin Tarantino', 'James Cameron'))
questions_list.append(Question("Which social media platform limits original posts to short character counts and was rebranded as X", 'Twitter', 'Instagram', 'Facebook', 'LinkedIn'))
questions_list.append(Question("What is the highest-grossing film of all time worldwide", 'Avatar', 'Avengers: Endgame', 'Titanic', 'Star Wars: The Force Awakens'))
questions_list.append(Question("Which video game features a world made completely of blocks and allows players to mine resources", 'Minecraft', 'Roblox', 'Terraria', 'Fortnite'))
questions_list.append(Question("Who sang the hit song 'Shape of You'", 'Ed Sheeran', 'Justin Bieber', 'Bruno Mars', 'Shawn Mendes'))

# History & World Events
questions_list.append(Question("In which year did the Titanic sink", '1912', '1905', '1920', '1898'))
questions_list.append(Question("Who was the first President of the United States", 'George Washington', 'Thomas Jefferson', 'Abraham Lincoln', 'John Adams'))
questions_list.append(Question("Which empire built the Colosseum in Rome", 'Roman Empire', 'Greek Empire', 'Persian Empire', 'Byzantine Empire'))
questions_list.append(Question("What year did World War II officially end", '1945', '1918', '1939', '1950'))
questions_list.append(Question("Who was the first woman to win a Nobel Prize", 'Marie Curie', 'Rosalind Franklin', 'Ada Lovelace', 'Mother Teresa'))

# Sports
questions_list.append(Question("How many players are on the field for one team in a standard soccer match", '11', '10', '12', '9'))
questions_list.append(Question("Which country host-won the first ever FIFA World Cup in 1930", 'Uruguay', 'Brazil', 'Argentina', 'Italy'))
questions_list.append(Question("What sport uses a shuttlecock", 'Badminton', 'Tennis', 'Squash', 'Table Tennis'))
questions_list.append(Question("How many rings make up the official Olympic logo", '5', '4', '6', '7'))
questions_list.append(Question("Which basketball player is nicknamed 'King James'", 'LeBron James', 'Michael Jordan', 'Kevin Durant', 'Stephen Curry'))

# Food & Drink
questions_list.append(Question("What is the main ingredient in traditional Japanese guacamole-alternative, Wasabi", 'Horseradish', 'Avocado', 'Green peas', 'Broccoli'))
questions_list.append(Question("Which country is credited with inventing pizza", 'Italy', 'Greece', 'France', 'United States'))
questions_list.append(Question("What beverage is known as 'the drink of the gods' in ancient Mayan culture", 'Hot chocolate', 'Wine', 'Coffee', 'Chicha'))
questions_list.append(Question("From which plant is commercial white sugar most commonly derived", 'Sugarcane', 'Sweet potato', 'Maple tree', 'Corn'))
questions_list.append(Question("What flavor is traditional Cointreau liqueur", 'Orange', 'Lemon', 'Apple', 'Almond'))

# Animals & Wildlife
questions_list.append(Question("What is the largest mammal currently living on Earth", 'Blue whale', 'African elephant', 'Colossal squid', 'Giraffe'))
questions_list.append(Question("How many hearts does an octopus have", '3', '1', '2', '4'))
questions_list.append(Question("Which bird is widely known for its ability to mimic human speech perfectly", 'Parrot', 'Crow', 'Eagle', 'Pigeon'))
questions_list.append(Question("What is a group of lions called", 'A pride', 'A pack', 'A herd', 'A flock'))
questions_list.append(Question("Which mammal is capable of true, sustained flight", 'Bat', 'Flying squirrel', 'Sugar glider', 'Flying lemur'))

# Art & Literature
questions_list.append(Question("Who painted the famous 'Mona Lisa'", 'Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Michelangelo'))
questions_list.append(Question("Who wrote the classic tragedy play 'Romeo and Juliet'", 'William Shakespeare', 'Charles Dickens', 'Mark Twain', 'Jane Austen'))
questions_list.append(Question("What is the primary color missing from this list: Red, Yellow, and...", 'Blue', 'Green', 'Purple', 'Orange'))
questions_list.append(Question("Which famous wizard attended Hogwarts School of Witchcraft and Wizardry", 'Harry Potter', 'Gandalf', 'Merlin', 'Dumbledore'))
questions_list.append(Question("In what country is the Louvre Museum located", 'France', 'Italy', 'Spain', 'United Kingdom'))

# Space & Astronomy
questions_list.append(Question("What is the hottest planet in our solar system", 'Venus', 'Mercury', 'Mars', 'Jupiter'))
questions_list.append(Question("Approximately how long does it take for light from the Sun to reach Earth", '8 minutes', '8 seconds', '8 hours', 'Instantly'))
questions_list.append(Question("What is the name of the first artificial satellite launched into space by humans", 'Sputnik 1', 'Apollo 11', 'Voyager 1', 'Hubble'))
questions_list.append(Question("Which galaxy is closest to our own Milky Way galaxy", 'Andromeda', 'Triangulum', 'Large Magellanic Cloud', 'Sombrero'))
questions_list.append(Question("What force keeps planets orbiting around the Sun", 'Gravity', 'Magnetism', 'Centrifugal force', 'Friction'))

# Mixed Miscellaneous
questions_list.append(Question("How many days are there in a standard leap year", '366', '365', '364', '367'))
questions_list.append(Question("What is the national currency of Japan", 'Yen', 'Won', 'Yuan', 'Ringgit'))
questions_list.append(Question("Which company developed the Windows operating system", 'Microsoft', 'Apple', 'Google', 'IBM'))
questions_list.append(Question("What does the 'VIP' acronym stand for", 'Very Important Person', 'Very Insecure Passport', 'Visually Important Person', 'Verified Institutional Player'))
questions_list.append(Question("How many total keys are on a standard classical piano", '88', '76', '92', '80'))

app = QApplication([])

btn_OK = QPushButton('Answer')
lb_Question = QLabel('The most difficult question in the world!')

RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?') 
lb_Correct = QLabel('the answer will be here!') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 

def show_result():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    btn_OK.setText('Next question')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def check_answer():
    if btn_OK.text() == "Answer":
        show_correct()
    else:
        next_question()

Answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(Answers)
    Answers[0].setText(q.right_answer)
    Answers[1].setText(q.wrong_1)
    Answers[2].setText(q.wrong_2)
    Answers[3].setText(q.wrong_3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def next_question():
    window.total += 1
    window.cur_question = randint(0,len(questions_list)-1)
    q = questions_list[window.cur_question]
    ask(q)

def show(res):
    lb_Result.setText(res)
    show_result()

def show_correct():
    if Answers[0].isChecked():
        show("Correct!")
        window.score += 1
        print("Statistic")
        print("-Total questions:",window.total)
        print("-Right answers:",window.score)
        print("-Rating:",window.score / window.total *100)
    else:
        if Answers[1].isChecked() or Answers[2].isChecked() or Answers[3].isChecked():
            show("Incorrect!")
            print("Statistic")
            print("-Total questions:",window.total)
            print("-Right answers:",window.score)
            print("-Rating:",window.score / window.total *100)
        


btn_OK.clicked.connect(check_answer)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(600,400)
window.score = 0
window.total = 0
next_question()
window.show()

app.exec()