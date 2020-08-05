"""
File: Milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    add_name = name  # 用盒子去接進來的數值
    add_year = year
    add_rank = rank
    if add_name and add_year in name_data:  # 如果年份跟名字已經在原本的字典裡
        old_rank = name_data[add_name][add_year]  # old_rank是name_data[add_name][add_year]的原本value
        if add_rank < old_rank:  # 如果新的rank比old_rank前面
            # old_rank = add_rank #將old_rank的數值用new_rank取代
            name_data[add_name][add_year] = add_rank
    elif add_name in name_data:  # 如果單只有名字曾出現在原本字典裡
        name_data[add_name][add_year] = add_rank  # 那麼就將 add_rank 設為 [add_name]inner dictionary「add year」這個key 的 value
    else:  # 如果add_name, add_year, add_rank都是全新的資訊
        name_data[add_name] = {add_year: add_rank}  # 直接加一個新的dictionary key-value pair到後面


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #

def test1():
    name_data = {'Kylie':{'2010':'57'}, 'Nick':{'2010':'37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')



def test3():
    name_data = {'Kylie': {'2010': '57'},'Sammy': {'1980':'451','1990': '200'}}
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
        return 123
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
