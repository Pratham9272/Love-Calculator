print("Welcome to the Love Calculator!")

name1=input("What is your name?")
name2=input("What is their name?")
lc_name1=name1.lower()
lc_name2=name2.lower()
T=str(lc_name1+lc_name2).count("t")
R=str(lc_name1+lc_name2).count("r")
U=str(lc_name1+lc_name2).count("u")
E=str(lc_name1+lc_name2).count("e")
Total1=T+R+U+E
L=str(lc_name1+lc_name2).count("l")
O=str(lc_name1+lc_name2).count("o")
V=str(lc_name1+lc_name2).count("v")
E=str(lc_name1+lc_name2).count("e")
Total2=L+O+V+E
Lov_Score=f"{Total1}{Total2}"
Love_Score=int(Lov_Score)
if Love_Score<10 or Love_Score>90:
  print(f"Your score is {Love_Score}%, you go together like coke and mentos.")
elif Love_Score>=40 and Love_Score<=50:
    print(f"Your score is {Love_Score}%, you are alright together.")
else:
  print(f"Your score is {Love_Score}%.")