import dearpygui.dearpygui as dpg
from translate import Translator


def translate(_, app_data):
    translator = Translator(from_lang=dpg.get_value("language_from"), to_lang=dpg.get_value("language_to"))
    dpg.set_value("translated_text", translator.translate(app_data))


def check_languages():
    if dpg.get_value("language_from") and dpg.get_value("language_to"):
        dpg.enable_item("input_text")


def init():
    with dpg.window(label="Language Translator", tag="main_window"):
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=True):
                dpg.add_text(default_value="From Language:")
                dpg.add_combo(items=['en', 'de', 'fr', 'it'],  tag='language_from', width=80, callback=check_languages)
            with dpg.group(horizontal=True):
                dpg.add_text(default_value="To Language:")
                dpg.add_combo(items=['en', 'de', 'fr', 'it'], tag='language_to', width=80, callback=check_languages)
        dpg.add_input_text(multiline=True, hint="enter a text", callback=translate, enabled=False, tag="input_text")
        dpg.add_text(tag="translated_text")


if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title='Language Translator', width=600, height=300)
    init()
    dpg.set_primary_window("main_window", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

