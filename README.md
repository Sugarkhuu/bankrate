# bankrate
Python web scraping and emailing code of bank FX rates in Mongolia. 

# Guide for beginners

- Clone the code first to your PC. If you don't know what it means, then google it. It's worth it :). If you're really too lazy to learn  about git cloning, then you can just copy all the codes and create files with the same names within one folder.
- You need to install the selenium for Python and the chromedriver (add it into your PATH), first of all. Of course, you should have Python installed.
- Then in config.py file, you should fill in your email (you should input its password via terminal prompt). To be apply to use gmail automatically from Python, you should allow less secure app access via this link: https://myaccount.google.com/lesssecureapps?pli=1

# To run the code:

- Go to cmd. Press Windows button + R. Type 'cmd'. Then Ok. 
- On cmd, put the folder with above files into current directory as: cd 'your folder path here, sth like: C\myfolder\bankrate.'
- then type 'python Rates.py'. It'll collect all the FX rates from banks' web and send as an email. Alongside, it should be creating two database named 'last_data' and 'historical_data'.  

Thank you very mkad;fj.
