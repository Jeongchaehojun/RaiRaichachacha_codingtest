#2025.07.02
#b2
colors = ["black", "brown", "red", "orange", "yellow", 
          "green", "blue", "violet", "grey", "white"]

first_color = input().strip()
second_color = input().strip()
multiplier_color = input().strip()

# 색상 인덱스를 숫자값으로 변환
first_digit = colors.index(first_color)
second_digit = colors.index(second_color)
multiplier = 10 ** colors.index(multiplier_color)

#(앞 두 자릿수) × (곱)
result = (first_digit * 10 + second_digit) * multiplier
print(result)
