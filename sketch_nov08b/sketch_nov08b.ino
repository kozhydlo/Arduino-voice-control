#include <Firmata.h>

void setup() {
  // Встановлюємо пін 9 як вихідний для керування світлодіодом
  Firmata.setPinMode(9, PIN_MODE_SERVO);
  Firmata.begin(57600);
}

void loop() {
  // Викликаємо основну функцію обробки команд від комп'ютера
  while (Firmata.available()) {
    Firmata.processInput();
  }
}

void analogWriteCallback(byte port, int value) {
  // Ця функція викликається при отриманні команди від комп'ютера
  if (port == 9) {
    if (value > 0) {
      // Увімкнути світлодіод
      digitalWrite(9, HIGH);
    } else {
      // Вимкнути світлодіод
      digitalWrite(9, LOW);
    }
  }
}
