print("Перенос  \n рядка")
print("Добавляєм \" лапки")
phrase = "Текст введений через змінну"
print(phrase + ", а тут ще й конкетинація")
print(phrase.lower() + ", а тут ще й нижній регістр")
print(phrase.upper() + ", а тут ще й верхній регістр")
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("чере"))
print(phrase.replace("Текст введений", "Букви введені"))