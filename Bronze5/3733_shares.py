#백준 3733번
#2025.05.09
#브론즈 5
"""
A group of N persons and the ACM Chief Judge share equally a number of S shares (not necessary all of them). Let x be the number of shares aquired by each person (x must be an integer). The problem is to compute the maximum value of x.

Write a program that reads pairs of integer numbers from an input text file. Each pair contains the values of 1 ≤ N ≤ 10000 and 1 ≤ S ≤ 109 in that order. The input data are separated freely by white spaces, are correct, and terminate with an end of file. For each pair of numbers the program computes the maximum value of x and prints that value on the standard output from the beginning of a line, as shown in the example below.

문제가 걍 존나 어려움 영어가. N명의 사람+판사임
"""
#N, S= map(int, input().split())
#print(S//(N+1))
#이 코드는 입력이 여러줄일때 불가능임
import sys #다량의 입력을 끝까지 자동으로 처리해줌
for line in sys.stdin: #입력을 줄 단위로 끝까지 차례대로 읽음! 걍 외워
    N, S = map(int, line.strip().split()) #공백 제거 후 두 개의 정수로 나눠
    print(S//(N+1)) #(참가자 수+판사 1명)