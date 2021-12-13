##CHANGE TAB BAR

import dearpygui.dearpygui as dpg

dpg.create_context()

def change_tab(sender, app_data):
    if sender == 100:
        dpg.set_value("tag_bar", "tab2")
    else:
        dpg.set_value("tag_bar", "tab1")


with dpg.window(label="Window", tag="window"):
    with dpg.tab_bar(tag="tag_bar") as tb:
        with dpg.tab(label="tab 1", tag="tab1"):
            dpg.add_button(label="activate tab 2", callback=change_tab, tag=100)
        with dpg.tab(label="tab 2", tag="tab2"):
            dpg.add_button(label="activate tab 1", tag=200, callback=change_tab,)

dpg.create_viewport(title="Viewport")
dpg.set_primary_window("window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
