from bevyframe.Widgets.Style import *
from hereus_ui_3_2.palette import palette

imports = [
    "https://fonts.googleapis.com/css2?family=Noto+Emoji:wght@700&display=swap",
    "https://fonts.googleapis.com/css2?family=Inter&display=swap",
    "https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,300,0,0",
    "https://fonts.googleapis.com/css2?family=Croissant+One&family=Parisienne&display=swap",
    "https://fonts.googleapis.com/css2?family=Catamaran:wght@100..900&family=Moirai+One&display=swap",
    "https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap",
    "https://www.nerdfonts.com/assets/css/webfont.css"
]
webkit = {
    "scrollbar": {
        "width": "0px"
    }
}


class Label:
    class Hover:
        border = NoStyle


class Badge:
    class Caution:
        font_weight = 500
        font_size = Size.pixel(15)
        background_color = Color.red
        z_index = 9999
        position = Position.relative()
        padding = Padding(
            left=Size.pixel(4),
            right=Size.pixel(4)
        )
        margin = Margin(
            left=Size.pixel(-30),
            top=Size.pixel(-50)
        )
        border_radius = Size.pixel(10)


class Textbox:
    border_radius = Size.pixel(5)
    border = FourSided(bottom=Border(Size.pixel(1), BorderLine.solid, "#808080A0"))
    font_family = ["Catamaran", "sans-serif"]
    background_color = palette["Blank"]["Light"]["SubWidgetColor"]
    color = Color.black
    width = Size.pixel(380)
    max_width = Size.pixel(380)
    height = Size.pixel(50)
    font_size = Size.pixel(20)
    padding = Padding(
        left=Size.pixel(10),
        right=Size.pixel(10)
    )

    class LightTheme:
        color = Color.black

        class Blank:
            background_color = palette["Blank"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Blank"]["Light"]["WidgetColor"]

        class Red:
            background_color = palette["Red"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Red"]["Light"]["WidgetColor"]

        class Orange:
            background_color = palette["Orange"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Orange"]["Light"]["WidgetColor"]

        class Yellow:
            background_color = palette["Yellow"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Yellow"]["Light"]["WidgetColor"]

        class Green:
            background_color = palette["Green"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Green"]["Light"]["WidgetColor"]

        class Blue:
            background_color = palette["Blue"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Blue"]["Light"]["WidgetColor"]

        class Pink:
            background_color = palette["Pink"]["Light"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Pink"]["Light"]["WidgetColor"]

    class DarkTheme:
        color = Color.white

        class Blank:
            background_color = palette["Blank"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Blank"]["Dark"]["WidgetColor"]

        class Red:
            background_color = palette["Red"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Red"]["Dark"]["WidgetColor"]

        class Orange:
            background_color = palette["Orange"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Orange"]["Dark"]["WidgetColor"]

        class Yellow:
            background_color = palette["Yellow"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Yellow"]["Dark"]["WidgetColor"]

        class Green:
            background_color = palette["Green"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Green"]["Dark"]["WidgetColor"]

        class Blue:
            background_color = palette["Blue"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Blue"]["Dark"]["WidgetColor"]

        class Pink:
            background_color = palette["Pink"]["Dark"]["SubWidgetColor"]

            class Grey:
                background_color = palette["Pink"]["Dark"]["WidgetColor"]

    class Focus:
        outline = NoStyle


class Button:
    border_radius = Size.pixel(15)
    border = NoStyle
    color = Color.white
    width = Size.pixel(400)
    height = Size.pixel(50)
    font_size = Size.pixel(20)
    cursor = Cursor.pointer
    font_family = ["Catamaran", "sans-serif"]

    class Small:
        border_radius = Size.pixel(15)
        width = Size.pixel(150)
        height = Size.pixel(50)
        font_size = Size.pixel(15)

    class Mini:
        border_radius = Size.pixel(15)
        width = Size.pixel(100)
        height = Size.pixel(30)
        font_size = Size.pixel(15)

    class Hover:
        outline = NoStyle
        css = {"box-shadow": "inset 0 0 100px 100px #FFFFFF60"}

    class LightTheme:
        class Blank:
            background_color = palette["Blank"]["AccentColor"]

        class Red:
            background_color = palette["Red"]["AccentColor"]

        class Orange:
            background_color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_color = palette["Yellow"]["AccentColor"]

        class Green:
            background_color = palette["Green"]["AccentColor"]

        class Blue:
            background_color = palette["Blank"]["AccentColor"]

        class Pink:
            background_color = palette["Pink"]["AccentColor"]

    DarkTheme = LightTheme


class Link:
    color = inherit
    text_decoration = inherit


class TextArea:
    margin = Size.pixel(3)
    font_family = ["Catamaran", "sans-serif"]

    class Focus:
        outline = NoStyle


class Page:
    font_family = ["Catamaran", "sans-serif"]
    overflow = Overflow(x=Visibility.hidden)
    scroll_behavior = Scroll.smooth
    padding = Padding(
        top=Size.pixel(0)
    )

    class LightTheme:
        color = Color.black

        class Blank:
            background_color = palette["Blank"]["Light"]["Background"]
            accent_color = palette["Blank"]["AccentColor"]

        class Red:
            background_color = palette["Red"]["Light"]["Background"]
            accent_color = palette["Red"]["AccentColor"]

        class Orange:
            background_color = palette["Orange"]["Light"]["Background"]
            accent_color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_color = palette["Yellow"]["Light"]["Background"]
            accent_color = palette["Yellow"]["AccentColor"]

        class Green:
            background_color = palette["Green"]["Light"]["Background"]
            accent_color = palette["Green"]["AccentColor"]

        class Blue:
            background_color = palette["Blue"]["Light"]["Background"]
            accent_color = palette["Blank"]["AccentColor"]

        class Pink:
            background_color = palette["Pink"]["Light"]["Background"]
            accent_color = palette["Pink"]["AccentColor"]

    class DarkTheme:
        color = Color.white

        class Blank:
            background_color = palette["Blank"]["Dark"]["Background"]
            accent_color = palette["Blank"]["AccentColor"]

        class Red:
            background_color = palette["Red"]["Dark"]["Background"]
            accent_color = palette["Red"]["AccentColor"]

        class Orange:
            background_color = palette["Orange"]["Dark"]["Background"]
            accent_color = palette["Orange"]["AccentColor"]

        class Yellow:
            background_color = palette["Yellow"]["Dark"]["Background"]
            accent_color = palette["Yellow"]["AccentColor"]

        class Green:
            background_color = palette["Green"]["Dark"]["Background"]
            accent_color = palette["Green"]["AccentColor"]

        class Blue:
            background_color = palette["Blue"]["Dark"]["Background"]
            accent_color = palette["Blank"]["AccentColor"]

        class Pink:
            background_color = palette["Pink"]["Dark"]["Background"]
            accent_color = palette["Pink"]["AccentColor"]


class Box:
    background_color = palette["Blank"]["Light"]["WidgetColor"]
    border = Border(Size.pixel(1), BorderLine.solid, "#808080A0")
    border_radius = Size.pixel(10)
    padding = Padding(
        top=Size.pixel(0),
        bottom=Size.pixel(0),
        left=Size.pixel(15),
        right=Size.pixel(15)
    )

    class LightTheme:
        class Blank:
            background_color = palette["Blank"]["Light"]["WidgetColor"]

        class Red:
            background_color = palette["Red"]["Light"]["WidgetColor"]

        class Orange:
            background_color = palette["Orange"]["Light"]["WidgetColor"]

        class Yellow:
            background_color = palette["Yellow"]["Light"]["WidgetColor"]

        class Green:
            background_color = palette["Green"]["Light"]["WidgetColor"]

        class Blue:
            background_color = palette["Blue"]["Light"]["WidgetColor"]

        class Pink:
            background_color = palette["Pink"]["Light"]["WidgetColor"]

    class DarkTheme:
        class Blank:
            background_color = palette["Blank"]["Dark"]["WidgetColor"]

        class Red:
            background_color = palette["Red"]["Dark"]["WidgetColor"]

        class Orange:
            background_color = palette["Orange"]["Dark"]["WidgetColor"]

        class Yellow:
            background_color = palette["Yellow"]["Dark"]["WidgetColor"]

        class Green:
            background_color = palette["Green"]["Dark"]["WidgetColor"]

        class Blue:
            background_color = palette["Blue"]["Dark"]["WidgetColor"]

        class Pink:
            background_color = palette["Pink"]["Dark"]["WidgetColor"]


class Navbar:
    height = Size.pixel(100)
    width = Size.pixel(60)
    overflow = Visibility.hidden
    border_radius = Size.pixel(10)
    z_index = 9999
    padding = Padding(
        right=Size.pixel(5)
    )
    position = Position.fixed(
        top=Size.pixel(20),
        bottom=Size.pixel(20),
        left=Size.pixel(10)
    )

    class RawItem:
        float = Float.right
        text_align = Align.center
        text_decoration = NoStyle
        font_size = Size.pixel(17)
        color = Color.white
        align_items = Align.left

    class ActiveItem:
        border_radius = Size.pixel(15)
        align_items = Align.left
        cursor = Cursor.pointer
        border = NoStyle
        padding = Padding(
            top=Size.pixel(14),
            bottom=Size.pixel(14),
            left=Size.pixel(16),
            right=Size.pixel(16)
        )

    class InactiveItem:
        background_color = Color.transparent
        border_radius = Size.pixel(15)
        align_items = Align.left
        cursor = Cursor.pointer
        color = Color.black
        border = NoStyle
        padding = Padding(
            top=Size.pixel(14),
            bottom=Size.pixel(14),
            left=Size.pixel(16),
            right=Size.pixel(16)
        )

    class Icon:
        float = Float.left
        text_align = Align.center
        text_decoration = NoStyle
        padding = Padding(
            left=Size.pixel(10),
        )

    class LightTheme:
        class Blank:
            active_item_color = Color.white
            active_item_background_color = palette["Blank"]["AccentColor"]

        class Red:
            active_item_color = Color.white
            active_item_background_color = palette["Red"]["AccentColor"]

        class Orange:
            active_item_color = Color.white
            active_item_background_color = palette["Orange"]["AccentColor"]

        class Yellow:
            active_item_color = Color.white
            active_item_background_color = palette["Yellow"]["AccentColor"]

        class Green:
            active_item_color = Color.white
            active_item_background_color = palette["Green"]["AccentColor"]

        class Blue:
            active_item_color = Color.white
            active_item_background_color = palette["Blank"]["AccentColor"]

        class Pink:
            active_item_color = Color.white
            active_item_background_color = palette["Pink"]["AccentColor"]

    DarkTheme = LightTheme


class Topbar:
    height = Size.pixel(75)
    overflow = Visibility.hidden
    border_radius = Size.pixel(10)
    z_index = 9999
    padding = Padding(
        right=Size.pixel(5),
        top=Size.pixel(20)
    )
    position = Position.fixed(
        top=Size.pixel(0),
        left=Size.pixel(0),
        right=Size.pixel(0)
    )
    margin = Margin(
        top=Size.pixel(-10)
    )

    class Item:
        background_color = Color.transparent
        border_radius = Size.pixel(15)
        align_items = Align.left
        cursor = Cursor.pointer
        float = Float.right
        color = Color.black
        border = NoStyle
        padding = Padding(
            top=Size.pixel(14),
            bottom=Size.pixel(14),
            left=Size.pixel(16),
            right=Size.pixel(16)
        )
        css = {"filter": "drop-shadow(1px 1px 1px #808080A0)"}
