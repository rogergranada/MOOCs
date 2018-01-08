#define GREEN_PIN 8
#define YELLOW_PIN 10
#define RED_PIN 12

int red_on = 3000;
int red_yellow_on = 1000;
int green_on = 3000;
int green_blink = 500;
int yellow_on = 1000;

void setup(){
    // set the ports as output to control LEDs
    pinMode(RED_PIN, OUTPUT);
    pinMode(YELLOW_PIN, OUTPUT);
    pinMode(GREEN_PIN, OUTPUT);
}

void loop(){
    // control the semaphore
    // turn on the RED_PIN
    digitalWrite(RED_PIN, HIGH);
    // wait while the red signal is on
    delay(red_on);

    // turn on the YELLOW_PIN
    digitalWrite(YELLOW_PIN, HIGH);
    delay(red_yellow_on);

    // turn on the YELLOW_PIN
    digitalWrite(RED_PIN, LOW);
    digitalWrite(YELLOW_PIN, LOW);
    digitalWrite(GREEN_PIN, HIGH);
    delay(green_on);
    digitalWrite(GREEN_PIN, LOW);

    for (int i=0; i<3; i=i+1){
        delay(green_blink);
        digitalWrite(GREEN_PIN, HIGH);
        delay(green_blink);
        digitalWrite(GREEN_PIN, LOW);
    }

    // turn yellow on now
    digitalWrite(YELLOW_PIN, HIGH);
    delay(yellow_on);
    digitalWrite(YELLOW_PIN, LOW);
    
}