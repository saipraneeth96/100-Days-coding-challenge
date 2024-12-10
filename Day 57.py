"""
Day 57 coding Statement :

"Pass or Fail

Anusree is struggling to pass a certain college course.
The test has a total of N question, each question carries 3 marks for a correct answer and −1 for an incorrect answer. Anusree is a risk-averse person so he decided to attempt all the questions. It is known that Anusree got X questions correct and the rest of them incorrect. For Anusree to pass the course he must score at least P marks.
Will Anusree be able to pass the exam or not?
Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, three integers N, X, P.
Output Format
For each test case output ""PASS"" if Chef passes the exam and ""FAIL"" if Chef fails the exam.
You may print each character of the string in uppercase or lowercase (for example, the strings ""pAas"", ""pass"", ""Pass"" and ""PASS"" will all be treated as identical).


Sample Input 1
3
5 2 3
5 2 4
4 0 0
Sample Output 1
PASS
FAIL
FAIL
"""
SOLUTION:

# input number of test cases
t = int(input("Number of test cases: "))

for i in range(t):
    n = int(input("Number of quesstions: "))
    x = int(input("Questions correctly answered by Anusree:"))
    p = int(input("Passing Score: "))
    # 3 marks for correct answer, -1 for incorrect answer
    # Marks obtained by Anusree
    total_score = (x*3) + (n-x)*(-1)
    
    if total_score >= p:
        print("PASS")
    else:
        print("FAIL")
