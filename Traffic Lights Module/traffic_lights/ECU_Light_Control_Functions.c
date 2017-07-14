#include "ECU_Light_Control_Functions.h"

//North >> PB2, PE0, PF0 >> red , orange , green
//West >> C5,C6,C7 >> Red yellow Green
//East >> A4,A3,A2 Red Orange Green
//South A5,A6,A7 Red yellow green
void Lights_Init(void)
{
	unsigned long volatile delay;
	// PORTA Init Pins 2 ---> 7
	SYSCTL_RCGC2_R |= 0x01;           // Port A clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles
	GPIO_PORTA_DIR_R |= 0xFC;					// Enable as output
	GPIO_PORTA_AFSEL_R &= ~0xFC;      // not alternative
  GPIO_PORTA_AMSEL_R &= ~0xFC;      // no analog
  GPIO_PORTA_PCTL_R &= ~0xFFFFFF00; // bits for PA2 ---> PA7
	GPIO_PORTA_DEN_R |= 0xFC;					// Enable Digital Function
	
	// PORTB Init Pin 2
	SYSCTL_RCGC2_R |= 0x02;           // Port B clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles
	GPIO_PORTB_DIR_R |= 0x04;					// Enable as output
	GPIO_PORTB_AFSEL_R &= ~0x04;      // not alternative
  GPIO_PORTB_AMSEL_R &= ~0x04;      // no analog
  GPIO_PORTB_PCTL_R &= ~0x00000F00; // bits for PB2
	GPIO_PORTB_DEN_R |= 0x04;					// Enable Digital Function
	
	// PORTC Init Pins 5 ---> 7
	SYSCTL_RCGC2_R |= 0x04;           // Port C clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles	
	GPIO_PORTC_DIR_R |= 0xE0;					// Enable as output
	GPIO_PORTC_AFSEL_R &= ~0xE0;      // not alternative
  GPIO_PORTC_AMSEL_R &= ~0xE0;      // no analog
  GPIO_PORTC_PCTL_R &= ~0xFFF00000; // bits for PC5 ---> PC7
	GPIO_PORTC_DEN_R |= 0xE0;					// Enable Digital Function
	
	// PORTE Init Pin 0
	SYSCTL_RCGC2_R |= 0x10;           // Port E clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles
	GPIO_PORTE_DIR_R |= 0x01;					// Enable as output
	GPIO_PORTE_AFSEL_R &= ~0x01;      // not alternative
  GPIO_PORTE_AMSEL_R &= ~0x01;      // no analog
  GPIO_PORTE_PCTL_R &= ~0x0000000F; // bits for PE0
	GPIO_PORTE_DEN_R |= 0x01;					// Enable Digital Function
	
	// PORTF Init Pin 0
	SYSCTL_RCGC2_R |= 0x20;           // Port F clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles
	
	GPIO_PORTF_LOCK_R = GPIO_LOCK_KEY;
	GPIO_PORTF_CR_R |= 0x01;
	
	GPIO_PORTF_DIR_R |= 0x01;					// Enable as output
	GPIO_PORTF_AFSEL_R &= ~0x01;      // not alternative
  GPIO_PORTF_AMSEL_R &= ~0x01;      // no analog
  GPIO_PORTF_PCTL_R &= ~0x0000000F; // bits for PF0
	GPIO_PORTF_DEN_R |= 0x01;					// Enable Digital Function
}

void North_Green_On(void)
{
	// Pins PB2, PE0 (off)
	// Pin PF0 = 1 (on)
	// North = 0x04;
	GPIO_PORTB_DATA_R &= ~0x04; // red
	GPIO_PORTE_DATA_R &= ~0x01; // orange
	GPIO_PORTF_DATA_R |= 0x01;  // green
}

void North_Orange_On(void)
{
	// North = 0x08;
	GPIO_PORTB_DATA_R &= ~0x04;  // red
	GPIO_PORTE_DATA_R |= 0x01; 	 // orange
	GPIO_PORTF_DATA_R &= ~0x01;  // green
}

