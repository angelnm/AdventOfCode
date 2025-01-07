class Processor:
    def __init__(this, file_path):
        this.line = this.read_line(file_path)
        this.length = len(this.line)
        
        this.working = True
        this.count = 0
        this.pos = 0

    def start(this):
        while(not this.hasEnded()):
            
            word = "do()"
            if this.checkWord(word):
                this.working = True
                this.pos += len(word)
                continue
            
            word = "don't()"
            if this.checkWord(word):
                this.working = False
                this.pos += len(word)
                continue
            
            if not this.working:
                this.pos += 1
                continue
        
            # WORKING, TRYING TO READ MUL(X,Y)
            if not this.checkWord("mul("):
                this.pos += 1
                continue 
            this.pos += 4
            
            number1 = this.readNumber()
            if not this.checkWord(","):
                this.pos += 1
                continue
            this.pos += 1
            number2 = this.readNumber()
            if not this.checkWord(")"):
                this.pos += 1
                continue
            this.pos += 1
            
            mult = number1*number2
            this.count += mult

    def readNumber(this):
        number = ""
        c_character = this.line[this.pos]
        while(not this.hasEnded() and "0"<= c_character <="9"):
            number += c_character
            this.pos +=1
            c_character = this.line[this.pos]
        return int(number)

    def checkWord(this, word):
        return this.line[this.pos:this.pos+len(word)] == word

    def hasEnded(this):
        return this.pos>=this.length

    def read_line(this, file_path):
        file = open(file_path, 'r')
    
        instruction = ""
        for line in file:
            instruction += line
        
        file.close()
        return instruction


def main():
    process = Processor('input2.txt')
    process.start()
    print(process.count)

main()