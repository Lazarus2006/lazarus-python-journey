# quiz 


questions = ("Which of the following organs is primarily responsible for pumping blood throughout the body?",
             "What is the SI unit of force?",
             "What is the chemical symbol for the element Gold?",
             "Which cellular component is often referred to as the powerhouse of the cell because it generates most of the cell's supply of ATP?",
             "What gas makes up the majority of Earth's atmosphere?",
             "When light passes from air into water, what phenomenon causes the light ray to bend?",
             "The process by which a solid turns directly into a gas without first becoming a liquid is called:",
             "In the Linnaean system of classification, which grouping is broader than Family but narrower than Class?",
             "Which planet in our solar system is known for its prominent system of rings?",
             "The principle that states that energy cannot be created or destroyed, only transformed from one form to another, is known as the:")
            
options = [("A. Lungs", "B. Liver", "C. Heart", "D. Kidneys"),
    ("A. Joule", "B. Watt","C. Hertz", "D. Newton"),
    ("A. Gd","B. Ag", "C. Hg","D. Au"),
    ("A. Nucleus", "B. Ribosome", "C. Endoplasmic Reticulum", "D. Mitochondrion"),
    ("A. Oxygen","B. Carbon Dioxide", "C. Argon", "D. Nitrogen"),
    ("A. Reflection", "B. Dispersion", "C. Diffraction", "D. Refraction"),
    ("A. Melting", "B. Condensation", "C. Evaporation", "D. Sublimation"),
    ("A. Species", "B. Genus", "C. Order", "D. Phylum"),
    ("A. Mars", "B. Jupiter", "C. Uranus", "D. Saturn"),
    ("A. Law of Thermodynamics", "B. Law of Conservation of Energy", "C. Law of Entropy", "D. Law of Relativity")]

correct_answers = ["C" , "D" , "D" , "D" , "D" , "D" , "D" , "C" , "D" , "B"]
guesses = []
score = 0
question_number = 0

for question in questions:
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    while True:
        response = input("Enter the answer (A / B / C / D): ").strip().upper()
        if response in ("A", "B", "C", "D"):
            break 
        else:
            print(" Invalid input. Please enter A, B, C, or D.")
            continue


    if response == correct_answers[question_number]:
            score += 1
            print(" Correct!")
    else:
            print(f" Incorrect. The answer was {correct_answers[question_number]}.")
    question_number += 1
print("")
print("")
print("")
print("")
print("")
print(f" you scored :{score*10}%")
