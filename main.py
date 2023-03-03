def on_button_pressed_a():
    # Skapar en funktion som kan k;ras
    # Skrolla hej på skärmen
    basic.show_string("test")
input.on_button_pressed(Button.A, on_button_pressed_a)

# Skapa en funktionen som tänder 4 slumpade lysdioder
# Registrera att funktionen on_gesture_shake körs när man skakar

def on_gesture_shake():
    for index in range(4):
        led.plot(randint(0, 5), randint(0, 5))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Skapa en funktion som rensar skärmen

def on_button_pressed_b():
    basic.clear_screen()
# Registrera att on_button_pressed_b körs när knapp B trycks ner
input.on_button_pressed(Button.B, on_button_pressed_b)

#kör en loop 10 gånger
for x in range(10):
    basic.show_icon(IconNames.HEART,500) # Visar ett Hjärta i 0.5s
    basic.show_icon(IconNames.SMALL_HEART,200) # Visar ett litet hjärta i 0.2s