#!/usr/bin/env bash


show_help(){
    echo "usage: flash [OPTION]"
    echo ""
    echo "options:"
    echo "    kbd      flash the keyboard only"
    echo "    screen   flash the screen only"
    echo "    both     flash both screen and keyboard"

}
# Flash the keyboard only
kbd_flash(){
    while true;do
        kbdlight max
        sleep 0.2

        kbdlight off
        sleep 0.2
    done
}

# Flash the screen only
screen_flash(){
    while true;do
        xbacklight -set 100
        sleep 0.1

        xbacklight -set 0
        sleep 0.1
    done
}

# Flash both the keyboard and the screen ;)
both_flash(){
    while true;do
        xbacklight -set 100
        kbdlight max
        sleep 0.1

        xbacklight -set 0
        kbdlight off
        sleep 0.1
    done
}

case "$1" in
    "kbd")
        kbd_flash
        exit
        ;;
    "both")
        both_flash
        exit
        ;;
    "screen")
        screen_flash
        exit
        ;;
    *|-h|--help)
        show_help
        exit
        ;;
esac
