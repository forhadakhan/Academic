/*  Print “yes” for the pattern that starts and ends with vowel. Otherwise, print “no”. */

/*** Definition Section ***/

%{
%}


/*** Rules Section ***/

%%
^[aeiouAEIOU].*[aeiouAEIOU]$ {printf("\t\t yes ");}

.* {printf("\t\t no ");}
%%


/*** User code section***/

int yywrap(){}

int main(int argc, char **argv[])
{
	printf("\n Enter your inputs: \n\n");
	yylex();

	return 0;
}
