ans_list = [1, 54, 27, 8, 95]

while True:
    answer = input("enter character:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか、qで終了します")
        break

    if answer in ans_list:
        print("Correct")
    else:
        print("Incorrect")

        
    
            
