import requests
import  base64
import bs4



def cut_up(list_class):
    if len(list_class)>6:
        list_class.pop(4)
        return list_class
    return list_class

def to_json(all_class):
    to_json = {'courses':[]}
    for day_class in all_class:
        day =[]
        for a_class in day_class:
            dir_a_class = {   'classNum': '',
                              'className': '',
                              'teacherName': '',
                              'classlocal': '',
                          }
            if len(a_class)==0:
                day.append(dir_a_class)
            else:
                for i in range(0,1):
                    try:
                        dir_a_class['className'] = a_class[i]
                    except:
                        pass
                    try:
                        dir_a_class['teacherName'] = a_class[i+1]
                    except:
                        pass
                    try:
                        dir_a_class['classlocal'] = a_class[i+3]
                    except:
                        pass
                    try:
                        day.append(dir_a_class)
                    except:
                        pass
        to_json['courses'].append(day)
    return to_json

def get_kb(name,password):
    session = requests.session()
    url = 'http://jwxt.jsu.edu.cn/jsxsd/xk/LoginToXk'
    xh_1 = xh = str(name)
    # xh_1 = xh = input("请输入学号：")
    # mm =input("请输入密码：")
    mm = str(password)
    xh = base64.b64encode(xh.encode('utf-8'))
    mm = base64.b64encode(mm.encode('utf-8'))
    data = {
        'encoded': xh.decode('utf-8') + '%%%' + mm.decode('utf-8')
    }
    a = session.post(url=url, data=data)
    url_home = 'http://jwxt.jsu.edu.cn/jsxsd/xskb/xskb_list.do'
    html = bs4.BeautifulSoup(session.get(url_home).text,"lxml")
    kbtable_all = html.find('table', attrs={"id": "kbtable"})
    kbtable_list = kbtable_all.find_all('tr')
    temp = []
    for x in range(1,6):
        for y in range(0,7):
            w = kbtable_list[x].find_all("td")[y].find_all('div',attrs={"class":"kbcontent"})[0].stripped_strings
            w = [text for text in w]
            temp.append(w)
    temp = [cut_up(i) for i in temp]
    temp3 = []
    for x in range(0,7):
        temp2 = []
        for y in range(x,35,7):
            temp2.append(temp[y])
        temp3.append(temp2)
    return to_json(temp3)

if __name__ == '__main__':
    print(get_kb('20154042056','yunteng8888.'))