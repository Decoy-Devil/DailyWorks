

LargestNumber(Digits):
maxdigit = answer <- empty string

while (digits not empty):
for digit in digits:
    if(digit + maxdigit) > (maxdigit + digit)



LargestNumber(Digits):
answer ← empty string
while Digits is not empty do
maxDigit ← string 0
for digit in Digits do
if int(digit + maxDigit) ≥ int(maxDigit + digit) then
maxDigit ← digit
end if
end for
append maxDigit to answer
remove maxDigit from Digits
end while
return int(answer)