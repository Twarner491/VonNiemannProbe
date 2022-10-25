# Von Niemann Probe
### Devoloped by [Teddy Warner](https://teddywarner.org/About-Me/about/) and [Jack Hollingsworth](http://fabacademy.org/2021/labs/charlotte/students/jack-hollingsworth/about/).

A AVR based bluetooth telegraph inlayed in a parametric shoe insole. 

## Sources -
 - [https://www.npr.org/2022/10/21/1130442319/hans-niemann-sues-magnus-carlsen-for-100-million-accusing-him-of-defamation](https://www.npr.org/2022/10/21/1130442319/hans-niemann-sues-magnus-carlsen-for-100-million-accusing-him-of-defamation)
 - [https://twitter.com/hansmokeniemann](https://twitter.com/hansmokeniemann)
 - [https://futurism.com/von-neumann-probe](https://futurism.com/von-neumann-probe)
 - [https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny212-412-DataSheet-DS40001911B.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny212-412-DataSheet-DS40001911B.pdf)
 - [https://components101.com/sites/default/files/component_datasheet/HC06%20Bluetooth%20Module%20Datasheet.pdf](https://components101.com/sites/default/files/component_datasheet/HC06%20Bluetooth%20Module%20Datasheet.pdf)
 - [https://components101.com/wireless/hc-06-bluetooth-module-pinout-datasheet](https://components101.com/wireless/hc-06-bluetooth-module-pinout-datasheet)
 - [http://www.sizecharter.com/clothing-fit-and-measurement/understanding-shoe-sizing](http://www.sizecharter.com/clothing-fit-and-measurement/understanding-shoe-sizing)
 - [https://www.researchgate.net/figure/The-Mean-of-Absolute-in-mm-and-Relative-in-FL-Foot-Dimensions-for-Both-Genders-a_tbl2_327021689](https://www.researchgate.net/figure/The-Mean-of-Absolute-in-mm-and-Relative-in-FL-Foot-Dimensions-for-Both-Genders-a_tbl2_327021689)
 - [https://www.researchgate.net/figure/Measurements-of-the-foot-and-the-inner-shoe-dimensions-a-Foot-Length-FL-and-Foot_fig5_280976288](https://www.researchgate.net/figure/Measurements-of-the-foot-and-the-inner-shoe-dimensions-a-Foot-Length-FL-and-Foot_fig5_280976288)
 - [https://www.protalus.com/blogs/news/how-to-measure-feet](https://www.protalus.com/blogs/news/how-to-measure-feet)

## Documentation -

---
- [Fork this repository](https://github.com/Twarner491/VonNiemannProbe/fork)
- [Watch this repo](https://github.com/Twarner491/VonNiemannProbe/subscription)
- [Create issue](https://github.com/Twarner491/VonNiemannProbe/issues/new)

## Python Dependencies - 

Various Python dependencies are needed to run the VNPFinal.py script, but overall the installation is pretty lightweight. The only change that needs to be made locally is the path of your stockfish .exe, which must be downlaoded from [here](https://stockfishchess.org/download/) prior to use. Any version of Stockfish should work, but we have only tested on the latest version (Version 15). 
<br/><br/>
The outgoing COM port of the Bluetooth module must be updated, this can be found in device manager in all Windows 7+ machines. 
Install commands for all Python dependencies are below, any release past Python 3.7 will work.

```python
pip install re
pip install pychess
pip install stockfish
```
