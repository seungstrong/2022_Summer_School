e_tot=0
o_tot=0
for x in range(1,101):
    if x%2 ==0:
        e_tot += x
    else:
        o_tot += x

print('1-100 까지의 짝수의 합 :', e_tot)
print('1-100 까지의 홀수의 합 :', o_tot)
print('홀수 + 짝수 = ',e_tot+o_tot) 
