"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'

def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    add_name = name #用盒子去接進來的數值
    add_year = year
    add_rank = rank
    if add_name in name_data and add_year in name_data[add_name]: # 如果年份跟名字已經在原本的字典裡
        old_rank = name_data[add_name][add_year] #old_rank是name_data[add_name][add_year]的原本value
        if add_rank < old_rank: #如果新的rank比old_rank前面
            #old_rank = add_rank #將old_rank的數值用new_rank取代
            name_data[add_name][add_year] = add_rank
    elif add_name in name_data: #如果單只有名字曾出現在原本字典裡
        name_data[add_name][add_year] = add_rank #那麼就將 add_rank 設為 [add_name]inner dictionary「add year」這個key 的 value
    else: #如果add_name, add_year, add_rank都是全新的資訊
        name_data[add_name] = {add_year: add_rank} #直接加一個新的dictionary key-value pair到後面


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        lines = f.readlines() #讀文檔的每一行
        print(lines)
        year = lines[0].strip() #第一行永遠是年份，所以先讀取並定義year，並清掉不需要之物
        for line in lines[1:]: #從第二行開始的每一行
            rank_list = line.split(',') #將每一行內容用逗號分割，並丟出一個list
            # for item in rank_list: #在rank_list裡面的每個position
            rank = rank_list[0] #第一個物件一定是rank
            rank = rank.strip() #將rank前後的空白去掉
            name_boy = rank_list[1] #第二個物件一定是男生名字
            name_boy = name_boy.strip()
            name_girl = rank_list[2] #第三個物件一定是女生名字
            name_girl = name_girl.strip()
            add_data_for_name(name_data, year, rank, name_boy) #相同年份跟排名的男女名字分開傳送進add_data_for_name function
            add_data_for_name(name_data, year, rank, name_girl)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {} #創造一個新的dictionary
    for file in filenames: #在filenames list裡面的每個file
        add_file(name_data, file) #丟進add_file function
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    matching_names = [] #創造一個新的list
    searched_name = target #用一個箱子裝target
    for names in name_data: #在name_data字典裡的所有name
        find_name = names.lower() #為了讓搜尋可以case insensitive, 把names變成小寫，用一個箱子接
        if searched_name in find_name: #如果搜尋的文字有出現在 find name 裡面
            matching_names.append(names) #就把沒有變成小寫的names加上matching_list的最後面-使用append,不可使用+=,不然會變成單字母
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
