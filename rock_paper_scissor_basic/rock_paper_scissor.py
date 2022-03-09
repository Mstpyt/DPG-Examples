import dearpygui.dearpygui as dpg
import random


def play(sender, app_data, user_data):
    comp = random.randint(1, 3)
    if user_data == comp:
        dpg.set_value("game_play", f"Both players selected {dpg.get_item_label(sender)}. It's a tie!")
    elif user_data == 1:
        if comp == 3:
            dpg.set_value("player_score", int(dpg.get_value("player_score"))+1)
            dpg.set_value("game_play", "Rock smashes scissors! You win!")
        else:
            dpg.set_value("comp_score", int(dpg.get_value("comp_score")) + 1)
            dpg.set_value("game_play", "Paper covers rock! You lose.")
    elif user_data == 2:
        if comp == 1:
            dpg.set_value("player_score", int(dpg.get_value("player_score")) + 1)
            dpg.set_value("game_play", "Paper covers rock! You win!")
        else:
            dpg.set_value("comp_score", int(dpg.get_value("comp_score")) + 1)
            dpg.set_value("game_play", "Scissors cuts paper! You lose.")
    elif user_data == 3:
        if comp == 1:
            dpg.set_value("player_score", int(dpg.get_value("player_score")) + 1)
            dpg.set_value("game_play", "Scissors cuts paper! You win!")
        else:
            dpg.set_value("comp_score", int(dpg.get_value("comp_score")) + 1)
            dpg.set_value("game_play", "Rock smashes scissors! You lose.")



dpg.create_context()
dpg.create_viewport(title="Rock Paper Scissor", width=200, height=200, vsync=True)
dpg.setup_dearpygui()
dpg.configure_app(auto_device=True)

with dpg.window(label="Tutorial") as main:
    with dpg.group(horizontal=True):
        dpg.add_text("Score:")
        dpg.add_text(default_value="0", tag="player_score")
        dpg.add_text(default_value="0", tag="comp_score")
    with dpg.group(horizontal=True):
        dpg.add_button(label="Rock", callback=play, user_data=1)
        dpg.add_button(label="Paper", callback=play, user_data=2)
        dpg.add_button(label="Scissor", callback=play, user_data=3)
    dpg.add_separator()
    dpg.add_text(tag="game_play", wrap=200)

dpg.set_primary_window(main, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
