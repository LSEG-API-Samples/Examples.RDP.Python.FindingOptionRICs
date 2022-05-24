# FindingOptionRICs - Class Implementation

### Overview

The current folder is a class implementation for the article [Functions to find Option RICs traded on different exchanges](https://developers.refinitiv.com/en/article-catalog/article/functions-to-find-option-rics-traded-on-different-exchanges) available in [Refinitiv Devportal](https://developers.refinitiv.com/en).

### Structure of the files
The files are structred as the following:

* **defClass** - this folder includes a .py file named *constructFunction*, which includes the main class file for option RIC construction. The class itself is comprised of multiple functions which allow constructing the different parts of option RIC such as asset name, exchange code, strike, expiration date. After a potential ric is constructed the class calls check_RIC function under supplFunctions directory.
* **supplFunctions** - this folders includes two .py files named  *checkRIC* and *getExchanges* respectively. *getExchanges.py* calls a function to get all exchange codes where options on a given asset are traded. The *checkRIC.py* requests prices for the constructed option RIC to check the validity of the RIC.

### How to run
To get constructed option RICs along with the prices for the last 3 month, simply run the .py file named **constructRIC**.
