# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# com_list = ["가위","바위","보"]
# com_choose = random.choice(com_list)
# choose = input('가위바위보 게임 : "가위", "바위", "보" 중 하나를 고르세요.')
#
# if com_choose == "가위":
#     print(f"computer\n{scissors}")
#     if choose == "가위":
#         print(f"you\n{scissors}")
#         print("\n비겼습니다.")
#     elif choose == "바위":
#         print(f"you\n{rock}")
#         print("\n이겼습니다.")
#     elif choose == "보":
#         print(f"you\n{paper}")
#         print("\n졌습니다.")
# elif com_choose == "바위":
#     print(f"computer\n{rock}")
#     if choose == "가위":
#         print(f"you\n{scissors}")
#         print("\n졌습니다.")
#     elif choose == "바위":
#         print(f"you\n{rock}")
#         print("\n비겼습니다.")
#     elif choose == "보":
#         print(f"you\n{paper}")
#         print("\n이겼습니다.")
# elif com_choose == "보":
#     print(f"computer\n{paper}")
#     if choose == "가위":
#         print(f"you\n{scissors}")
#         print("\n이겼습니다.")
#     elif choose == "바위":
#         print(f"you\n{rock}")
#         print("\n졌습니다.")
#     elif choose == "보":
#         print(f"you\n{paper}")
#         print("\n비겼습니다.")

import random

ascii_art = {
    "가위": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
    "바위": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    "보": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
}

choices = ["가위", "바위", "보"]
win_map = {
    ("가위", "보"),
    ("바위", "가위"),
    ("보", "바위")
}

user = input('"가위", "바위", "보" 중 하나를 고르세요: ')
if user not in choices:
    print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 입력하세요.")
else:
    computer = random.choice(choices)
    print(f"\n컴퓨터의 선택:\n{ascii_art[computer]}")
    print(f"당신의 선택:\n{ascii_art[user]}")

    if user == computer:
        print("\n비겼습니다.")
    elif (user, computer) in win_map:
        print("\n이겼습니다!")
    else:
        print("\n졌습니다.")
