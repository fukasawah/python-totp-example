import sys
import qrcode
from urllib.parse import quote

if len(sys.argv) < 2:
    print("required argument")
    sys.exit(1)
  

SECRET_KEY_BASE32 = sys.argv[1]

USER = "example@dummy.local"
ISSUER = "EXAMPLE"

uri = f"otpauth://totp/{quote(ISSUER)}:{quote(USER)}?secret={SECRET_KEY_BASE32}&issuer={quote(ISSUER)}"

# pyotpを使う場合は以下のようにしてもURIが得られる
import pyotp
totp = pyotp.TOTP(SECRET_KEY_BASE32)
uri = totp.provisioning_uri(name=USER, issuer_name=ISSUER)

image = qrcode.make(uri)
image.save("qrcode.png")