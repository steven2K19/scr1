# Opera Arias Database Scraping
## Dataframe for Opera Arias
It is a Python 3 library for generating dataframe of opera arias info. 

Famous composer includes: Hendel, Mozart, Rossini, Donizetti, Wagner, Strauss, Puccini. 

webpage: https://www.opera-arias.com/arias/

![1](https://user-images.githubusercontent.com/46503526/74561809-540aa200-4f37-11ea-9330-ac15a8c6ede0.PNG)

## Usage
```
# pip install fundamental

from fundamental import fundamental

symlist = ['MSFT','GOOG','FB'] 
df = fundamental.get_df_list(symlist)        

```

## Limitation
- slow internet connection would lead scraping error and the program will auto try 3 times. 

