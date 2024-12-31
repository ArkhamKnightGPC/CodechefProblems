class Team:
    def __init__(self):
        self.nm = "" #team name
        self.pt = 0 #points
        self.gd = 0 #goal difference
        
    def comp(self, nm):
        return self.nm == nm or self.nm == ""
        
    def upt(self, nm, gs, gt): #gs = goals scored, gt = goals taken
        self.nm = nm
        self.pt += 3 if gs > gt else (1 if gs==gt else 0)
        self.gd += gs-gt

def cmp_teams(t1): #tuple used to compare two teams
    return (-t1.pt, -t1.gd)

t = int(input())

while t>0:
    
    teams = [Team() for i in range(4)]
    
    for i in range(12):
        inp = input().split()
        nm1, g1, g2, nm2 = inp[0], int(inp[1]), int(inp[3]), inp[4]
        flag1 = True
        flag2 = True
        for j in range(4):
            if teams[j].comp(nm1) and flag1:
                flag1 = False
                teams[j].upt(nm1, g1,  g2)
            elif teams[j].comp(nm2) and flag2:
                flag2 = False
                teams[j].upt(nm2, g2,  g1)
                
    teams.sort(key = cmp_teams)
    print(f"{teams[0].nm} {teams[1].nm}")
    t -= 1
