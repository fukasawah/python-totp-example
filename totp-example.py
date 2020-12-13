import sys

import pyotp

# 手元で試すだけなので、引数で決める

if len(sys.argv) < 2:
    print("required argument")
    sys.exit(1)

SECRET_KEY_BASE32 = sys.argv[1]

# 実際はユーザ毎に秘密鍵を生成して、Authenticatorアプリに登録してもらう
# SECRET_KEY_BASE32 = pyotp.random_base32(length=32)

# インスタンス生成
totp = pyotp.TOTP(SECRET_KEY_BASE32)


# 定期的にコードが更新されることを確認する（30秒毎）
import time
prev_code = ""
while True:
    code = totp.now()
    if prev_code == code:
        time.sleep(1)
        continue
    print(code)
    prev_code = code
    