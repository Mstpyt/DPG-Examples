import dearpygui.dearpygui as dpg

dpg.create_context()


def render_window_center(sender, app_data, user_data):
    if dpg.does_item_exist(user_data):
        main_width = dpg.get_viewport_width()
        main_height = dpg.get_viewport_height()
        login_width = dpg.get_item_width(user_data)
        login_height = dpg.get_item_height(user_data)
        dpg.set_item_pos(user_data, [int((main_width // 2 - login_width // 2)),
                                     int((main_height / 2 - login_height / 2))])


class PopupFactory:
    def __init__(self, item_id, width, height, title=None, no_background=False, title_bar=True):
        self.item_id = item_id
        self.width = width
        self.height = height
        self.autosize = self.width <= 0
        self.label = title
        self.background = no_background
        self.title_bar = title_bar

    def create_popup(self):
        dpg.add_window(modal=True, no_close=True, no_move=True, width=self.width, height=self.height,
                       tag=self.item_id, autosize=self.autosize,
                       label=self.label, no_open_over_existing_popup=False,
                       no_title_bar=self.title_bar, no_background=self.background, no_resize=True,
                       pos=[int((dpg.get_viewport_width() // 2 - 500 // 2)),
                            int((dpg.get_viewport_height() // 2 - 500 // 2))])
        with dpg.item_handler_registry(tag=dpg.generate_uuid()) as handler:
            dpg.add_item_visible_handler(callback=render_window_center, parent=handler, user_data=self.item_id)
        dpg.bind_item_handler_registry(item=self.item_id, handler_registry=handler)


def create_msg_popup():
    if dpg.does_item_exist("test_popup"):
        dpg.delete_item("test_popup")
    popup = PopupFactory("test_popup", 200, 150, "Test Message", False, False)
    popup.create_popup()
    with dpg.group(parent="test_popup"):
        dpg.add_text(default_value="This is a test Popup")
        dpg.add_spacer()
        dpg.add_button(label="Close", user_data=("test_popup", True),
                       callback=lambda sender, app_data, user_data: dpg.delete_item("test_popup"))


with dpg.window(label="Popups", tag="Primary Window"):
    dpg.add_button(label="Open Message", callback=create_msg_popup)

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
