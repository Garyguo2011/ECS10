#include<stdio.h>
#include "genlib.h"
#include "strlib.h"

string ReverseString(string str);

main()
{
string str;
printf("Enter the first string:\n");
str = GetLine();
printf("The string entered is %s\n",str);

printf("The length of the string is %d\n", StringLength(str));

printf("Enter the position which you need:\n");

int x = GetInteger();

printf(" The %dth character is: %c\n",x, IthChar(str,x));

printf(" Concatenating ....%s\n",Concat(str,"concat"));

printf(" Reversing string ....%s\n",ReverseString(str));

printf("Converting cases ...%s\n", ConvertToUpperCase(str));

}

string ReverseString(string str)

{

string result;

int i;

result = "";

for(i=0;i< StringLength(str);i++)
{
result = Concat(CharToString(IthChar(str,i)),result);
}

return (result);
}

