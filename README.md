# APM466_A1

To use this project, what you need to do is open the file Spider_for_A1 and you may start as follows:

  1. Run the module collector.py to get the web links.
  2. Run the module price_spider.py to get the price data based on the web links.
  3. Run the module info_spider.py to get the bond info data based on the web links.
  4. Run the module finalize.py to combine the 2 data into one as results.txt and results.csv.

Notice:

* Warm: there might have some error when you do the Step 1. The reson is I am using write("historical", "a") instead of "w". The file may not exist. But anyway, you may be able to fix it by yourself, right? ^-^

* This project uses too many for-loop. Thus for step 1, 2 and 3, it will take nearly 10 min for each module. However, you may make it more efficient if you want. I am not gonna to do it, tho. ^-^
  
  1. Try
      driver_i = webDriver.Chorme(), for i \in {1,2, ... ,32}. 
  Thus, you will collect data from 32 websites, instead of what I did, which collect the data one web by one.
    
  2. In step 1, I should have record the web links for historical data and snapshot data. But when I am writing that code, I haven't got the assignment, thus not knowing that we need the data from snapshot. 
  By doing so, you may skip step 3.
  
  3. You may use BeatifulSoup instead. BS can be run behind the screen. The problem is the HTML BS read in our assignment is kind of wried for some reason I don't know. Therefore, I simply give it up. 
