
This software was built and used because doing taxes really fucking sucks, and it sucks even more
when your bank with chase. They only will give you your CC statements in pdf form (you can get the last
three months in csv format ...) and their customized search stuff sucks. This process will take your PDFS,
convert them to text, and the give you the ability to filter them using a tagging (comma separated command line)
system.

Any questions, @josephmisiti

1. First, you need to download your statements at www.chase.com

Customer Center -> See Account Statements -> Credit Card

2. Download each statement you want to process by month in the following format

2012-01.pdf
2012-02.pdf
2012-03.pdf
...

3. Install pdftotext

brew install xpdf

4. run process.sh

./process.sh

5. Now you should have a directory full of text files as follows:

2012-01.txt
2012-02.txt
2012-03.txt
...

6. Now you my clean.py script to clean transactions:

You want to see all your amazon transactions:

josephmisiti$ ./clean.py amazon

01/21 AMAZON MKTPLACE PMTS AMZN.COM/BILL WA 28.5
...

OR - how about all the times you ate in mcdonald's in the last year:

josephmisiti$ ./clean.py mcdon
04/18 MCDONALD'S F10623 NEW YORK NY 3.15
05/11 MCDONALD'S F11679 RAMSEY NJ 3.2
06/05 MCDONALD'S F10623 NEW YORK NY 1.09

OR - how about your time warner bills:

josephmisiti$ ./clean.py time
02/13 TWC*TIME WARNER NYC 718-358-0900 NY 89.78

OR - your time warner and sprint bills

josephmisiti$ ./clean.py time,sprint
02/02 SPRINT *WIRELESS 800-639-6111 KS 127.81
02/13 TWC*TIME WARNER NYC 718-358-0900 NY 89.78

You get the point, it may or may not save you a shitload of time..

