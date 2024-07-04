'''
เกมต่อคำหรรษา
'''

class TorKumHansar:
    def __init__(self):
        self.word_list = []

    @property
    def last_word(self):
        if len(self.word_list) == 0:
            return None

        return self.word_list[-1] 
    
    def validate_word(self, word):
        if len(self.word_list) == 0:
            self.word_list.append(word)
            return True

        if word.upper() in [w.upper() for w in self.word_list]:
            return False
        
        if word[0:2].upper() != self.last_word[-2:].upper():
            return False
        
        self.word_list.append(word)
        return True
    
    def validate_command(self, command):
        signal = command[0]
        word = command[2:]

        if signal == 'P':
            if self.validate_word(word):
                print(f'Word: {word} / List = {self.word_list}')
            else:
                print(f'ERROR: {word}')

        elif signal == 'R':
            self.reset_word_pool()

        elif signal == 'X':
            print("Stop")
            quit()
    
    def reset_word_pool(self):
        self.word_list = []
        print("Game is restarting")
        
    def play(self, commands):
        for command in commands:
            self.validate_command(command)

raw_cmd = [str(cmd) for cmd in input().split(',')]
Game = TorKumHansar()
Game.play(raw_cmd)

