// PISCAR UM LED EXTERNO, CONECTADO AO DIGITAL PIN 5 E AO GND
/*
Considerando que o Arduino opera com uma corrente
de 20 mA e voltagem de 5 V, e o LED opera à 20 mA 
e voltagem de 2V, é necessário conectar um resistor
de 150 Ohms entre o LED e o Arduino.
*/

int time = 1000;
int ledPin = 5;

void setup() {
    pinMode(ledPin, OUTPUT);
}

void loop() {
    digitalWrite(ledPin, HIGH);
    delay(time);
    digitalWrite(ledPin, LOW);
    delay(time);
}
