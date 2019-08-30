
# coding: utf-8

from wordcloud import WordCloud
import PIL.Image as image
import jieba
import numpy as np

class Arti_WCloud():
    #需要三个参数，初始文档，背景图，停用词文档
    def __init__(self,text,picture,stopword):
        self.text = text
        self.picture = picture
        self.stopword = stopword
    #先进行中文分词，并且去除停用词
    def text_jieba(self):
        general = jieba.cut(self.text)
        stop_words = [i.replace(u'\n','') for i in self.stopword if i.startswith(u'\n')==False]
        word_list = [i for i in general if i not in stop_words]
        word_text = " ".join(word_list)
        return word_text
    #构造词云
    def get_image(self):
        color_mask = np.array(image.open(self.picture))
        wc = WordCloud(font_path="C:\\Windows\\Fonts\\STKAITI.TTF",background_color="white",mask=color_mask,max_words=100,max_font_size=200,random_state=30).generate(self.text_jieba())
        wc.to_file("arti_cloud.jpg")
        
class Rest_WCloud():
    def __init__(self,rest,picture):
        self.rest = rest
        self.picture =picture
    def get_image(self):
        color_mask = np.array(image.open(self.picture))
        wc = WordCloud(font_path="C:\\Windows\\Fonts\\STKAITI.TTF",background_color="white",mask=color_mask,max_words=100,max_font_size=200,random_state=30).generate(self.rest)
        wc.to_file("rest_cloud.jpg")

if __name__=="__main__":
    file1 = open("cart_text.txt",encoding="utf-8") #帖子的文档
    file2 = open("stopword.txt",encoding="utf-8") #停用词文档
    picture = "heart.jpg" #背景图片
    stopword = file2.readlines()
    text = file1.read() #帖子文本（类型为字符串）
    #餐厅文本 类型为字符串
    rest = "黄焖鸡米饭 黄焖鸡米饭 黄焖鸡米饭 黄焖鸡米饭 黄焖鸡米饭 黄焖鸡米饭 黄焖鸡米饭 黄焖鸡米饭 潮汕砂锅粥 潮汕砂锅粥 潮汕砂锅粥 潮汕砂锅粥 潮汕砂锅粥 南京大排档 南京大排档 南京大排档 南京大排档 南京大排档 外婆家 外婆家 绿茶 绿茶 绿茶 海底捞火锅 海底捞火锅"
    arti_wcloud = Arti_WCloud(text,picture,stopword)
    arti_wcloud.get_image()
    rest_wcloud = Rest_WCloud(rest,picture)
    rest_wcloud.get_image()



