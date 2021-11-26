import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()

def stage_card_to_payload(sender, data, user):
    print(data)
    print(user)
    card = sender
    payload = dpg.get_item_children(card, slot=3)[0]
    old_card_window = dpg.get_item_parent(card)

def add_card_from_stage(sender, data, user):
    drop_target_item = sender
    card = data
    old_card_window = dpg.get_item_parent(data)
    print(dpg.get_item_type(drop_target_item))
    new_card_container = dpg.add_child_window(parent=drop_target_item, height=dpg.get_item_height(old_card_window))
    dpg.move_item(card, parent=new_card_container)
    dpg.delete_item(old_card_window)

    print(data)
    # this should be printing drop data, appears there is a bug in dpg

    print(user)

def add_card_item(sender, data, user):
    card = dpg.get_item_parent(sender)
    card_window = dpg.get_item_parent(card)
    new_item = dpg.add_input_text(hint="Some text", parent=dpg.get_item_parent(sender), before=sender)
    old_height = dpg.get_item_height(card_window)
    dpg.set_item_height(card_window, old_height + 23)


def create_new_card(prj_name, prj_hours, parent):
    with dpg.child_window(height=60, parent=parent):
        with dpg.group(drag_callback=stage_card_to_payload, width=-1) as card:
            dpg.add_text(f"Name: {prj_name} | Hours: {prj_hours}")
            dpg.add_button(label="+", callback=add_card_item)
        with dpg.drag_payload(parent=card, payload_type="CARD", drag_data=card, drop_data="drop data"):
            dpg.add_text(prj_name)


def add_chart(chart_name):
    print(f"user_data {chart_name}")
    dpg.add_table_column(parent="tab_chart")
    with dpg.child_window(parent="tab_row", height=-2, drop_callback=add_card_from_stage, payload_type="CARD") as parent_todo:
        with dpg.group(horizontal=True):
            dpg.add_text(chart_name)
        dpg.add_separator()


def open_card_window_popup(sender, app_data, user_data):
    with dpg.mutex():
        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()
        with dpg.window(label="Create Card", modal=True, no_close=True,
                        width=400, height=400, no_title_bar=True, no_background=False, no_resize=True,
                        no_move=False) as modal_id:
            dpg.add_text(default_value="Adding a new Card to the Project")
            dpg.add_input_text(hint="Project Name", tag="card_prj_name")
            dpg.add_input_int(tag="card_prj_hours", step=0)

            with dpg.group(horizontal=True):
                dpg.add_button(label="Create",
                               callback=lambda sender, data,: create_new_card(dpg.get_value("card_prj_name"),
                                                                        dpg.get_value("card_prj_hours"),
                                                                              user_data))
                dpg.add_button(label="Cancle", callback=lambda sender, data: dpg.delete_item(modal_id))

    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
    with dpg.item_handler_registry(tag=dpg.generate_uuid()) as handler:
        dpg.add_item_visible_handler(callback=_render_window_center, parent=handler, user_data=modal_id)
    dpg.bind_item_handler_registry(item=modal_id, handler_registry=handler)


def open_chart_window_popup():
    with dpg.mutex():
        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()
        with dpg.window(label="Create Chart", modal=True, no_close=True,
                        width=400, height=400, no_title_bar=True, no_background=False, no_resize=True,
                        no_move=False) as modal_id:
            dpg.add_text(default_value="Adding a new Chart to the Project")
            dpg.add_input_text(hint="Chart Name", tag="chart_name", on_enter=False)
            dpg.focus_item(dpg.last_item())
            with dpg.group(horizontal=True):
                dpg.add_button(label="Create", callback=lambda sender, data,: add_chart(dpg.get_value("chart_name")))
                dpg.add_button(label="Cancle", callback=lambda sender, data: dpg.delete_item(modal_id))

    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
    with dpg.item_handler_registry(tag=dpg.generate_uuid()) as handler:
        dpg.add_item_visible_handler(callback=_render_window_center, parent=handler, user_data=modal_id)
    dpg.bind_item_handler_registry(item=modal_id, handler_registry=handler)


def _render_window_center(sender, app_data, user_data):
    if dpg.does_item_exist(user_data):
        main_width = dpg.get_viewport_width()
        main_height = dpg.get_viewport_height()
        login_width = dpg.get_item_width(user_data)
        login_height = dpg.get_item_height(user_data)
        dpg.set_item_pos(user_data, [int((main_width // 2 - login_width // 2)),
                                     int((main_height / 2 - login_height / 2))])


def init_gui():
    with dpg.window(label="some window") as mainWin:
        with dpg.group(horizontal=True):
            dpg.add_button(label="Add Chart", callback=open_chart_window_popup)
        with dpg.table(header_row=False, tag="tab_chart"):

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row(tag="tab_row"):
                # height is because table must be taking some space play with styles maybe this wont be needed
                with dpg.child_window(height=-2, drop_callback=add_card_from_stage, payload_type="CARD") as parent_todo:
                    with dpg.group(horizontal=True):
                        dpg.add_text("To Do")
                        dpg.add_button(label="New", callback=open_card_window_popup, user_data=parent_todo)
                    dpg.add_separator()

                with dpg.child_window(height=-2, drop_callback=add_card_from_stage, payload_type="CARD"):
                    dpg.add_text("In Progress")
                    dpg.add_separator()

                with dpg.child_window(height=-2, drop_callback=add_card_from_stage, payload_type="CARD"):
                    dpg.add_text("In Review")
                    dpg.add_separator()

                with dpg.child_window(height=-2, drop_callback=add_card_from_stage, payload_type="CARD"):
                    dpg.add_text("Completed")
                    dpg.add_separator()

    dpg.set_primary_window(mainWin, True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    init_gui()