k = [176, 214, 205, 246, 264, 255, 227, 237, 242, 244, 265, 270, 283]
u = "administrator"
password = ""
for i in range(0, len(u)):
    password += chr(k[i] - ord(u[i]) - i * 10)

print(password)