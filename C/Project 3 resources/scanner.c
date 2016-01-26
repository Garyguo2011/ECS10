/*
 * File: scanner.c
 * ---------------
 * This file implements the scanner.h interface.
 */

#include <stdio.h>
#include <ctype.h>
#include "genlib.h"
#include "strlib.h"
#include "scanner.h"
#define TRUE 1
#define FALSE 0
/*
 * Private variables
 * -----------------
 * buffer          -- Private copy of the string passed to InitScanner
 * buflen          -- Length of the buffer, saved for efficiency
 * cpos            -- Current character position in the buffer
 * skipWhitespace  -- Flag for whitespace behaviour. If true, whitespace
 *                    tokens are ignored by GetNextToken.
 */

static string buffer;
static int buflen;
static int cpos;
static bool skipWhitespace = FALSE;

/*
 * Function: InitScanner
 * ---------------------
 * All this function has to do is to initialize the private
 * variables used in this package.
 */

void InitScanner(string line)
	{
	buffer = line;
	buflen = StringLength(buffer);
	cpos = 0;
	}

/*
 * Private function: skipWhitespaceCharacters
 * Usage: skipWhitespaceCharacters();
 * ------------------------------------------
 * This function steps the current buffer position ahead as long as the
 * current character is whitespace. It does nothing if the current
 * behaviour of the package is set to return whitespace tokens.
 */

static void skipWhitespaceCharacters(void)
	{
	if(skipWhitespace) /* Do we have to skip? */
		{
		/* Skip characters as long as whitespace is found: */
		while(cpos < buflen && isspace(IthChar(buffer, cpos)))
			++cpos;
		}
	}

/*
 * Function: GetNextToken
 * ----------------------
 * The implementation of GetNextToken follows its behavioural
 * description as given in the interface: if the next character
 * is alphanumeric (i.e., a letter or a digit), the function
 * searches to find an unbroken string of such characters and
 * returns the entire string. If the current character is not
 * a letter or a digit, a one-character string containing that
 * character is returned.
 *
 * Extension 1 change: We have to skip whitespace before *and*
 * after reading the next token. This ensures that the user does
 * not run into "No more tokens" errors when changing the behaviour.
 */

string GetNextToken(void)
	{
	char ch;
	int start;
	string result;
	
	/* Check for error condition: */
	if(cpos >= buflen)
		Error("No more tokens");
	
	/* Depending on the package mode, we have to skip
	   whitespace characters: */
	skipWhitespaceCharacters();

	/* Retrieve the next character: */
	ch = IthChar(buffer, cpos);
	
	/* Based on that character, either scan a string or return the character: */
	if(isalnum(ch)) /* Character is alphanumeric: */
		{
		/* Remember the start of the string: */
		start = cpos;
		
		/* Iterate until a non-alphanumeric character is encountered: */
		while(cpos < buflen && isalnum(IthChar(buffer, cpos)))
			++cpos;
		
		/* Return the substring from start to the current character position: */
		result = SubString(buffer, start, cpos - 1);
		}
	else /* Character is not alphanumeric: */
		{
		++cpos;
		result = CharToString(ch);
		}
	
	/* Depending on the package mode, we have to skip
	   whitespace characters again: */
	skipWhitespaceCharacters();

	return result;
	}

/*
 * Function: AtEndOfLine
 * ---------------------
 * This implementation compares the current buffer position
 * against the saved length.
 */

bool AtEndOfLine(void)
	{
	return cpos >= buflen;
	}

/*
 * Function: SkipWhitespace
 * ------------------------
 * This function toggles the globla skipWhitespace flag.
 */

void SkipWhitespace(bool flag)
	{
	skipWhitespace = flag;
	}
