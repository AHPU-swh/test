num=10
if int(input("请输入第一次猜想的数字:"))==num:
    print(f"恭喜你第一次就猜对了，答案是{num}")
elif int(input("不对，再猜一次"))==num:
    print(f"恭喜你第二次猜对了，答案是{num}")
elif int(input("不对，再猜最后一次"))==num:
    print(f"恭喜你终于猜对了，答案是{num}")
else:
    print(f"答案其实是{num}")
