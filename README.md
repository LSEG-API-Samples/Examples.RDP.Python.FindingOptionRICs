# FindingOptionRICs

### Overview

The current notebook includes functions to constructs option RICs on equities and index. Section 1 defines supplementarty functions which are further called by the main RIC construction functions. In section 2, I define separate functions per supported stock exchange. Section 3, defines a universal function which takes isin, maturity, strike and option type as an input, finds all exchanges where the options on the given asset are traded, constructs RICs for them, validates and returns the constructed RICs along with the prices.

The current version covers the following exchanges:
* US OPRA - refer to RULES7, RULES2, RULES3, RULES4 in Workspace, and Guideline for strikes above 10000 in [MyRefinitiv](https://my.refinitiv.com/content/mytr/en/datanotification/DN099473.html).
* EUREX - refer to RULES2, RULES3, RULES4 in Workspace, and general option RIC structure in [MyRefinitiv](https://my.refinitiv.com/content/mytr/en/faqs/2016/09/000195632.html). 
* Osaka Exchange - refer to RULES2, RULES3, RULES4 in Workspace, and RIC structure for Osaka exchange in [MyRefinitiv](https://my.refinitiv.com/content/mytr/en/faqs/2014/10/000189842.html).
* Stock Exchange of Hong Kong - refer to RULES2, RULES3, RULES4 in Workspace, and RIC structure for HK exchange in [MyRefinitiv](https://my.refinitiv.com/content/mytr/en/faqs/2021/04/000198505.html).
* Hong Kong Future Exchange - refer to RULES2, RULES3, RULES4 in Workspace, and RIC structure for HK exchange in [MyRefinitiv](https://my.refinitiv.com/content/mytr/en/faqs/2021/04/000198505.html).
* Intercontinental Exchange (ICE) - refer to RULES2, RULES3, RULES4 in Workspace, and general option RIC structure in [MyRefinitiv](https://my.refinitiv.com/content/mytr/en/faqs/2016/09/000195632.html). 

Syntax for expired options is universal accross exchanges and can be found [here](https://my.refinitiv.com/content/mytr/en/faqs/2018/09/000178972.html).
