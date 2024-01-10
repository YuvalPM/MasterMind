class Score(list):

   def calculate(self,code, move):
       for i in range(len(move)):
           s = 0
           if move[i] in code:
               if move[i] == code[i]:
                   s=2
               else:
                   s=1
           self.append(s)
       self.sort(reverse=True)



