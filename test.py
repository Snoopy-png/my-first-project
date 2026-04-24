books_list=[{"num":"A001","name":"《高等数学》","author":"同济大学数学系","sum":100},
            {"num":"A002","name":"《线性代数》","author":"同济大学数学系","sum":100},
            {"num":"A003","name":"《离散数学》","author":"屈婉玲","sum":100},
            {"num":"A004","name":"《python语言程序设计基础》","author":"嵩天","sum":100},
            {"num":"A005","name":"《西游记》","author":"吴承恩","sum":100}
            ]
def main():
    print("----------------主菜单---------------")
    print("请选择以下操作：")
    print("添加图书信息\t\t选项【1】")
    print("查看所有图书\t\t选项【2】")
    print("查询图书\t\t选项【3】")
    print("修改图书数量\t\t选项【4】")
    print("删除图书\t\t选项【5】")
    print("保存图书信息到文件\t\t选项【6】")
    print("退出系统\t\t选项【7】")
def add():
    print("-----------------添加图书---------------")
    book_info={}
    num=input("请输入图书的编号:")
    name=input("请输入图书的书名：")
    author=input("请输入图书的作者：")
    try:
        count=int(input("请输入图书的数量："))
        book_info["num"]=num
        book_info["name"]=name
        book_info["author"]=author
        book_info["sum"]=count
        books_list.append(book_info)
        print("添加成功")
    except ValueError:
        print("数量必须是数字！添加失败。")
    except Exception as e:
        print(f"发生了未知错误：{e}")
def check():
    print("---------------查看所有图书--------------")
    print(f"{'编号':<10} {'书名':<20} {'作者':<15} {'库存':<10}")
    print("-" * 50) 
    for book in books_list:
        num = book['num']
        name = book['name']
        author = book['author']
        sum_val = book['sum'] 
        print(f"{num:<10} {name:<20} {author:<15} {sum_val:<10}")
def inquire():
    print("----------------查询图书信息----------------")
    goal=input("请输入你想查询的图书的名字或编号：")
    for book in books_list:
        if goal==book["name"] or goal==book["num"]:
            print(f"找到了：编号:{book['num']} 书名:{book['name']} 作者:{book['author']}  数量:{book['sum']}")
            break
    else:
        print("未找到！！")
def modify_sum():
    print("----------------修改图书的数量----------------")
    modify_name = input("输入你想修改书籍的名字：")
    found = False
    for book in books_list:
        if modify_name == book["name"]:
            try:
                new_sum = int(input("请输入你想修改的数量："))
                book["sum"] = new_sum
                print("修改成功！！")
            except ValueError:
                print("数量必须是数字，修改失败！")
            
            found = True
            break
    if not found:
        print("未找到这本书！！")
def delete():
    print("-------------删除图书---------------")
    goal = input("请输入要删除的图书名字或编号：")
    # 标记是否找到
    found = False
    for book in books_list:
        # 如果输入的内容等于书名 或者 等于编号
        if goal == book["name"] or goal == book["num"]:
            books_list.remove(book)
            print("删除成功！！")
            found = True
            break  # 找到并删除后，必须立刻停止循环，否则会报错
    
    if not found:
        print("未找到这本书，无法删除！")
import json  # 1. 导入这个内置库

def save_books_json(book_list, filename="books.json"):
    try:
        # 2. 打开文件
        # 注意：encoding='utf-8' 必须加，否则中文会变乱码
        with open(filename, 'w', encoding='utf-8') as f:
            
            # 3. 【核心代码】一行搞定保存！
            # book_list: 你要保存的数据（列表）
            # f: 文件对象
            # ensure_ascii=False: 让中文正常显示，不变成 \u4e2d\u6587 这种乱码
            # indent=4: 让文件排版漂亮点，自动缩进4格
            json.dump(book_list, f, ensure_ascii=False, indent=4)
            
        print(" 保存成功！")   
    except Exception as e:
        print(f"❌ 出错了：{e}")
while True:
    main()
    try:
        num = int(input("请输入选项编号："))
    except ValueError:
        print("请输入数字！")
        continue

    if num == 1:
        add() 
    elif num == 2:
        check()
    elif num == 3:
        inquire()
    elif num == 4:
        modify_sum()  
    elif num == 5:
        delete()      
    elif num == 6:
        save_books_json(books_list) 
    elif num == 7:
        print("退出系统")
        break
    else:
        print("无效数字，请重新选择。")
