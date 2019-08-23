# Dene-Yap-Python
Dene Yap Yapay Zeka Eğitimi Python Örnekleri


# Önemli Not

Burada bulunan dosyaları açabilmek için [Buraya Tıklayarak](https://www.anaconda.com/distribution/) Anacondayı indirmeniz ve kurmanız gerekmektedir. 

# İçindekiler

1. TwitterDataScrape.ipynb : 
    -  Twitter üzerinden herhangi bir API kullanmadan, python da bulunan selenium kütüphanesinin yardımıyla veri indirmenin anlatıldığı [jupyter notebook](http://www.veridefteri.com/2017/10/30/jupyter-notebook-nedir-2/) dökümanıdır. 
    
    **NOT :** chromedriver.exe bu uygulamada web tarayıcısının taşınabilir versiyonu olarak kullanılmaktadır. Silinmemesi gerekiyor.

2. Genetik Algoritma Yüz.ipynb :
    - [Genetik Algoritma](https://ahmetcevahircinar.com.tr/2017/08/08/genetik-algoritma-nedir-genetik-algoritma-nasil-calisir/) konusunun yüz çizme örneği ile anlatıldığı [jupyter notebook](http://www.veridefteri.com/2017/10/30/jupyter-notebook-nedir-2/) dökümanıdır. 

    - Öncelikle Çizilmiş bir yüzün değerleri makineye öğretilir. Ardından makine rastgele 100 farklı yüz oluşturur. Burada matematiksel olarak yüze en çok benzeyen 50 yüz seçilir. Seçilen yüzler çaprazlanarak yeni yüzler oluşur. Ardından yine en çok benzeyen 50 yüz seçilir. Ve bu süreç mükemmel yüz oluşana kadar devam eder. 

3. Genetik Algoritma Yol - Basit.ipynb :
    - [Genetik Algoritma](https://ahmetcevahircinar.com.tr/2017/08/08/genetik-algoritma-nedir-genetik-algoritma-nasil-calisir/) konusunun en iyi yolu bulma örneği ile anlatıldığı [jupyter notebook](http://www.veridefteri.com/2017/10/30/jupyter-notebook-nedir-2/) dökümanıdır. 

    - Öncelikle başlangıç ve bitiş noktaları belirlenir. Ardından başlangıçtan bitişe rastgele yollar üretilmeye başlanır. Bu kısımda bitiş noktasına en yakın olan 50 yol seçilir ve çaprazlanarak yeni yollar üretilir. Ardından yine en yakın 50 yol seçilir. Ve bu süreç bitiş noktasına ulaşılana kadar devam eder.

4. Genetik Algoritma Yol - Kompleks.ipynb :
    - [Genetik Algoritma](https://ahmetcevahircinar.com.tr/2017/08/08/genetik-algoritma-nedir-genetik-algoritma-nasil-calisir/) konusunun en iyi yolu bulma örneği ile anlatıldığı [jupyter notebook](http://www.veridefteri.com/2017/10/30/jupyter-notebook-nedir-2/) dökümanıdır. 
    - Buradaki yapının **Genetik Algoritma Yol - Basit.ipynb**'den farkı yoktur. Ancak kodlar daha düzgün ve nesne yönelimli şekilde yazılmıştır.

5. Sesli Kontrol ile Oyun Yönetimi : Bu örnekte, Siyah ekranda mavi bir kareyi sesli olarak sağa, sola, yukarı ve aşağı hareket ettirme konusu işlenmiştir. 
    - Game.py :
        - Oyunun altyapısının kurulduğu python kodudur. 
    - SesliKontrol.py :
        - Açıldığı andan itibaren mikrofondaki sesleri algılamaya başlayan ve sağ, sol, yukarı veya aşağı komutlarını duyduğu anda klavyedeki tuşlara basarak oyundaki karenin ilerlemesini sağlayan python kodudur.
