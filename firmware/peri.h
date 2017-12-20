//#define IS_SWITCH_PRESSED() ((PINC & (1 << PC1)) ^ (1 << PC1))
#define IS_SWITCH_PRESSED() ((PINC & 0b10) == 0b10)

void init_peripheral();
uint16_t read_adc(uint8_t channel);
uint16_t get_light(uint8_t channel);

#define digital_high(pin, no)   (pin = pin | (1 << no))
#define digital_low(pin, no)    (pin = pin & ~(1 << no))
#define digital_read(pin, no)   ((pin >> no) & 0b1)
#define delay(ms)               _delay_ms(ms)