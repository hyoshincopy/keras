# My first obesity model

https://www.kaggle.com/jameskhoo/deep-learning-with-keras-and-tensorflow 참조 <br>
***
Pandas Function or Attribute
===============
<strong>1. df.drop() </strong>

* Remove selected index or column. 
* how to use: ```df=df.drop(['age','name'],axis=1)```
* when use: When extract proper data that can train from csv file.
* return : DataFrame

<strong>2. df.fillna() </strong>

* Fill absent data.
* how to use: ```x_train=x_train['age'].fillna(x_train['age].mean())```
* when use: When there are absent data, you can fill any data.
* return : DataFrame

<strong>3. df.cut() </strong>

* Cut column or index
* how to use: <br>``` 
 bins=(0,50,70,90,140) ```<br>
 ```group_names = ['Light', 'Standard', 'Heavy', 'Very Heavy']``` <br>
 <strong>```categories=pd.cut(df['weight'],bins,labels=group_names)```</strong>
* when use: When there are absent data, you can fill any data.
* return : DataFrame

<strong>4. df.categories.cat.codes </strong>

* Change data into discrete data.( discrete data: 이산데이터)
* how to use: <br>
    ```bins = (0, 10, 20, 30, 40, 50)```<br>
    ```group_names = ['Baby', 'Teenager', 'Young Adult', 'Adult', 'Senior']```<br>
    ```categories = pd.cut(df['age'], bins, labels=group_names)```<br>
    <strong>```df['age'] = categories.cat.codes```</strong>
* when use: When classify is ended, it makes change all of data into discrete data. 
* additional explain: After second senetece( ```categorical=pd.cut(df['age'],bins,labels=group_names)```), <br>
your data has each 'nickname' for example, 11 is 'Baby', 25 is 'Young Adult'. <br>
But computer can only calculate <strong> DECRETE DATA</strong>. <br>
So if you use ```df.categories.cat.codes``` attribute, each nickname will mapping, <br>
'Baby'        - 0 <br>
'Teenager'    - 1 <br>
'Young Adult' - 2 <br>
'Adult'       - 3 <br>
'Senior'      - 4 <br>
* return : X (It is attribute)
