from inutils import crypt

var1 =crypt.base.encode(crypt.base.encode(1*'h'+1*'e'+2*'l'+1*'o',64),85)

print(var1)

print(crypt.base.decode(crypt.base.decode(var1,85),64))