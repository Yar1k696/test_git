
                                                #1


# import re
#
# def fragment_of_letter(text):
#     pattern = r'[Rr][Bb]+'
#
#     letter = re.findall(pattern, text)
#     return letter
# text = input('ввести текст:>> ')
# res = fragment_of_letter(text)
# print(res)


                                                  # 2

# import re
#
# def card_verification(card):
#
#     pattern = r'^(?:\d{4}[-]){3}\d{4}$'
#
#
#
#     if re.match(pattern, card):
#         return 'Валідний номер картки'
#     else:
#         return 'Невірний номер'
# card = input('введить номер картки:>> ')
# res = card_verification(card)
# print(res)


                                                    # 3

# import re
#
# def email_gverification(email):
#
#     pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#
#     if re.match(pattern, email):
#         return 'Вітиємо, введенно вірно'
#     else:
#         return 'невірне введення('
#
# email = input('ввести електронну почту:>> ')
#
# res = email_gverification(email)
# print(res)


                                                 # 4

# def login_verification(login):
#
#     pattern = r'[A-Z][a-z]*\d{2,10}'
#
#     if re.match(pattern, login):
#         return 'Вітиємо, логін введенно вірно'
#     else:
#         return 'Невірний Логін'
#
# login = input('Введіть Логін:>>> ')
# result = login_verification(login)
# print(result)

