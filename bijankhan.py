## 
## bijankhan normalizer
## 
## Copyright 2015 Mostafa Sedaghat Joo
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## 
##


#!/usr/bin/python
# -*- coding: utf-8 -*-



import os
import glob
import operator
import argparse
from collections import Counter




class Bijankhan(object):
    
    
    def __init__(self):
        self.misspelled = []
        with open('misspelled.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self.misspelled.append(line.split())
        
    
    def Normalize(self, word):
        word = word.replace('\u064A', '\u06CC') ## yeh arabic to yeh farsi
        word = word.replace('\u0626', '\u06CC') ## yeh arabic to yeh farsi
        word = word.replace('\u0649', '\u06CC') ## yeh arabic to yeh farsi
        word = word.replace('\u0643', '\u06A9') ## kaf arabic to kaf farsi
        word = word.replace('\u0623', '\u0627') ## arabic h 
        
        ## space to zwnj
        while word.find('\u200c') > -1:
            word = word.replace('\u200c', ' ')
            
        while word.find('  ') > -1:
            word = word.replace('  ', ' ')
            
        word = word.replace(' ', '\u200c')      
        
        for k,v in self.misspelled:
            word = word.replace(k, v)
            
        return word
        
    def Process(self, path):
        count = len(os.listdir(path))
        index = 0
        
        fname = '{0}\\bijankhan.txt'.format(path)        
        with open(fname, 'w', encoding='utf-8') as o:
            while index < count:
            
                fname = '{0}\\1 ({1}).LBL'.format(path, index)
                print("normalizing %s." % fname)
                with open(fname, 'r', encoding='cp1256') as f:
                
                    for line in f.readlines():
                        word_tag = line.split('       ')
                        word = self.Normalize(word_tag[0].strip())
                        tag = word_tag[-1].strip()
                        
                        o.write('%s\t%s\n' %(word, tag))
                            
                        
                index = index + 1
            

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Path to Bijankhan lbl files")
args = parser.parse_args()

if args.path:
    b = Bijankhan()
    b.Process(args.path)
else:
    parser.print_help()


    
