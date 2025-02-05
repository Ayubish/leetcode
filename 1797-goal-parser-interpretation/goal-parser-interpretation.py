class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ""
        for i in range(len(command)):
            if command[i] == "(":
                continue
            elif command[i] == ")":
                if command[i-1] == "(":
                    interpreted += "o"
                else:
                    continue
            else:
                interpreted += command[i]
        return interpreted