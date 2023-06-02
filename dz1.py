; Задача 2: Найдите сумму цифр трехзначного числа.

; *Пример:*

; 123 -> 6 (1 + 2 + 3)
; 100 -> 1 (1 + 0 + 0) |

n = int(input('Введите трехзначное число: '))
sum = n%10 + n//100 + n//10%10
print(f'Сумма цифр числа {n} = {sum}')

; Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

; *Пример:*

; 6 -> 1  4  1
; 24 -> 4  16  4
;     60 -> 10  40  10

s = int(input('Сколько журавликов сделали Петя, Катя и Сережа вместе? => '))
print(f"Петя сделал {s//6}, Сережа сделал {s//6}, а Катя сделала {s//3*2}.")

; Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

; *Пример:*

; 385916 -> yes
; 123456 -> no

n = int(input('Введите шестизначный номер билета: '))
s1 = n//100000 + n//10000%10 + n//1000%10
s2 = n//100%10 + n//10%10 + n%10
if s2 == s1:
    print('Ваш билет счастливый')
else:
    print('Ваш билет не счастливый')

; Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

; *Пример:*

; 3 2 4 -> yes
; 3 2 1 -> no

n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Сколько долнек вы хотите отломить? => '))

if (m*n > k) and ((k%m == 0) or (k%n == 0)):
    print('Это возможно')
else:
     print('Это невозможно')