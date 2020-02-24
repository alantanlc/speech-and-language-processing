We'll make use of some Unix commands: 
  tr, used to systematically change particular characters in the input;
  sort, which sorts input lines in alphabetical order;
  uniq; which collapses and counts adjacent identical lines

We can use tr to tokenize the words by changing every sequence of non-alphabetic characters to a newline ('A-Za-z' means alphabetic, the -c option complements to non-alphabet, and the -s option squeeze all sequences into a single character):

  tr -sc 'A-Za-z' '\n' < sh.txt

Now that there is one word per line, we can sort the lines, and pass them to uniq -c which will collapse and count them:

  tr -sc 'A-Za-z' '\n' < sh.txt | sort | uniq -c

Alternatively, we can collapse all the upper case to lower case:

  tr -sc 'A-Za-z' '\n' < sh.txt | tr A-Z a-z | sort | uniq -c

Now we can sort again to find the frequent words. The -n option to sort means to sort numerically rather than alphabetically, and the -r option means to sort in reverse oder (highest-to-lowest):

  tr -sc 'A-Za-z' '\n < sh.txt | tr A-Z a-z | sort | uniq -c | sort -n -r

The results show that the most frequent words in Shakespeare, as in any other corpus, are the short function words like articles, pronouns, prepositions.

Unix tools of this sort can be very handy in building quick word count statistics for any corpus.

