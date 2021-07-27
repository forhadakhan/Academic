/*  A lex program for the pattern that starts with vowel, 
	ends with consonant and might have digits too. */


/*** Definition Section ***/

%{
int valid_patterns = 0, invalid_patterns =0;
%}

PATTERN ([aeiouAEIOU][A-Za-z0-9]*[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])*

/*** Rule section***/ 

%%
{PATTERN} {printf("\n\t Pattern Matched: %s", yytext); valid_patterns++;}
[A-Za-z0-9]+ {invalid_patterns++;}
"\n" {
	printf("\n\n\t Total Matched Patterns  : %d", valid_patterns);
	printf("\n\t Total Unmatched Patterns: %d\n", invalid_patterns);
	valid_patterns = 0; invalid_patterns = 0;
}
%%


/*** User Code Section***/

int yywrap(){}

int main(int argc, char **argv[])
{
	printf("\n Enter your inputs: \n\n");
	yylex();

	return 0;
}
