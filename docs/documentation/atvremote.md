---
layout: template
title: atvremote
permalink: /documentation/atvremote/
link_group: documentation
---
# atvremote

To more easily test pyatv, the atvremote application can be used. It is bundled with
pyatv and supports all the functionality implemented by the library. So it is also a
good place to go to for inspiration when implementing your own application.

## Discovering devices

To find devices, use the `scan` command:

    $ atvremote scan
    ========================================
           Name: Living Room
       Model/SW: 4K tvOS 13.3.1 build 17K795
        Address: 10.0.0.10
            MAC: AA:BB:CC:DD:EE:FF
     Deep Sleep: False
    Identifiers:
     - 01234567-89AB-CDEF-0123-4567890ABCDE
     - 00:11:22:33:44:55
    Services:
     - Protocol: MRP, Port: 49152, Credentials: None
     - Protocol: AirPlay, Port: 7000, Credentials: None

           Name: Kitchen
       Model/SW: 3 ATV SW
        Address: 10.0.0.11
	    MAC: AA:AA:AA:AA:AA:AA
    Identifiers:
     - ABCDEFABCDEFABCD
     - AA:BB:CC:DD:EE:FF
    Services:
     - Protocol: AirPlay, Port: 7000, Credentials: None
     - Protocol: DMAP, Port: 3689, Credentials: 00000000-1111-2222-3333-444455556666

In this case two devices were found, one named `Living Room` and another named
`Kitchen`. You can read more about what everything means under [Concepts](concepts.md).

### Discovering specific devices

A normal `scan` uses multicast to discover all devices on the network. It is possible to
scan for specific devices ("unicast") by specifying `--scan-hosts`:

    $ atvremote --scan-hosts 10.0.0.10 scan
    ========================================
           Name: Living Room
       Model/SW: 4K tvOS 13.3.1 build 17K795
        Address: 10.0.0.10
            MAC: AA:BB:CC:DD:EE:FF
     Deep Sleep: False
    Identifiers:
     - 01234567-89AB-CDEF-0123-4567890ABCDE
     - 00:11:22:33:44:55
    Services:
     - Protocol: MRP, Port: 49152, Credentials: None
     - Protocol: AirPlay, Port: 7000, Credentials: None


This yields the same result, but is much faster as it only has to wait for response from
one device. Downside is of course that it cannot automatically find devices, you must know the
IP-address. Multiple devices can be specified as a comma-separated list:

    $ atvremote --scan-hosts 10.0.0.10,10.0.0.11 scan

If you have problems using regular scanning or have configured a static address on your Apple TV,
this is the recommended way of finding your devices. Please do note that you should not manually
specify address, port, etc. when using this method. It is not necessary.

The `--scan-hosts` flag can be used with any other command as well:

    $ atvremote --scan-hosts 10.0.0.10 -n Kitchen <some command>

### Specifying a device

In order for `atvremote` to know which device you want to control, you must specify the
`--id` flag (or `-i` for short) together with an identifier. You may choose any of the available
identifiers.

Based on the output in the previous chapter, you may write:

    $ atvremote -i 00:11:22:33:44:54 <some command>

But this would also work equally good:

    $ atvremote -i 01234567-89AB-CDEF-0123-4567890ABCDE <some command>

It is also possible to use the device name by specifying `-n` instead:

    $ atvremote -n "Living Room" <some command>

### Manually specifying a device

It is possible to bypass the automatic scanning that `atvremote` performs
by passing the `--manual` flag. This is convenient if you rely on an external
scanning process or to shorten the turn-around time during development testing.
However, doing so means that you mainly lose all benefits of unique identifiers.
They lose meaning completely. Only use this mode if you know what you are doing
and refrain from using this in conjunction with `--scan-hosts`!

When specifying `--manual` you *must* also specify `--address`, `--port`, `--protocol`
and `--id`. Even though the identifier is not used (or applicable), you must
still specify something. A simple call example looks like this:

    $ atvremote --manual --address 10.0.0.10 --port 49152 --protocol mrp --id test playing

