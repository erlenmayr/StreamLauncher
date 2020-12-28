# rC3 Stream Starter

Starts rC3 streams with the celluloid (former gnome-mpv) or any other favorite
video player.

## Why?

Watching streams in the browser slows down the computer, draining battery and
consuming resources that could be used for the rc3 World.

## How?

### Requirements
```
$ sudo apt install gnome-devel celluloid
```

### Installation
```
$ git clone https://github.com/erlenmayr/streamlauncher
$ cd streamlauncher
$ meson build
$ ninja -C build
$ ninja -C build install
```

### Hacking

I recommend Gnome Builder (should be installed by gnome-devel) to easily hack

## Screenshot

![Screenshot](web/screenshot2.png "Screenshot")
