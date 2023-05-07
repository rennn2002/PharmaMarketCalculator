# PharmaMarketCalculator
Market size calculator based on Japanese prescription sales data(NDB open data 2021-2022)


### Description
厚生労働省の公開するレセプト情報・特定健診等情報データベースであるNDBオープンデータを持ちいて、薬の年間売上を取得するツールです。


### Requirements
No requirements needed for this project


### Usage
clone this repo and go to PharmaMarketCalculator
```
git clone https://github.com/rennn2002/PharmaMarketCalculator.git
```

```
cd PharmaMarketCalculator
```


```
python main.py {name of medicine}
```


### Example

#### Code
```
python main.py ルミガン
```

#### Reslults
```
院外処方：
ルミガン点眼液０．０３％
院内処方：
ルミガン点眼液０．０３％
入院処方：
院外処方売上: 24億8千万円
院内処方売上: 24億8千万円
入院処方売上: 0円
総売上: 49億7千万円
```


### Links
[第７回NDBオープンデータ](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000177221_00011.html)