## Pairing with a device

In most cases you have to pair with a device and obtain *credentials* in order to communicate
with it. To pair you must specify a device, which protocol to pair and use the `pair` command:

    $ atvremote --id 00:11:22:33:44:55 --protocol mrp pair
    Enter PIN on screen: 1234
    Pairing seems to have succeeded, yey!
    You may now use these credentials: xxxx

Which protocols a device supports can be seen with `scan`. But in general you need to pair
either `mrp` (devices running tvOS) or `dmap` (Apple TV 3 and earlier). If you also want to
stream video, you can pair `airplay` as well. The procedure is the same for all of them, just
change the argument provided to `--protocol`.

### Credentials

Once you have paired and received credentials, you must provide said credentials to `atvremote`
via the `--xxx-credentials` flags. Replace `xxx` with either `mrp`, `dmap` or `airplay`.  You
may specify multiple credentials:

    $ atvremote -n Kitchen --mrp-credentials abcd --airplay-credentials 1234 playing

In the future, `atvremote` will likely store these automatically for you. But as of right now, you
have to manage the credentials yourself. Follow progress at
[#242](https://github.com/postlund/pyatv/issues/243).

## Push updates

With `atvremote` you can use `push_updates` to display current play status automatically
without having to ask the device for it:

    $ atvremote -n Kitchen push_updates
    Press ENTER to stop
      Media type: Unknown
    Device state: Paused
    --------------------

Updates will be displayed when they happen. Just press ENTER to stop.

## Power management

Power management commands are supported by MRP devices only. 

List of supported devices:
 - Apple TV Gen 4
 - Apple TV 4K

You can turn your Apple TV on:

    $ atvremote -i 00:11:22:33:44:54 turn_on

Or turn it off:

    $ atvremote -i 00:11:22:33:44:54 turn_off

Or check the current power state:

    $ atvremote -i 00:11:22:33:44:54 power_state

## Working with commands

Several commands are supported by the library. Easiest is just to use the command
called `commands`, as it will present a list of available commands:

    $ atvremote --id 00:11:22:33:44:54 commands
    Remote control commands:
     - down - Press key down
     - home - Press key home
     - home_hold - Hold key home
     - left - Press key left
     - menu - Press key menu
     - next - Press key next
     - pause - Press key play
     - play - Press key play
     - play_pause - Toggle between play and pause
     - previous - Press key previous
     - right - Press key right
     - select - Press key select
     - set_position - Seek in the current playing media
     - set_repeat - Change repeat state
     - set_shuffle - Change shuffle mode to on or off
     - skip_backward - Skip backwards a time interval
     - skip_forward - Skip forward a time interval
     - stop - Press key stop
     - suspend - Suspend the device
     - top_menu - Go to main menu (long press menu)
     - up - Press key up
     - volume_down - Press key volume down
     - volume_up - Press key volume up
     - wakeup - Wake up the device

    Metadata commands:
     - app - Return information about current app playing something
     - artwork - Return artwork for what is currently playing (or None)
     - artwork_id - Return a unique identifier for current artwork
     - device_id - Return a unique identifier for current device
     - playing - Return what is currently playing

    Power commands:
     - power_state - Return device power state
     - turn_off - Turn device off
     - turn_on - Turn device on

    Playing commands:
     - album - Album of the currently playing song
     - artist - Artist of the currently playing song
     - device_state - Device state, e.g. playing or paused
     - genre - Genre of the currently playing song
     - hash - Create a unique hash for what is currently playing
     - media_type - Type of media is currently playing, e.g. video, music
     - position - Position in the playing media (seconds)
     - repeat - Repeat mode
     - shuffle - If shuffle is enabled or not
     - title - Title of the current media, e.g. movie or song name
     - total_time - Total play time in seconds

    AirPlay commands:
     - play_url - Play media from an URL on the device

    Device Info commands:
     - build_number - Operating system build number, e.g
     - mac - Device MAC address
     - model - Hardware model name, e.g
     - operating_system - Operating system running on device
     - version - Operating system version

    Device commands:
     - artwork_save - Download artwork and save it to artwork.png
     - cli - Enter commands in a simple CLI
     - delay - Sleep for a certain amount if milliseconds
     - device_info - Print various information about the device
     - features - Print a list of all features and options
     - push_updates - Listen for push updates

    Global commands:
     - commands - Print a list with available commands
     - help - Print help text for a command
     - pair - Pair pyatv as a remote control with an Apple TV
     - scan - Scan for Apple TVs on the network

You can for instance get what is currently playing with `playing`:

    $ atvremote --id 00:11:22:33:44:54 playing
      Media type: Music
    Device state: Playing
        Position: 0/397s (0.0%)
          Repeat: Off
         Shuffle: False

Or seek in the currently playing media:

    $ atvremote --id 00:11:22:33:44:54 set_position=123

Check operating system version:

    $ atvremote --id 00:11:22:33:44:54 version
    13.3.1

Or all device information (same as seen with `atvremote scan`):

    $ atvremote --id 00:11:22:33:44:54 device_info
    Model/SW: 4K tvOS 13.3.1 build 17K795
         MAC: 00:11:22:33:44:55

Perhaps see supported features:

    $ atvremote -n Vardagsrum -s 10.0.10.81 features
    Feature list:
    -------------
    Up: Available
    Down: Available
    Left: Available
    Right: Available
    Play: Available
    PlayPause: Available
    Pause: Available
    Stop: Available
    Next: Available
    Previous: Available
    Select: Available
    Menu: Available
    VolumeUp: Unknown
    VolumeDown: Unknown
    Home: Available
    HomeHold: Available
    TopMenu: Available
    SkipForward: Unavailable
    SkipBackward: Unavailable
    SetPosition: Available
    SetShuffle: Available
    SetRepeat: Available
    Title: Available
    Artist: Available
    Album: Available
    Genre: Available
    TotalTime: Available
    Position: Available
    Shuffle: Available
    Repeat: Available
    Artwork: Available
    App: Available
    PlayUrl: Available
    PowerState: Available
    TurnOn: Available
    TurnOff: Available

    Legend:
    -------
    Available: Supported by device and usable now
    Unavailable: Supported by device but not usable now
    Unknown: Supported by the device but availability not known
    Unsupported: Not supported by this device (or by pyatv)

Show active app:

    $ atvremote --id 00:11:22:33:44:54 app
    App: Musik (com.apple.TVMusic)

Play a video via AirPlay:

    $ atvremote --id 00:11:22:33:44:54 play_url=http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4

Artwork with a specific size (width,height):

    $ atvremote --id 00:11:22:33:44:54 artwork_save=300,-1

Using -1 will let the device decide that parameter in order to keep aspect ratio.

Multiple commands can be specified to simplify scripting. There's also a
`delay` that sleeps a certain amount of milliseconds before next command is
executed. Here's an example where `select` is pressed, followed by `left` after
waiting a second:

    $ atvremote --id 00:11:22:33:44:54 select delay=1000 left

If you want additional help for a specific command, use help:

    $ atvremote help pair
    COMMAND:
    >> pair(self)

    HELP:
    Pair pyatv as a remote control with an Apple TV.

### Logging and debugging

You can enable additional debugging information by specifying
either `--verbose` or `--debug.`. By default `pyatv` will limit some log points in length,
mainly due to an excessive amount of data might be logged otherwise. This mainly applies to
binary data (raw protocol data) and protobuf messages. These limits can be overridden by
setting the following environment variables:

    $ export PYATV_BINARY_MAX_LINE=1000
    $ export PYATV_PROTOBUF_MAX_LINE=1000
    $ atvremote --debug ... playing

In general, you shouldn't have to change these, but under some cicrumstances the complete
logs might be deseriable.
