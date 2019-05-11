// 1ci opamp 5ci bacak GROUND baglanacak

// #include <SoftwareSerial.h>

// SoftwareSerial bt_iletisim(7, 6); // RX,TX
int data = 10;

int bPins[] = {1,2,3};
int bits[3];

void setup()
{
  Serial.begin(9600);
  // bt_iletisim.begin(9600);

  for (int thisPin = 0; thisPin < 3; thisPin++) {
    pinMode(bPins[thisPin], INPUT);
  }
  
}

void loop()
{
  
  for (int i = 0; i < 3; i++)
  {
    bits[i] = digitalRead(bPins[i]);
  }
  
  for (byte i = 0; i < 3; i = i + 1) {
    Serial.println(bits[i]);
  }
  
  Serial.println("***************");

  // bt_iletisim.println(data);
  // data += 10;
  // Serial.println(data);

  delay(100);
  
}