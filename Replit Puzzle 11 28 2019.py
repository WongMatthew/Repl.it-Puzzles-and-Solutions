from base64 import b32encode, b32decode

mask = b"weird"
secret = b"D4IR2AQXJVFEMAABA4EUOGYQLAHQMGYKLAHQ4AQMDAIBQBSJIVKAOEYQBUGAK==="
final = bytearray()
for i, byte in enumerate(secret):
  final.append(byte ^ mask[i % 5])

final = b32encode(final).decode()
print(final)

decoded = b32decode(final.encode())
original_message = bytearray()
for i, byte in enumerate(decoded):
  original_message.append(byte ^ mask [i % 5])
print(original_message.decode())