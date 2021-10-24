print ("***********************This is your Marksheet***********************\n");
print ("Enter your Mathematics Marks") 
mathEmatics = float(input());
print ("Enter your English Marks") 
engLish = float(input());
print ("Enter your Urdu Marks")
urDu = float(input());

obtainedMarks = mathEmatics + engLish + urDu;
toTalmarks = 300;

print ("Your Score is" +" "+ str(obtainedMarks) +" "+ "out of" +" "+ str(toTalmarks));

perCentage = obtainedMarks / toTalmarks * 100;
print ("Your percentage is: "+" "+ str(perCentage))

if perCentage >= 90 and perCentage <= 100:
    print ("Your Garde Is A+ !");

elif perCentage >= 80 and perCentage <= 90:
    print ("Your Garde Is A1 !");

elif perCentage >= 70 and perCentage <= 80:
    print ("Your Garde Is A !");

elif perCentage >= 60 and perCentage <= 70:
    print ("Your Garde Is B !");

elif perCentage >= 50 and perCentage <= 60:
    print ("Your Garde Is C !");

elif perCentage >= 40 and perCentage <= 50:
    print ("Your Garde Is D !");

elif perCentage >= 30 and perCentage <= 40:
    print ("Your Garde Is E !");

elif perCentage >= 20 and perCentage <= 30:
    print ("Your Garde Is F !");

elif perCentage >= 10 and perCentage <= 20:
    print ("Your Garde Is F !");

else:
    print ("Your result is available!")
