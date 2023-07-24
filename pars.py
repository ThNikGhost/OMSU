import requests
from bs4 import BeautifulSoup as bs
def get_data():
    URL_TEMPLATE = ["https://abit.omsu.ru/abitpage/skripty?new=8690", "https://abit.omsu.ru/abitpage/skripty?new=8745", "https://abit.omsu.ru/abitpage/skripty?new=8744", "https://abit.omsu.ru/abitpage/zachislenie_orig?new=8744&ratingl=1801"] # ссылка на сайт
    all_data = []
    for i in URL_TEMPLATE:
        r = requests.get(i)
        soup = bs(r.text, "lxml")
        title_dirty = soup.find_all('font', attrs={"size": "3"}) 
        TITLE = title_dirty[0].text

        data_dirty = soup.find_all('tr')
        list_ = []
        for i in data_dirty:
            if 'Орлов Никита Анатольевич' in i.text:
                list_.append(i.text)
        if len(list_) == 0:
            break
        end = list_[0].find('\n', 2)
        start = list_[0].find('\n')
        MY_NUM = list_[0][start+1:end]

        text = data_dirty[-1].text
        end = text.find('\n', 2)
        start = text.find('\n')
        END_NUM = text[start+1:end]
        all_data.append([TITLE, MY_NUM, END_NUM])

    #УДАЛИТЬ pyqt6-tools
    return all_data
