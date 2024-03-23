# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import json, os

mod = "mod4"
terminal = guess_terminal()

@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "n", minimize_all(), desc="Toggle minimization on all window"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "e", lazy.spawn('rofi -show calc'), desc="Spawn rofi calc"),
    Key([mod], "r", lazy.spawn('./.config/rofi/launchers/misc/launcher.sh'), desc="Spawn rofi drun"),
    Key([mod], "t", lazy.spawn(''), desc="Spawn rofi file explorer"),

    Key([mod], "x", lazy.spawn('betterlockscreen -l'), desc="Lock screen"),

    # Sound
    Key([mod], "m", lazy.spawn('pkill -f radio-mpv'), desc="Kill radio"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 4- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 4+ unmute")),

    # Bar
    #Key([mod], "å", lazy.hide_show_bar("top")),
    #Key([mod], æ, lazy.hide_show_bar("bottom")),
]

def init_group_names():
    return [("  WEB", {'layout': 'max'}),
            ("  NOTE", {'layout': 'max'}),
            ("  DEV", {'layout': 'max'}),
            ("  MISC", {'layout': 'max'})
            ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))       # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


BG="#00000080"
BG2="#00000080"
BGL="#151515"
WHI="#FFFFFF"
TRA="#00000000"

font = "Source Code Pro"


#Pywal Colors
colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
ColorBG=(colordict['colors']['color0'])
ColorBGL=(colordict['colors']['color1'])
ColorA=(colordict['colors']['color2'])
ColorB=(colordict['colors']['color3'])
ColorC=(colordict['colors']['color4'])
ColorD=(colordict['colors']['color5'])
ColorE=(colordict['colors']['color6'])
ColorF=(colordict['colors']['color7'])
ColorG=(colordict['colors']['color8'])
ColorH=(colordict['colors']['color9'])
ColorI=(colordict['colors']['color10'])
ColorJ=(colordict['colors']['color11'])
ColorK=(colordict['colors']['color12'])
ColorL=(colordict['colors']['color13'])
ColorM=(colordict['colors']['color14'])
ColorN=(colordict['colors']['color15'])


### LAYOUTS ###
layout_theme = {
    "border_width": 0,
    "margin": 15,
    "border_focus": "#000",
    "border_normal": "#fff",
    "font": font,
}

layouts = [
    #layout.Zoomy(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.floating.Floating(border_focus_stack=["#FFF", "#FFFFFF"], border_width=2),
]

widget_defaults = dict(
    fontsize=12,
    padding=5,
    background=TRA,
    font=font,
)
extension_defaults = widget_defaults.copy()

### WIDGETS ###
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(fmt="{}", highlight_method='line', disable_drag="True", active=WHI, inactive="#888888", background=ColorBGL, highlight_color=TRA, border=WHI, this_current_screen_border=WHI, this_screen_border=BGL, other_current_screen_border=WHI),
                widget.TextBox(fmt = "◤", foreground=ColorBGL, background=BG, padding=-7, fontsize=32),
                widget.CurrentLayout(background=BG, fmt=" [ {} ] "),
                widget.TextBox(fmt = "◤", foreground=BG, padding=-7, fontsize=32),

                #widget.Prompt(background=TRA),
                #widget.LaunchBar(background=TRA),
                widget.WindowName(background=TRA, fmt="{}"),
                widget.Systray(),
                
                widget.TextBox(fmt = "◥", foreground=BG, padding=-7, fontsize=32),
                widget.Volume(background=BG, foreground=WHI,fmt=" [ Volume - {} ] "),
                widget.Battery(background=BG, foreground=WHI, format=" [ Charge - {percent:2.0%} ] "),

                widget.TextBox(fmt = "◥", foreground=ColorBGL, background=BG, padding=-7, fontsize=32),
                widget.Clock(format=" [ %Y-%m-%d %a %H:%M ] ", foreground=WHI, background=ColorBGL),
            ],
            20,
            background="#00000000",
            border_width=[0, 0, 0, 0],
            border_color=[BG, "#CCC", BG, "#CCC"],
        ),
    ),

    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(fmt="{}", highlight_method='line', disable_drag="True", active=WHI, inactive="#888888", background=ColorBGL, highlight_color=TRA, border=WHI, this_current_screen_border=WHI, this_screen_border=BGL, other_current_screen_border=WHI),
                widget.TextBox(fmt = "◤", foreground=ColorBGL, background=BG, padding=-7, fontsize=32),
                widget.CurrentLayout(background=BG, fmt=" [ {} ] "),
                widget.TextBox(fmt = "◤", foreground=BG, padding=-7, fontsize=32),

                #widget.Prompt(background=TRA),
                #widget.LaunchBar(background=TRA),
                widget.WindowName(background=TRA, fmt="{}"),
                
                widget.TextBox(fmt = "◥", foreground=BG, padding=-7, fontsize=32),
                widget.Volume(background=BG, foreground=WHI,fmt=" [ Volume - {} ] "),
                widget.Battery(background=BG, foreground=WHI, format=" [ Charge - {percent:2.0%} ] "),

                widget.TextBox(fmt = "◥", foreground=ColorBGL, background=BG, padding=-7, fontsize=32),
                widget.Clock(format=" [ %Y-%m-%d %a %H:%M ] ", foreground=WHI, background=ColorBGL),
            ],
            20,
            background="#00000000",
            border_width=[0, 0, 0, 0],
            border_color=["#FFFFFF", "#CCC", "#CCC", "#CCC"],
        )
    )
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"