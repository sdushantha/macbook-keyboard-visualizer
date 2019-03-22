<h1 align="center">MacBook Keyboard Visualizer</h1>

[![](https://user-images.githubusercontent.com/27065646/54805885-a0425900-4c78-11e9-8934-8c9b0ea719ba.png)](https://youtu.be/esSRsTjA4s0)

This project was heavily inspired by [@pirate's repo](https://github.com/pirate/mac-keyboard-brightness).

This script has only been tested on Manjaro on the MacBook Air, but I am pretty sure it will work on other Linux distros running on MacBooks. **This does not work on MacOS!**


## Dependencies
**Python dependencies**

```numpy```

```pyaudio```

**Other**

```kbdlight``` *(Available on the [AUR](https://aur.archlinux.org/packages/kbdlight/))*


## TODO
I need to make the script more *sensitive*? At the moment, it only has three levels so, sometimes the lights are at maximum for [a long time at the same brightness](https://youtu.be/esSRsTjA4s0?t=41)

## Research sources
- https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python
- https://github.com/pirate/mac-keyboard-brightness
- https://askubuntu.com/questions/26248/how-to-get-keyboard-light-keys-working-on-macbook
- https://github.com/WhyNotHugo/kbdlight
