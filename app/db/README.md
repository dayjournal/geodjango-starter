# Install database

### Google Cloud SQL  

- PostgreSQLとPostGISをインストール  
- 課金が発生するので利用は自己責任でお願いします
- ローカル環境やDocker環境でのインストールでも問題ありません

<br>

インスタンス作成

![001](../../img/db/001.png)

<br>

PostgreSQL選択

![002](../../img/db/002.png)

<br>

インスタンス設定

![003](../../img/db/003.png)

<br>

作成されたインスタンス確認

![004](../../img/db/004.png)

<br>

Cloud Shellに接続

![005](../../img/db/005.png)

<br>

データベース作成

```sql
CREATE DATABASE sampledb;
```

![006](../../img/db/006.png)

<br>

コンソールでデータベース確認

![007](../../img/db/007.png)

<br>

データベース確認

```sql
\l
```

![008](../../img/db/008.png)

<br>

データベースにPostGIS適用

```sql
\c sampledb
CREATE EXTENSION postgis;
```

![009](../../img/db/009.png)

<br>

PostGISのバージョン確認

```sql
SELECT postgis_version();
```

![010](../../img/db/010.png)

<br>

[Cloud SQL Proxy](https://cloud.google.com/sql/docs/postgres/sql-proxy)でデータベースに接続

```sh
./cloud_sql_proxy -instances="instance name"=tcp:3306
```

![011](../../img/db/011.png)

<br>

データベースツールでデータベースに接続

![012](../../img/db/012.png)

<br>

データベースの確認

![013](../../img/db/013.png)

<br>
<br>

## ライセンス
MIT

Copyright (c) 2020 Yasunori Kirimoto

<br>
