<h1>Veri Yapilari Insertion Sort</h1>

[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
<h3>1.soru</h3> 
Big-O gösterimini yazınız.

<h3>2.soru:</h3>
Time Complexity 

Average case:
Aradığımız sayının ortada olması

Worst case: 
Aradığımız sayının sonda olması

Best case: 
Aradığımız sayının dizinin en başında olması.

<h3>3.soru:</h3>
Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.

<h3>4.soru:</h3>
[7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.




<h5>1.soru çözümü</h5> Insertion Sort türüne göre aşamaları
1. adım [2,27,16,22,18,6]
2. adım [2,6,16,22,18,27]
3. adım [2,6,16,18,22,27]

<h5>2.soru çözümü</h5>Big-O gösterimi
O(n2)

<h5>3.soru çözümü</h5>
Dizi sıralandıktan sonra 18 sayısı Average Case kapsamındadır

<h5>4.soru çözümü</h5>

1.Adım [3,7,5,8,2,9,4,15,6]

2.Adım [3,5,7,8,2,9,4,15,6]

3.Adım [3,5,7,8,2,9,4,15,6]

4.Adım [3,5,7,2,8,9,4,15,6]


<h1>Veri Yapilari Merge Sort</h1>


<h3>1.soru:</h3> Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.

<h3>2.soru:</h3> Big-O gösterimini yazınız.
  
  
<h5>1.soru çözümü</h5>

1.adım	[16,21,11,8,12,22]
2.adım	[16,21,11]-[8,12,22]
3.adım	[16]-[21,11]-[8]-[12,22]
4.adım	[16]-[21]-[11]-[8]-[12]-[22]
5.adım	[16]-[21,11]-[8]-[12,22]
6.adım	[11,16,21]-[8,12,22]
7.adım	[8,11,12,16,21,22]

<h5>2.soru çözümü</h5>

2^x=n logn O(nlogn)


<h1>Veri Yapilari Binary-Search-Tree</h1>

[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

<h5>1.adım:</h5>

Root:7 


<h5>2.adım:</h5> 5 < 7

         7 
        /
       5
<h5>3.adım:</h5> 1 < 7

         7
        / 
       5
      /
     1
<h5>4.adım:</h5> 8 > 7

           7
          / \
         5   8
        /
      1
<h5>5.adım:</h5> 3 < 7

          7
         / \
        5   8
       /
      1
       \
         3
<h5>6.adım:</h5> 6 < 7

           7
          / \
         5   8
        / \
       1   6
       \
         3
<h5>7.adım:</h5> 0 < 7

           7
          / \
         5   8
        / \
       1   6
      / \
     0   3
<h5>8.adım:</h5> 9 > 7

            7
           / \
          5   8
         / \    \
        1   6    9
       / \
      0   3
<h5>9.adım:</h5> 4 < 7

             7
            / \
           5    8
          / \     \
         1   6     9
        / \
       0   3
            \
             4
<h5>10 .adım:</h5> 2 < 7

               7
              / \
             5   8
            / \    \
           1   6    9
          / \
         0   3
             / \
            2    4



<h1>KodluyoruzIlkRepo</h1>

Bu repo Kodluyoruz Pythob Veri Bilimi Eğitiminde oluşturduğumuz ilk repo. İçerisinde bir adet README dosyası, bir adet de index.html barındırıyor.

<h4>Installation</h4>
Öncelikle projeyi clonelayın. (Buraya sizin reponuzdan aldığınız link gelecek)

git clone https://github.com/ali-osman-de/kodluyoruzilkrepo

<h4>Usage</h4>
Projeyi cloneladıktan sonra Visual Studio Code programında açınız.

Linux için:

cd kodluyoruzilkrepo
				
code .

<h4>Contributing</h4>
Pull requestler kabul edilir. Büyük değişiklikler için, lütfen önce neyi değiştirmek istediğinizi tartışmak için bir konu açınız.

<h4>License</h4>
https://choosealicense.com/licenses/mit/




<h1>Sezgisel Matematik Blog</h1>

Bu yazımda sezgisel olarak matematikteki limit konusunu inceleyeceğiz. Limit konusu isminden de anlaşılacağı üzere bir limit belirlemek üzere konulmuş bir konu. Aslında biraz geniş düşündüğümüzde birçok şeyin limitinin olduğunu görüyoruz. Size verilen her bir veri setinin alt ve üst birer limiti vardır. Örnek olarak bir araba satış veri setinde alt ve üstü bulmak basit olsa da CERN gibi atomu inceleyen bilim labaratuvarlarının o kadar veri setinin arasından istenilen limitleri belirlemesi hem komplex hem de uzun bir süreci içeriyor.


<h1>Veri Bilimi Blog</h1>

İnsanların sahip olduğu tüm bilişsel ve entelektüel yeteneklere sahip bir makine kavramı, yapay genel zeka (AGI) veya alternatif olarak genel AI olarak bilinir. Bununla birlikte teknolojiyle daha dar ölçekli AI görevlerinin üstesinden gelmeyi başardık. Günümüzde yoğun olarak algılama, tahmin veya planlama için belirli ihtiyaçlar için kullanılan yapay zeka modellerinden bahsedebiliriz. Toplamda bunlar 7 adet olduğunu söyleyebiliriz.


<h1>Python Temel Proje</h1>


<h3>Soru-1:</h3>

Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]


<h3>Soru-2:</h3>
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

<h5>1.soru çözümü</h5>
Soru_1.py dosyası
linki: 

<h5>2.soru çözümü</h5>
Soru_2.py dosyası
linki: