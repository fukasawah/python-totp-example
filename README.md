
TOTP Example.


Usage
--------------------

### 0. Install library

``` bash
pip install -r requirements.txt
```

### 1. Generate secret key

``` bash
python generate-key.py
# => B3DQULIS7BASNVU2ZLYTZGU4NU7YNVF5
```

### 2. Generate QR Code


``` bash
python qrcode-generate.py B3DQULIS7BASNVU2ZLYTZGU4NU7YNVF5
```

see: [qrcode.png](qrcode.png)


### 3. Check TOTP code


``` bash
python totp-example.py B3DQULIS7BASNVU2ZLYTZGU4NU7YNVF5
```

```
421697
692918 (sleep 30 sec...)
823269 (sleep 30 sec...)
088076 (sleep 30 sec...)
...
```