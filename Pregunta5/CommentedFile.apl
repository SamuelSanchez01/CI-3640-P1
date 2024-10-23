⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝
                                                      ⍝
⍝ We need to ask for user input, so we ask for int   ⍝
n←⎕                  ⍝ Now in n we have the input   ⍝
                                                      ⍝
⍝ Rn, we calculate flow log base 2 of \binom{2}{n}   ⍝
B←⌊2⍟n               ⍝ Now in B we have this value   ⍝
                                                      ⍝
⍝ Now this line calculate tribonacci(check the md)   ⍝
x←({⍵,+/¯3↑⍵}⍣n)1 2 ⍝ x is a vector with the nums   ⍝
                                                      ⍝
⍝ Finally we call x[log 2 of narayana of n, log2 n]  ⍝
x[(⌊2⍟(B!n)×((B-1)!n)÷n)+1] ⍝As we call x it print   ⍝
                                                      ⍝
⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝⍝