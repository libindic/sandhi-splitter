from sandhisplitter.util import vowelT
from sandhisplitter.util import split_word_at_locations


class PostProcessor:
    def __init__(self):
        pass
    

    def transform(self, first, second):
        # Check if first.last is ya or va
        if(first[-1] == 'യ' and second[0] in vowelT.keys()):
            first = first[:-1]
            second = vowelT[second[0]] + second[1:]
            
        
        # Check if its ma
        elif(first[-1] == 'മ' and second[0] in vowelT.keys()):
            first = first[:-1] + 'ം'
            second = vowelT[second[0]] + second[1:]
            
        elif(second[0] in vowelT):
            first = first + '്'
            second = vowelT[second[0]] + second[1:]        
            
        if(len(second) >= 3):
            x, y, z = second[:3]
            if(x == z and y == '്'):
                second = second[2:]
        
        return (first, second)
            
    
    def split(self, word, locations):
        splits = split_word_at_locations(word, locations)
        word_count = len(splits)       
        for i in range(word_count-1):
            first, second = splits[i:i+2]
            first, second = self.transform(first, second)
            splits[i] = first
            splits[i+1] = second
        return splits
