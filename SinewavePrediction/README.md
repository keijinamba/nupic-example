# Sineウェーブ予測

## 実行

Swarmingには、予めMysqlを起動。(以下MacOS)
```sh
mysql.server start
```

Nupicを実行。
```sh

# Sineウェーブデータをファイルに出力
python generate_data.py

# Modelパラメータ生成
python swarm.py

# Swarming実行
python run.py
```
