class courseGrades:
  
  def __init__(self, history, math):
    self.hist = history
    self.math = math
    
  def transcript(self):
    print("History: " + str(self.hist) +"\n Math: " + str(self.math))
    
lucy = courseGrades(95, 82)
arnav = courseGrades(80, 60)
brian = courseGrades(100, 40)
eva = courseGrades(97, 89)
lucy.transcript()

print((lucy.hist + arnav.hist + brian.hist + eva.hist)/4)

class shapes:
  
  def __init__(self, sides):
    self.sides = sides
    
  def whatAmI(self):
    if self.sides == 1:
      print("I am a circle")
    elif self.sides == 3:
      print("I am a triangle")
    elif self.sides < 3:
      print("I have more than 3 sides")
      
class square(shapes):
  
  
  def whatAmIChild(self):
    square.whatAmI()
    
    if self.sides == 4:
      print("I am a square")

