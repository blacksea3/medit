from blog.models import *

## 按照时间由近至远寻找板块
## 输入范围
## 输出内容，格式为Queryset
def select_block_bytime(range):
    newblocks = Block.objects.all().order_by('modifytime')[range[0]:range[1]]
    return newblocks

## 生成板块数量
## 输出数字
def generate_total_block_number():
    return Block.objects.all().count()
    
#页码参考表
'''
present occur   out         total==9
1       4       1234
2       4       1234
3       4       2345
1       5       12345
2       5       12345
3       5       12345
4       5       23456
7       4       6789
8       4       6789
9       4       6789
6       5       56789
7       5       56789
8       5       56789
9       5       56789
''' 

## 生成页码标记
## 输入每页数量,当前页码和最多同时存在的页数
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)

def generate_block_page(number,present,occurnumber):
    last_page_number = Block.objects.all().count()//number + 1
    if last_page_number <= occurnumber:
        return (1, [_ + 1 for _ in range(last_page_number)], last_page_number)
    else:
        #页码靠前处理
        if present <= occurnumber//2:
            return (1, [_ + 1 for _ in range(occurnumber)], 1, occurnumber, last_page_number)
        #页码靠后处理 
        elif (last_page_number - present + 1) <= occurnumber//2:
            return (1, [last_page_number - occurnumber + _ + 1 for _ in range(occurnumber)], 
                last_page_number - occurnumber + 1, last_page_number, last_page_number)
        #页码居中处理
        else:
            return (1, [last_page_number - (occurnumber - occurnumber//2) + _ + 1 for _ in range(occurnumber)], 
                last_page_number - (occurnumber - occurnumber//2) + 1,
                last_page_number + occurnumber//2,
                last_page_number)
            