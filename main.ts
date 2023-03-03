input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  Skapar en funktion som kan k;ras
    //  Skrolla hej på skärmen
    basic.showString("test")
})
//  Skapa en funktionen som tänder 4 slumpade lysdioder
//  Registrera att funktionen on_gesture_shake körs när man skakar
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    for (let index = 0; index < 4; index++) {
        led.plot(randint(0, 5), randint(0, 5))
    }
})
//  Skapa en funktion som rensar skärmen
//  Registrera att on_button_pressed_b körs när knapp B trycks ner
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.clearScreen()
})
// kör en loop 10 gånger
for (let x = 0; x < 10; x++) {
    basic.showIcon(IconNames.Heart, 500)
    //  Visar ett Hjärta i 0.5s
    basic.showIcon(IconNames.SmallHeart, 200)
}
