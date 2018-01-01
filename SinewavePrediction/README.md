# Sineウェーブ予測

## 前準備

Swarmingには、予めMysqlを起動。(以下MacOS)
```sh
mysql.server start
```

Sineウェーブデータをファイルに出力
```sh
python generate_data.py
```

## 実行

１）Swarming + Modelで予測
```sh
# Swarmingを実行してModelパラメータを生成
python swarm.py

# Model実行
python run.py
```

２）NetworkAPIで予測
```sh
python network.py
```