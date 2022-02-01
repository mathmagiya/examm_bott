# examm_bott
# @neotor2_bot

## Repair of copying equipment bot

Commands: 

**/start**

**/help**

**/admin**

This command shows possible actions for Mr. Admistrator (how to refresh prices)

**/addnewprice**

Use this command after loading new csv file. 

## Framework and ORM
Framework for Telegram Bot API: **aiogram**.

ORM: Admin uploads file with new prices and the content loads into sqlite3 DB by **SQLAlchemy** ORM. And then any user's query also handels by ORM commands. 


## NB for teachers: 

This bot is loaded on my VPS, that's why is works in any time. Command for Linux is 


<code>nohup python3.9 main.py &</code>

Also privided logging: any brand's button push (and it's time) is visible at
**db_button_push_log.txt** and any changes of prices **db_query_log.txt**.