void North_Red_On(void)
{
	GPIO_PORTB_DATA_R |= 0x04;   // red
	GPIO_PORTE_DATA_R &= ~0x01;  // orange
	GPIO_PORTF_DATA_R &= ~0x01;  // green
}

void North_Off(void)
{
	// Pins PB2, PE0, PF0 = 0 (off)
	GPIO_PORTB_DATA_R &= ~0x04;   // red
	GPIO_PORTE_DATA_R &= ~0x01;  // orange
	GPIO_PORTF_DATA_R &= ~0x01;  // green
}

void West_Green_On(void)
{
	// C5,C6,C7 >> Red yellow Green

	GPIO_PORTC_DATA_R &= ~0x60;
	GPIO_PORTC_DATA_R |= 0x80;
}

void West_Orange_On(void)
{
	GPIO_PORTC_DATA_R &= ~0xA0;
	GPIO_PORTC_DATA_R |= 0x40;
}

void West_Red_On(void)
{
	GPIO_PORTC_DATA_R &= ~0xC0;
	GPIO_PORTC_DATA_R |= 0x20;
}

void West_Off(void)
{
	// Pins PD0, PD1, PD2 = 0 (off)
	GPIO_PORTC_DATA_R &= ~0xE0;
}

void East_Green_On(void)
{
	//East >> A4,A3,A2 Red Orange Green
	GPIO_PORTA_DATA_R &= ~0x18;
	GPIO_PORTA_DATA_R |= 0x04;
}

void East_Orange_On(void)
{
	GPIO_PORTA_DATA_R &= ~0x14;
	GPIO_PORTA_DATA_R |= 0x08;
}

void East_Red_On(void)
{
	GPIO_PORTA_DATA_R &= ~0x0C;
	GPIO_PORTA_DATA_R |= 0x10;
}

void East_Off(void)
{
	// Pins PA2, PA3, PA4 = 0 (off)
	GPIO_PORTA_DATA_R &= ~0x1C;
}

void South_Green_On(void)
{
	//South A5,6,7 Red yellow green
	GPIO_PORTA_DATA_R &= ~0x60;
	GPIO_PORTA_DATA_R |= 0x80;
}

void South_Orange_On(void)
{
	GPIO_PORTA_DATA_R &= ~0xA0;
	GPIO_PORTA_DATA_R |= 0x40;
}

void South_Red_On(void)
{
	GPIO_PORTA_DATA_R &= ~0xC0;
	GPIO_PORTA_DATA_R |= 0x20;
}

void South_Off(void)
{
	// Pins PA5, PA6, PA7 = 0 (off)
	GPIO_PORTA_DATA_R &= ~0xE0;
}

void Change_Lights(unsigned char direction, mode m)
{
	switch(m)
	{
		case GREEN:
			switch(direction)
			{
				case 'N':
					North_Green_On(); South_Red_On();	East_Red_On(); West_Red_On();
					break;
				case 'S':
					North_Red_On();	South_Green_On(); East_Red_On(); West_Red_On();
					break;
				case 'E':
					North_Red_On(); South_Red_On(); East_Green_On(); West_Red_On();
					break;
				case 'W':
					North_Red_On(); South_Red_On(); East_Red_On(); West_Green_On();
					break;
			}
			break;
			
		case ORANGE:
			switch(direction)
			{
				case 'N':
					North_Orange_On();
					break;
				case 'S':
					South_Orange_On();
					break;
				case 'E':
					East_Orange_On();
					break;
				case 'W':
					West_Orange_On();
					break;
			}
			break;
			
		case ORANGE_EXCEPT:
			switch(direction)
			{
				case 'N':
					North_Green_On(); South_Orange_On(); East_Orange_On();	West_Orange_On();
					break;
				case 'S':
					North_Orange_On(); South_Green_On(); East_Orange_On(); West_Orange_On();
					break;
				case 'E':
					North_Orange_On(); South_Orange_On(); East_Green_On(); West_Orange_On();
					break;
				case 'W':
					North_Orange_On(); South_Orange_On(); East_Orange_On(); West_Green_On();
					break;
			}
			break;
	}
}
