class Solution:
    def interpret(self, command: str) -> str:
        re=""
        for i in range (len(command)):
            if command[i]=="G":
                re += "G"
            elif command[i]=="(":
                if command[i+1]==(")"):
                    re += "o"
                else:
                    re+="al"
            else:
                continue
        return re