import dearpygui.dearpygui as dpg
import time


def init():
    with dpg.window(tag="main_window"):
        dpg.add_text(tag="clock_label")
        dpg.set_global_font_scale(2.0)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    dpg.set_value("clock_label", time_live)


if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title='Digital Clock', width=420, height=150)
    init()
    dpg.set_primary_window("main_window", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        digital_clock()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()
