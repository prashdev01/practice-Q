import csv
import re 
from collections import Counter


class File_operations:
    
    def __init__(self,filename) -> None:
        self.filename =  filename
    
    def word_count_from_from(self, filename,delimiters):
        self.filename = filename 
        self.delimiters = delimiters
        ''' Count the number of words in text file 
        Args:
            give a text filename that you want to check
        Return:
            The number of word in text file: 
        '''
        with open(filename,'r') as file:
            text = file.read()
            
        words = text.split()
        for delimiter in delimiters:
            words = [word for word in words if delimiter not in word]
            
            return len(words)
        
    def word_count_from_from(self, filename,delimiters):
        self.filename = filename
        self.delimiters = delimiters
    
        ''' Count the number of words in text file 
        Args:
            give a text filename that you want to check
        Return:
            The number of word in text file: 
            And the  longest word in the file
        '''
        with open(filename,'r') as file:
            text = file.read()
            
        words = text.split()
        for delimiter in delimiters:
            words = [word for word in words if delimiter not in word]
            
        max_length = 0
        largest_word = ''
        for word in words:
            length = len(word)
            if length> max_length:
                max_length = length
                largest_word = word 
            
        return len(words)  , 'and largest word is ' , largest_word 
    
    
    def most_freq_words(self, filename):
        self.filename = filename
        '''
        Finds the most frequent word in text file 
        
        Args :  
            Takes the filename as input 
        
        Returns:
            returns the most frequent word present in the text file 
        
        '''
        
        with open(filename, 'r') as file_data :
            words= []
            for line in file_data:
                words += line.split()
                
        word_count = Counter(words)
        most_freqent_words = word_count.most_common(1)[0][0]
        
        return most_freqent_words
    
    def count_rows_in_csv(self, filename):
        with open(self.filename , 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows =list(reader)
            
        return len(rows)


 