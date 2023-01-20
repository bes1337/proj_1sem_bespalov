new_file22 = open("text18-1.txt", "w+")
new_file22.close()
new_file22 = open("text18-1.txt", "w+", encoding = "UTF=8")
new_file22.write('Скажи-ка, дядя, ведь не даром\nМосква, спаленная пожаром,\nФранцузу отдана?\nВедь были ж схватки боевые,\nДа, говорят, еще какие!\nНедаром помнит вся Россия\nПро день Бородина!\n')
new_file22.close()


new_file22 = open(file="text18-1.txt", mode="r+", encoding="UTF=8")
a = new_file22.read()
len_up = len([i for i in a if i.isupper()])
new_file22.write(f"Колличество букв в верхнем регистре: {len_up}")
new_file22.close()


new_file21 = open("text18-1-1.txt" , "w+"  ,encoding = "UTF=8")
new_file21.write('Скажи-ка, дядя, ведь не даром\nПро день Бородина!\nМосква, спаленная пожаром,\nФранцузу отдана?\nВедь были ж схватки боевые,\nДа, говорят, еще какие!\nНедаром помнит вся Россия')

