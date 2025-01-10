function SUPERPUPERMEGAINTRO (micro: boolean, fan: boolean, strip: boolean, LCD: boolean, servodoor: boolean, led2: boolean) {
    if (micro) {
        basic.showIcon(IconNames.Happy)
        music.play(music.stringPlayable("D E F G C5 B A A ", 180), music.PlaybackMode.UntilDone)
    }
    basic.pause(2000)
    if (fan) {
        pins.analogWritePin(AnalogPin.P12, 256)
        basic.pause(1000)
        pins.analogWritePin(AnalogPin.P12, 0)
        pins.analogWritePin(AnalogPin.P13, 256)
        basic.pause(1000)
        pins.analogWritePin(AnalogPin.P13, 0)
    }
    basic.pause(2000)
    if (strip) {
        for (let index = 0; index <= 4; index++) {
            strip.setPixelColor(index, [
            neopixel.colors(NeoPixelColors.Red),
            neopixel.colors(NeoPixelColors.Green),
            neopixel.colors(NeoPixelColors.Yellow),
            neopixel.colors(NeoPixelColors.Blue)
            ][index])
            strip.show()
            basic.pause(250)
        }
    }
    basic.pause(2000)
    if (LCD) {
        I2C_LCD1602.BacklightOn()
        for (let index2 = 0; index2 <= 15; index2++) {
            I2C_LCD1602.ShowString("1", index2, 0)
            basic.pause(50)
        }
        basic.pause(500)
        I2C_LCD1602.clear()
    }
    basic.pause(2000)
    if (led2) {
        for (let index = 0; index <= 18; index++) {
            pins.servoWritePin(AnalogPin.P8, index * 10)
            basic.pause(100)
        }
        for (let index = 0; index <= 18; index++) {
            pins.servoWritePin(AnalogPin.P8, 180 - index * 10)
            basic.pause(100)
        }
    }
    basic.pause(2000)
    if (true) {
        for (let index = 0; index <= 10; index++) {
            pins.digitalWritePin(DigitalPin.P16, 1)
            basic.pause(1000 - index * 100)
            pins.digitalWritePin(DigitalPin.P16, 0)
            basic.pause(1000 - index * 100)
        }
    }
}
function intro (micro: boolean, fan: boolean, led2: boolean, bool2: boolean) {
	
}
function init () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P13, 0)
    I2C_LCD1602.LcdInit(0)
    I2C_LCD1602.BacklightOff()
    I2C_LCD1602.on()
    strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
    strip.clear()
    strip.show()
    pins.digitalWritePin(DigitalPin.P16, 0)
}
let strip: neopixel.Strip = null
init()
intro(true, true, true, true)
basic.forever(function () {
	
})
