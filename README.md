# Chase Credit Card Processing

This software was built and used because doing taxes really fucking sucks, and it sucks even more
when you bank with chase. They will only give you your CC statements in pdf form (you can get the last
three months in csv format ...) and their customized search stuff sucks. This process will take your PDFs,
convert them to text, and the give you the ability to filter them using a tagging (comma separated command line)
system.

Any questions, @josephmisiti

- First, you need to download your statements at www.chase.com

Customer Center -> See Account Statements -> Credit Card

- Download each statement you want to process by month in the following format

2012-01.pdf
2012-02.pdf
2012-03.pdf
...

put them in the same directory as these files in a directory called "pdfs"

- Install pdftotext

brew install xpdf

- run process.sh

./process.sh

- Now you should have a directory full of text files as follows:

2012-01.txt
2012-02.txt
2012-03.txt
...

- Now you my clean.py script to clean transactions:

You want to see all your amazon transactions:

josephmisiti$ ./clean.py amazon

01/21 AMAZON MKTPLACE PMTS AMZN.COM/BILL WA 28.5
...

OR - how about all the times you ate in mcdonald's in the last year:

josephmisiti$ ./clean.py mcdon

### To Sort Highest to Lowest

```
./clean.py '' sort | awk -F"|" '{print $3" "$2" "$1}' | sort -k 1n
```
