//
// Group names     : Tarek Chaalan, Nick Haga and Zhengyao Huang
// Assignment      : No.1
// Due date        : Thursday February 2, 2023
// Purpose         : This program reads an expression in postfix form, evaluates the expression and displays its value
//

#include <iostream>
#include <stack>
#include <cstring>
using namespace std;

int evaluate(int x, int y, char op)
{
    if (op == '+') return x + y;
    if (op == '-') return x - y;
    if (op == '*') return x * y;
    if (op == '/') return x / y;
    return 0;
}

int main()
{
    char postfix[100];
    int i, x, y;
    stack<int> s;
    char response = 'y';
    int a = 5, b = 7, c = 2, d = 4;
    
    while (response == 'y' || response == 'Y')
    {
        cout << "Enter a postfix expression with $ at the end: ";
        cin >> postfix;
        int len = strlen(postfix);
        for (i = 0; i < len - 1; i++)
        {
            if (isalpha(postfix[i]))
            {
                switch (postfix[i])
                {
                    case 'a': s.push(a); break;
                    case 'b': s.push(b); break;
                    case 'c': s.push(c); break;
                    case 'd': s.push(d); break;
                }
            }
            else
            {
                y = s.top();
                s.pop();
                x = s.top();
                s.pop();
                s.push(evaluate(x, y, postfix[i]));
            }
        }
        cout << "Value = " << s.top() << endl;
        cout << "CONTINUE(y/n)? ";
        cin >> response;
    }
    return 0;
}