'''В этом ката от вас требуется, получив строку, заменить каждую букву на ее позицию в алфавите.
Если что-то в тексте не является буквой, проигнорируйте это и не возвращайте.
"a" = 1, "b" = 2 и др.'''
def alphabet_position(text):
    return ' '.join(str(ord(i)- ord('a') + 1) for i in text.lower() if i.isalpha())
