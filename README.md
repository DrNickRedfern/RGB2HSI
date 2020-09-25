# RGB2HSI
This repository contains two Python functions:

* `RGB2HSI`: convert RGB colour values to HSI
* `deltaHSI`: find the distance between two colours in HSI colour space

These functions are based on Koschan and Abidi (2008: 58-60, 63-64).

## HSI colourspace

The HSI colour model represents colour as *hue* (H), *saturation* (S), and *intensity* (I).

<img src="https://www.mdpi.com/water/water-11-02339/article_deploy/html/images/water-11-02339-g004.png" width="600">
(Cao, Zhu, Zhao, Liu, & Gao (2019) CC-BY 4.0)

The hue describes the dominant colour represented as an angle in the range [0, 360], where red is 0&#176;, yellow is 60&#176;, green is 120&#176; cyan is 180&#176;, blue is 240&#176;, and magenta is 300&#176;.

The saturation is the realtive purity of the colour and depends on the amount of white light present, and has the range [0, 100].

The intensity ranges from black (0) to White (100).

## RGB2HSI

`RGB2HSI` converts RGB colour values to HSI using the following equations:

<img src="https://render.githubusercontent.com/render/math?math=H=\delta">&nbsp;&nbsp;if&nbsp;&nbsp;<img src="https://render.githubusercontent.com/render/math?math=B\leq\G">&nbsp;&nbsp;and&nbsp;&nbsp;<img src="https://render.githubusercontent.com/render/math?math=H=360-\delta">&nbsp;&nbsp;if&nbsp;&nbsp;<img src="https://render.githubusercontent.com/render/math?math=B>G">, where

<img src="https://render.githubusercontent.com/render/math?math=\delta=arcos\Big(\frac{(R-G)%2B(R-B)}{2*SQRT((R-G)_2%2B(R-B)*(G-B))}\Big)">&nbsp;.

<img src="https://render.githubusercontent.com/render/math?math=S=1-3*\frac{min(R,G,B)}{R%2BG%2BB}">

<img src="https://render.githubusercontent.com/render/math?math=I=\frac{R%2BG%2BB}{3}">

`RGB2HSI` expects as input a tuple of RGB colour values. For example, to convert the RGB colour <img src="https://render.githubusercontent.com/render/math?math=C_{1}=(100,150,200)"> to HSI:

```Python
RGB2HSI((100, 150, 200))
```

returns the tuple (210, 33.3, 150).

### deltaHSI

For two colours <img src="https://render.githubusercontent.com/render/math?math=C_{1}=(H_{1},S_{1},I_{1})"> and <img src="https://render.githubusercontent.com/render/math?math=C_{2}=(H_{2},S_{2},I_{2})"> in HSI colour space, the disdtanbce between them is given by

<img src="https://render.githubusercontent.com/render/math?math=\Delta_{HSI}(C_{1},C_{2})=SQRT((\Delta I)^{2}%2B(\Delta C)^{2})">,

where

<img src="https://render.githubusercontent.com/render/math?math=\Delta I=|I_{1}-I_{2}"> and <img src="https://render.githubusercontent.com/render/math?math=\Delta C=SQRT(S^2_{1}%2BS^2_{2}%2B-2S_{1}S_{2}cos\theta)">, with

<img src="https://render.githubusercontent.com/render/math?math=\theta=|H_{1}-H_{2}|">&nbsp;&nbsp;if&nbsp;&nbsp;<img src="https://render.githubusercontent.com/render/math?math=|H_{1}-H_{2}|\leq\pi">&nbsp;&nbsp;and&nbsp;&nbsp;<img src="https://render.githubusercontent.com/render/math?math=\theta=2\pi-|H_{1}-H_{2}|">&nbsp;&nbsp;if&nbsp;&nbsp;<img src="https://render.githubusercontent.com/render/math?math=|H_{1}-H_{2}|>\pi">.

`deltaHSI` calculates this distance for two HSI colours entered as tuples. For example, where <img src="https://render.githubusercontent.com/render/math?math=C_{1}=(100,200,150)"> and <img src="https://render.githubusercontent.com/render/math?math=C_{2}=(139,57.1,117)"> we can determine the distance betwen them using 
```Python
deltaHSI((210, 33.3, 150), (139, 57.1, 117))
```
which returns the result 81.44611821341518.

## References
Cao, P., Zhu, Y., Zhao, W., Liu, S., & Gao, H. (2019) Chromaticity measurement based on the image method and its application in water quality detection, *Water* 11 (11): 2339. https://doi.org/10.3390/w11112339.
Koschan, A., and Abidi, M. (2008) *Digital Color Image Processing*. Hoboken, NJ: John Wiley & Sons.
