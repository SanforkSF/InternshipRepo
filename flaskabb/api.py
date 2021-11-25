from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
    "https://www.openforest.org.ua/wp-content/uploads/2020/01/4-768x459.jpg",
    "https://meha.kiev.ua/wp-content/uploads/2008/01/bobrik1.jpg",
    "http://www.mukachevo.net/Content/img/news/2391/p_2391682_1_slidertop2.jpg",
    "https://cdnimg.rg.ru/img/content/208/58/94/beaver_bober_1000_d_850.jpg",
    "https://atmhunt.ru/wp-content/uploads/2013/03/bobry-bobrovye4.jpg",
    "https://images.agromassidayu.com/img/novosti-i-obshestvo/79/kanadskij-bobr-razmeri-pitanie-sreda-obitaniya-i-opisanie-kanadskij-bobr-v-rossii.jpg",
    "https://cs8.pikabu.ru/post_img/big/2016/06/07/8/1465304947165982068.jpg",
    "http://svidok.online/wp-content/uploads/2021/09/976629.jpg",
    "https://maximum.fm/uploads/media_news/2016/12/0947f7eb49d275128a4e8e44360612c3536c9cd6.jpg?w=1200&h=675&il&q=65&output=jpg",
    "https://ecologyofrussia.ru/upload/iblock/fce/bober.jpg",
    "https://m.day.kyiv.ua/sites/default/files/main/articles/13092018/32_bober2.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJji1WeMSvHzOQKPQYXrTe_ffO4QUBZc_KFVT1dqUXWiDJEpy3WHaNQPOvsrIdJU8UQDc&usqp=CAU",
    "data:image/jpeg;base64,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"
]
@app.route('/')

def index():
    url = random.choice(images)

    return render_template('index.html', url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")