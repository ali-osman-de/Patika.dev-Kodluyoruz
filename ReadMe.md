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
