import random as rand

#   Assumption about soft pity:
#       Others say that the chance doubles every pull after 74
#       Others say that it is exponential scaling
#       We can assume either:
#       1 - chance scales exponentially with a defined base so that it reaches 100% at 90 pulls
#           in which case, the exponential base is 1.37678
#       2 - the chance increases by 0.6% (chance of getting a 5 star) every pull then immediately 
#           jumps to 100% at 90 pulls
#
#       For now we are using the second choice
#

#       I don't know how 4 star soft pity works

class PullSimulator:
    def __init__(self):
        self.items = [ "5star", "4star", "3star" ]
        self.sample = 0
        self._4sPty = 0
        self._5sPty = 0
        self.stat_5s = 0
        self.stat_4s = 0
        self.stat_3s = 0
        self.stat_5w = 0
        self.stat_4w = 0
        self.stat_5r = 0
        self.stat_4r = 0
        self.stat_5wr = 0
        self.stat_4wr = 0

    def _updatePty(self, curr):
        self.sample += 1
        if curr == "5star":
            self._4sPty = 0
            self._5sPty = 0
        elif curr == "4star":
            self._4sPty = 0
            self._5sPty += 1
        elif curr == "3star":
            self._4sPty +=1
            self._5sPty +=1
        else:
            return False
    
    def calc_ch_5s(self):
        if self._5sPty == 89:
            return 1.0
        return max( (self._5sPty - 74)*0.006 , 0.006)
    
    def calc_ch_4s(self):
        # input code here for 4 star soft pity
        if self._4sPty == 9:
            return 1.0
        return .051
    
    def calc_res(self):
        self.stat_5r = float(self.stat_5s)  /   float(self.sample)
        self.stat_4r = float(self.stat_4s)  /   float(self.sample)
        self.stat_5wr = float(self.stat_5w) /   float(self.stat_5s)
        self.stat_4wr = float(self.stat_4w) /   float(self.stat_4s)

    def print(self):
        print(f"Sample Size: {self.sample}")
        print(f"\t5 Stars: {self.stat_5s} - {self.stat_5r:.2%}\t\tWins: {self.stat_5w} - { self.stat_5wr:.2%}" )
        print(f"\t4 Stars: {self.stat_4s} - {self.stat_4r:.2%}\t\tWins: {self.stat_4w} - { self.stat_4wr:.2%}" )
        print(f"\t3 Stars: {self.stat_3s}")

    def test(self, sample_size):
        guarra_4s = False
        guarra_5s = False
        for i in range(sample_size):
            ch_5s = self.calc_ch_5s()
            ch_4s = self.calc_ch_4s()
            ch_3s = 1.0 - ( ch_4s + ch_5s )

            if ch_5s == 1.0:        # If 5 star hard pity, chance of 4 star and 3 star is 0
                ch_4s = 0
                ch_3s = 0
            elif ch_4s == 1.0:      # If 4 star hard pity but not 5 star hard pity, chance of 3 star is 0 ; chance for 5 star if not 5 star, guaranteed 4 star
                ch_4s = 1.0 - ch_5s
                ch_3s = 0

            result = rand.choices( self.items, weights=[ch_5s, ch_4s, ch_3s], k=1).pop()

            self._updatePty(result)

            if result == "5star":
                self.stat_5s += 1
                
                if guarra_5s:                       # Guaranteed
                    self.stat_5w += 1
                    guarra_5s = False
                elif not guarra_5s:
                    if rand.randint(1,2) == 1:      # 5050 WIN
                        self.stat_5w += 1
                        guarra_5s = False
                    elif rand.randint(1,10) == 10:  # CAPTURING RADIANCE WIN
                        self.stat_5w +=1
                        guarra_5s = False
                    else:                           # LOSE
                        guarra_5s = True

            elif result == "4star":
                self.stat_4s += 1

                if guarra_4s:                       # 5050 WIN
                    self.stat_4w += 1
                    guarra_4s = False
                else:                               # LOSE
                    guarra_4s = True

            elif result == "3star":
                self.stat_3s += 1  
        
        self.calc_res()          
            


if __name__=='__main__':
    sample = PullSimulator()
    sample.test(300000)
    sample.print()
