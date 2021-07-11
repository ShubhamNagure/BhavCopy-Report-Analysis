[![Linkedin: Shubham Nagure](https://img.shields.io/badge/-Shubham-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/shubham-nagure/)](https://www.linkedin.com/in/shubham-nagure/)
![Twitter Follow](https://img.shields.io/twitter/follow/shubham_nagure?style=social)
![](https://visitor-badge.glitch.me/badge?page_id=ShubhamNagure.ShubhamNagure)
# BSE BHAVCOPY DAILY REPORT

A report in which csv extracted and parserd to JSON and loaded on REDIS(as primary DB and to Cache) and rendered by VUE.JS using DJANGO backend.

<p align="center">
<img src="https://github.com/ShubhamNagure/BhavCopy-Report-Analysis/blob/main/screenshot/Demo.PNG"   />
</p>

## REQUIREMENT :

Simple Python task:
(Django + Vue + CSV export on UI).

BSE publishes a "Bhavcopy" (Equity) ZIP every day here: https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

A standalone Python Django web app/server that will do following tasks:

- [x] Downloads the equity bhavcopy zip from the above page every day at 18:00 IST for the current date.
- [x] Extracts and parses the CSV file in it.
- [x] Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
- [x] Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a table of results and optionally downloads the results as CSV. Make this page look nice!
- [x] The search needs to be performed on the backend using Redis.


## IMPLEMENTATION :

### Standalone  scripts

```-getData.py ```      -a script which extract the data from BSE site.

```-insertoRedis.py```  -a script which insert data to REDIS.

```-scheduler.py```     -scheduled above script 2 standalone scripts.


### DJANGO APP

Django backed the application to retrive data from REDIS and convert to JSON Object and handover to frontend JS.

### VUE.JS

VUE.JS render the table and serves to the template.


### REDIS

Hash data structure is used and inserted list of dictionary, keys are "SC_NAME" and values are dictionary of respective row.


ADDITIONALY:

Django-Cache is used to cache the search keys on redis in order to improve the performance and user experience.


## live [demo](http://139.59.11.162/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
