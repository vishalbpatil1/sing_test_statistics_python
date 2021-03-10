# sing_test_statistics_python
non parametric sing test in python

```
# small sample
   Sample(x)  Differnce  - sign  + sign
0         119         -1   False    True
1         120          0   False   False
2         125          5    True   False
3         122          2    True   False
4         118         -2   False    True
5         117         -3   False    True
6         126          6    True   False
7         114         -6   False    True
8         115         -5   False    True
9         123          3    True   False
10        121          1    True   False
11        120          0   False   False
12        124          4    True   False
13        127          7    True   False
14        126          6    True   False
P_value=0.291
Level_of_significance=0.050
Accept Ho at 5% level of significance
RESULT:-120 is population median of give sample x
```


```
# small two sample
 Sample1(x)  Sample2(y)  Differnce  - sign  + sign
0           70          69          1    True   False
1           69          72         -3   False    True
2           72          71          1    True   False
3           74          74          0   False   False
4           66          68         -2   False    True
5           68          67          1    True   False
6           69          72         -3   False    True
7           70          72         -2   False    True
8           71          72         -1   False    True
9           69          70         -1   False    True
10          73          75         -2   False    True
11          72          73         -1   False    True
12          68          71         -3   False    True
13          72          72          0   False   False
14          67          69         -2   False    True
p_value=0.046
Level_of_significance=0.050
reject Ho at 5% level of significance
RESULT:-Population median of both sample are different
```

```
# large sample
     Sample1(x)  Sample2(y)  Differnce  - sign  + sign
0          108         103          5    True   False
1          104         116        -12   False    True
2          103         106         -3   False    True
3          112         104          8    True   False
4           99          99          0   False   False
5          105          94         11    True   False
6          102         110         -8   False    True
7          112         128        -16   False    True
8          119         106         13    True   False
9          106         103          3    True   False
10         125         120          5    True   False
11          96          98         -2   False    True
12         107         117        -10   False    True
13         115         130        -15   False    True
14         101         100          1    True   False
15         110         101          9    True   False
16         103          96          7    True   False
17         105          99          6    True   False
18         124         120          4    True   False
19         113         116         -3   False    True
20         111         100         11    True   False
21         100         101         -1   False    True
22         122         108         14    True   False
23         124         118          6    True   False
24         104          95          9    True   False
25          97         100         -3   False    True
26         112         105          7    True   False
27         109         103          6    True   False
28         119          99         20    True   False
29         101          95          6    True   False
Calulated value of Z=1.826
Tabulated value of Z=1.960
Accept Ho at 5% level of significance
RESULT:-Population median of both sample are same
```
