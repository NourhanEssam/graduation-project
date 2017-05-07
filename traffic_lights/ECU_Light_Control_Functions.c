#include "ECU_Light_Control_Functions.h"


void Lights_Init(void)
{
	unsigned long volatile delay;
	// PORTB Init Pins 2 ---> 7
	SYSCTL_RCGC2_R |= 0x02;           // Port B clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles
	GPIO_PORTB_DIR_R |= 0xFC;					// Enable as output
	GPIO_PORTB_AFSEL_R &= ~0xFC;      // not alternative
  GPIO_PORTB_AMSEL_R &= ~0xFC;      // no analog
  GPIO_PORTB_PCTL_R &= ~0xFFFFFF00; // bits for PB2 ---> PB7
	GPIO_PORTB_DEN_R |= 0xFC;					// Enable Digital Function
	
	// PORTE Init Pins 0 ---> 5
	SYSCTL_RCGC2_R |= 0x10;           // Port E clock
  delay = SYSCTL_RCGC2_R;           // wait 3-5 bus cycles
	GPIO_PORTE_DIR_R |= 0x3F;					// Enable as output
	GPIO_PORTE_AFSEL_R &= ~0x3F;      // not alternative
  GPIO_PORTE_AMSEL_R &= ~0x3F;      // no analog
  GPIO_PORTE_PCTL_R &= ~0x00FFFFFF; // bits for PE0	---> PE5
	GPIO_PORTE_DEN_R |= 0x3F;					// Enable Digital Function
}

void North_Green_On(void)
{
	// Pins PB3, PB4 (off)
	// Pin PB2 = 1 (on)
	North = 0x04;
}

void North_Orange_On(void)
{
	// Pins PB2, PB4 (off)
	// Pin PB3 = 1 (on)
	North = 0x08;
}

void North_Red_On(void)
{
	// Pins PB2, PB3 (off)
	// Pin PB4 = 1 (on)
	North = 0x10;
}

void North_Off(void)
{
	// Pins PB2, PB3, PB4 = 0 (off)
	North = 0;
}

void West_Green_On(void)
{
	// Pins PB6, PB7 = 0 (off)
	// Pin PB5 = 1 (on)
	West = 0x20;
}

void West_Orange_On(void)
{
	// Pins PB5, PB7 = 0 (off)
	// Pin PB6 = 1 (on)
	West = 0x40;
}

void West_Red_On(void)
{
	// Pins PB5, PB6 = 0 (off)
	// Pin PB7 = 1 (on)
	West = 0x80;
}

void West_Off(void)
{
	// Pins PB5, PB6, PB7 = 0 (off)
	West = 0;
}

void East_Green_On(void)
{
	// Pins PE1, PE2 = 0 (off)
	// Pin PE0 = 1 (on)
	East = 0x01;
}

void East_Orange_On(void)
{
	// Pins PE0, PE2 = 0 (off)
	// Pin PE1 = 1 (on)
	East = 0x02;
}

void East_Red_On(void)
{
	// Pins PE0, PE1 = 0 (off)
	// Pin PE2 = 1 (on)
	East = 0x04;
}

void East_Off(void)
{
	// Pins PE0, PE1, PE2 = 0 (off)
	East = 0;
}

void South_Green_On(void)
{
	// Pins PE4, PE5 = 0 (off)
	// Pin PE3 = 1 (on)
	South = 0x08;
}

void South_Orange_On(void)
{
	// Pins PE3, PE5 = 0 (off)
	// Pin PE4 = 1 (on)
	South = 0x10;
}

void South_Red_On(void)
{
	// Pins PE3, PE4 = 0 (off)
	// Pin PE5 = 1 (on)
	South = 0x20;
}

void South_Off(void)
{
	// Pins PE3, PE4, PE5 = 0 (off)
	South = 0;
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
