∇r←A n
B←⌊2⍟n
C←⌊2⍟(B!n)×((B-1)!n)÷n
x←({⍵,+/¯3↑⍵}⍣n)1 2
r←x[C+1]∇