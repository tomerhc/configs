import copy
import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile

mod = "mod4"
terminal = "alacritty"

# key bindings
keys = [
    # essentials
    Key(
        [mod], "Return",
        lazy.spawn(terminal),
        desc='Launches Terminal'
    ),
    Key(
        [mod], "backslash",
        lazy.spawn("firefox"),
        desc='Launches Terminal'
    ),
    Key(
        [mod], "r",
        lazy.spawn("env LC_ALL=en_US.UTF-8 dmenu_run"),
        desc='Starts Dmenu on the bar'
    ),
    Key(
        [mod], "space",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key(
        [mod], "BackSpace",
        lazy.window.kill(),
        desc='Kill active window'
    ),
    Key(
        [mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key(
        [mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),

    # Switch focus to specific monitor (out of three)
    Key([mod], "q",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "w",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    Key([mod], "e",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 3'
        ),

    # Switch focus of monitors
    Key([mod, "control"], "Right",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod, "control"], "Left",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),

    # Window controls

    # Switch between windows
    Key(
        [mod], "Right", lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    Key([mod], "Left", lazy.layout.previous(),
        desc="Move focus to left"),
    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up"),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key(
        [mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key(
        [mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),
    Key(
        [mod], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
    ),

    # Stack controls
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
    ),

    # volume control
    Key(
        [mod], "F3",
        lazy.spawn("amixer set 'Master' 10%+"),
        desc='volume up 10%'
    ),
    Key(
        [mod], "F2",
        lazy.spawn("amixer set 'Master' 10%-"),
        desc='volume up 10%'
    ),
    Key(
        [mod], "F1",
        lazy.spawn("amixer set 'Master' toggle"),
        desc='Volume mute toggle'
    ),
]

# GROUPS

groups = [Group(i, layout='monadtall') for i in "12345"]

for group in groups:
    keys.append(
        Key([mod],
            str(group.name),
            lazy.group[group.name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, "shift"],
            str(group.name),
            lazy.window.togroup(group.name))
    )  # Send current window to another group

# DEFAULT THEME SETTINGS FOR LAYOUTS
layout_theme = {"border_width": 2,
                "margin": 12,
                "border_focus": "fabd20",
                "border_normal": "32302f"
                }

# THE LAYOUTS
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

'''
colors:
    primary:
        background: '0x32302f'
        foreground: '0xd5c4a1'

    # Normal colors
    normal:
        black:   '0x32302f'
        red:     '0xfb4934'
        green:   '0xb8bb26'
        yellow:  '0xfabd2f'
        blue:    '0x83a598'
        magenta: '0xd3869b'
        cyan:    '0x8ec07c'
        white:   '0xd5c4a1'

    # Bright colors
    bright:
        black:   '0x665c54'
        red:     '0xfb4934'
        green:   '0xb8bb26'
        yellow:  '0xfabd2f'
        blue:    '0x83a598'
        magenta: '0xd3869b'
        cyan:    '0x8ec07c'
        white:   '0xfbf1c7'
'''

colors = [["#32302f", "#1b1519"],  # 0 - panel background
          ["#40323b", "#fabd2f"],  # 1 - background for current screen tab
          ["#fabd2f", "#fdfdae"],  # 2 - font color for group names
          ["#ebdbb2", "#ebdbb2"],  # 3 - border line color for current tab
          # 4 - border line color for other tab and odd widgets
          ["#d3869b", "#d3869b"],
          ["#8ec07c", "#8ec07c"],  # 5 - color for the even widgets
          ["#fabd2f", "#fdfdae"],  # 6 - window title
          ["#c3807a", "#c3807a"],  # 7 - Light red widget font color
          ["#535337", "#535337"],  # 8 - dark beige background
          ["#3a3a3a", "#3a3a3a"],  # 9 - dark gray systray
          ["#000000", "#665c54"],  # 10 - font color for widgets
          ]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# DEFAULT WIDGET SETTINGS
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize=18,
    padding=2,
    background=colors[2],
    foreground=colors[10]
)
extension_defaults = widget_defaults.copy()


def make_widget_list():
    widget_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[2],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            fontsize=20,
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=colors[10],
            background=colors[5],
        ),
        widget.ThermalSensor(
            foreground=colors[10],
            background=colors[5],
            threshold=90,
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text=" 🖬",
            foreground=colors[10],
            background=colors[4],
            padding=0,
        ),
        widget.Memory(
            foreground=colors[10],
            background=colors[4],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            padding=5,
            measure_mem='G'
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Battery(
            foreground=colors[10],
            background=colors[5],
            padding=5,
            discharge_char="discharging: ",
            charge_char="charging: ",
            empty_char="empty: ",
            format='{char}{percent:2.0%}'
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors[10],
            background=colors[4],
            padding=0
        ),
        widget.Volume(
            foreground=colors[10],
            background=colors[4],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[10],
            background=colors[5],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            foreground=colors[10],
            background=colors[5],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Clock(
            foreground=colors[10],
            background=colors[4],
            format="%A, %B %d - %H:%M "
        ),
    ]
    return widget_list


def status_bar():
    widget_list = make_widget_list()
    return bar.Bar(widget_list, 24, opacity=1.0)


# screens = [Screen(bottom=status_bar(widget_list))]

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

# screens = [Screen(bottom=status_bar(widget_list))
#            for _ in range(connected_monitors)]
screens = [
    Screen(bottom=status_bar()),
    Screen(bottom=status_bar()),
    Screen(bottom=status_bar()),
]
# DRAG FLOATING WINDOWS
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

# FLOATING WINDOWS
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"


# STARTUP APPLICATIONS
@ hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call(["bash", home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.


wmname = "LG3D"
