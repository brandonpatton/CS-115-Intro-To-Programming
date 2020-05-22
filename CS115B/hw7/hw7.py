'''
Created on Oct 24, 2017
I pledge my honor that I have abided by the Stevens Honor System

Brandon Patton

@author: bpatton
'''
FullAdder = { ('0','0','0') : ('0','0'), ('0','0','1') : ('1','0'), ('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def numToBaseB(N, B):
    '''Returns the string of N in base B'''
    if N == 0:
        return ''
    return numToBaseB(N//B, B) + str(N % B)

def BaseBToNum(S, B):
    '''Returns the integer of S from base B'''
    if S == '':
        return 0
    return BaseBToNum(S[:-1], B) * B + int(S[-1])

def baseToBase(B1, B2, SinB1):
    '''Takes two bases as input as B1 and B1 and a string SinB1. Converts a string
    in B1 to a string in B2'''
    return numToBaseB(BaseBToNum(SinB1, B1), B2)

def add(S, T):
    '''Takes two binary strings S and T as input and returns their sum, also in
    Binary. Converts each string to numbers, adds them, then converts back to 
    Binary'''
    return numToBaseB(BaseBToNum(S, 2) + BaseBToNum(T, 2), 2)

def addB(S, T):
    '''Takes two strings of binary numbers and adds them using binary addition
    rather than converting to numbers and adding from there'''
    if len(S) > len(T):
        T = (len(S) - len(T))*'0' + T 
    if len(T) > len(S):
        S = (len(T) - len(S))*'0' + S
    def addB_helper(S, T, carry):
        '''Uses the Dictionary FullAdder and a carry variable to achieve binary
        addition. The dictionary has every possible outcome stored to reference when
        needed.'''
        if S == '' or T == '':
            return carry
        result = FullAdder[(S[-1], T[-1], carry)]
        return addB_helper(S[:-1], T[:-1], result[1]) + result[0]
    def leading_zeros(S):
        '''Eliminates leading zeros from the final binary string.'''
        if S == '0':
            return '0'
        if S[0] == '0':
            return leading_zeros(S[1:])
        if S[0] != '0':
            return S
    return leading_zeros(addB_helper(S, T, '0'))
    



    
        
        
        
        
        
        
        
        
        
        
        
