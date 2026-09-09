class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()

        l =0 
        r  = len(skill) -1

        team_skill = skill[l] + skill[r]
        chem  =0 

        while l < r:

            if team_skill != skill[l] + skill[r]:
                return -1

            chem += skill[l] * skill[r]

            l +=1
            r -=1
        return chem 
        