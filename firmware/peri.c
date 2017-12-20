#include <avr/io.h>
#include "peri.h"

void init_peripheral()
{	
	DDRC &= ~((1 << PC0) | (1 << PC2)); //set pc0 and pc2 to input
	DDRC &= ~((1 << PC1)); // set pc1 to input
	
	//PORTC |= (1 << PC1); //set pull up PC1
}

uint16_t read_adc(uint8_t channel) {
	ADMUX = (0 << REFS1) | (1 << REFS0) | (0 << ADLAR) | (channel & 0b1111);
	ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0) | (1 << ADSC);
	while((ADCSRA & (1 << ADSC)));
	return ADCL + ADCH*256;  
}

uint16_t get_light(uint8_t channel) {
    return read_adc(channel);
}
