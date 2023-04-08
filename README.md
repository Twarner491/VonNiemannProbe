# Von Niemann Probe
### Devoloped by [Teddy Warner](https://teddywarner.org/About-Me/about/) and [Jack Hollingsworth](http://fabacademy.org/2021/labs/charlotte/students/jack-hollingsworth/about/).

**An AVR-based Bluetooth telegraphing shoe insole that lets you play chess in the way Hans Niemann has been accused!** This project is our contribution to the ongoing investigation into the Hans Niemann / Magnus Carlsen cheating scandal and tests the feasibility of creating and using an over-the-board chess cheating aid.

### Check out the Von Niemann Probe's documentation on [TeddyWarner.org](https://teddywarner.org/Projects/VonNiemannProbe/)!

**© Teddy Warner & Jack Hollingsworth- 2022**
> This work may be reproduced, modified, distributed, performed, and displayed for any purpose,
> but must acknowledge Teddy Warner. Copyright is retained and must be preserved. 
> The work is provided as is; no warranty is provided, and users accept all liability.

### Sponsor -
<a href="https://www.pcbway.com/"><img src="https://teddywarner.org/images/VonNiemannProbe/PCBWay.png" width="150"></a>

## Python Dependencies - 

Various Python dependencies are needed to run the VNPFinal.py script, but overall the installation is pretty lightweight. The only change that needs to be made locally is the path of your stockfish .exe, which must be downloaded from [here](https://stockfishchess.org/download/) prior to use. Any version of Stockfish should work, but we have only tested on the latest version (Version 15). 
<br/><br/>
The outgoing COM port of the Bluetooth module must be updated, this can be found in device manager in all Windows 7+ machines. 
Install commands for all Python dependencies are below, any release past Python 3.7 will work.

```python
pip install stockfish
pip install python-chess
pip install pyserial
pip install regex
```

## Sources -
- [https://www.npr.org/2022/10/21/1130442319/hans-niemann-sues-magnus-carlsen-for-100-million-accusing-him-of-defamation](https://www.npr.org/2022/10/21/1130442319/hans-niemann-sues-magnus-carlsen-for-100-million-accusing-him-of-defamation)
- [https://youtu.be/eg5G1A_mTFg](https://youtu.be/eg5G1A_mTFg)
- [https://twitter.com/hansmokeniemann](https://twitter.com/hansmokeniemann)
- [https://futurism.com/von-neumann-probe](https://futurism.com/von-neumann-probe)
- [https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny212-412-DataSheet-DS40001911B.pdf](https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny212-412-DataSheet-DS40001911B.pdf)
- [https://components101.com/sites/default/files/component_datasheet/HC06%20Bluetooth%20Module%20Datasheet.pdf](https://components101.com/sites/default/files/component_datasheet/HC06%20Bluetooth%20Module%20Datasheet.pdf)
- [https://components101.com/wireless/hc-06-bluetooth-module-pinout-datasheet](https://components101.com/wireless/hc-06-bluetooth-module-pinout-datasheet)
- [http://www.sizecharter.com/clothing-fit-and-measurement/understanding-shoe-sizing](http://www.sizecharter.com/clothing-fit-and-measurement/understanding-shoe-sizing)
- [https://www.researchgate.net/figure/The-Mean-of-Absolute-in-mm-and-Relative-in-FL-Foot-Dimensions-for-Both-Genders-a_tbl2_327021689](https://www.researchgate.net/figure/The-Mean-of-Absolute-in-mm-and-Relative-in-FL-Foot-Dimensions-for-Both-Genders-a_tbl2_327021689)
- [https://www.researchgate.net/figure/Measurements-of-the-foot-and-the-inner-shoe-dimensions-a-Foot-Length-FL-and-Foot_fig5_280976288](https://www.researchgate.net/figure/Measurements-of-the-foot-and-the-inner-shoe-dimensions-a-Foot-Length-FL-and-Foot_fig5_280976288)
- [https://www.protalus.com/blogs/news/how-to-measure-feet](https://www.protalus.com/blogs/news/how-to-measure-feet)
- [https://www.magnuscarlsen.com/en](https://www.magnuscarlsen.com/en)
- [https://twitter.com/MagnusCarlsen](https://twitter.com/MagnusCarlsen)
- [https://www.chess.com/blog/CHESScom/hans-niemann-report](https://www.chess.com/blog/CHESScom/hans-niemann-report)
- [https://www.bbc.com/news/world-63010107](https://www.bbc.com/news/world-63010107)
- [https://www.bbc.com/news/world-63043023](https://www.bbc.com/news/world-63043023)
- [https://www.youtube.com/watch?v=CJZuT-_kij0&t=593s](https://www.youtube.com/watch?v=CJZuT-_kij0&t=593s)
- [https://cse.buffalo.edu/~regan/chess/fidelity/data/Niemann/](https://cse.buffalo.edu/~regan/chess/fidelity/data/Niemann/)
- [https://twitter.com/MagnusCarlsen/status/1574482694406565888?s=20](https://twitter.com/MagnusCarlsen/status/1574482694406565888?s=20)
- [https://www.wsj.com/articles/chess-cheating-hans-niemann-report-magnus-carlsen-11664911524](https://www.wsj.com/articles/chess-cheating-hans-niemann-report-magnus-carlsen-11664911524)
- [https://storage.courtlistener.com/recap/gov.uscourts.moed.198608/gov.uscourts.moed.198608.1.0.pdf](https://storage.courtlistener.com/recap/gov.uscourts.moed.198608/gov.uscourts.moed.198608.1.0.pdf)
- [https://frontofficesports.com/top-chess-player-platform-join-forces-in-82-9m-deal/](https://frontofficesports.com/top-chess-player-platform-join-forces-in-82-9m-deal/)
- [https://www.washingtonpost.com/sports/2022/10/05/chess-com-investigation-cheating-hans-niemann-magnus-carlsen/](https://www.washingtonpost.com/sports/2022/10/05/chess-com-investigation-cheating-hans-niemann-magnus-carlsen/)

---
- [Fork this repository](https://github.com/Twarner491/VonNiemannProbe/fork)
- [Watch this repo](https://github.com/Twarner491/VonNiemannProbe/subscription)
- [Create issue](https://github.com/Twarner491/VonNiemannProbe/issues/new)
