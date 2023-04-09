# Facebook costco group crawler


This is a small project to crawl facebook group page. <br>


## Explain
I use selenium package of python to do this work,and used browser is Firefox.So there most to have a geckodriver in file, defult position is in same folder.<br>

main.py is main program file,if you want to change crawled web, you have to change url in here. But I don't konw whether each facebook group is same archive ,user have to check before run. It's just a rough status.<br>
sub_program file is the folder where main program's function place.<br>
data file will put text file of the crawl result. 
I use "a" tag to write in there, if you wnat to re-run this program, please remember there is some data in there.<br>

## Data format

Result data will save in ./data/selenium_fb_costco.txt.<br>
You can change any path you want in main.py. And I use dictionary struct to store ,hope this will good to visualize.<br>
```
{
   "post_name" : poster name,
   "contnet" : contnet,
   "comments" : [
      {"comment_name" : leave comment user name,
       "message" : leave comment }
         .
         .
         .
   ]
}
```
Each line will be one post record.










