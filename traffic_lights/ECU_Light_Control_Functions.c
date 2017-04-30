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
	// Pin PB2 = 1 (on)
	North_Green = 0xFF;
}

void North_Green_Off(void)
{
	// Pin PB2 = 0 (off)
	North_Green = 0;
}

void North_Orange_On(void)
{
	// Pin PB3 = 1 (on)
	North_Orange = 0xFF;
}

void North_Orange_Off(void)
{
	// Pin PB3 = 0 (off)
	North_Orange = 0;
}

void North_Red_On(void)
{
	// Pin PB4 = 1 (on)
	North_Red = 0xFF;
}

void North_Red_Off(void)
{
	// Pin PB4 = 0 (off)
	North_Red = 0;
}

void West_Green_On(void)
{
	// Pin PB5 = 1 (on)
	West_Green = 0xFF;
}

void West_Green_Off(void)
{
	// Pin PB5 = 0 (off)
	West_Green = 0;
}

void West_Orange_On(void)
{
	// Pin PB6 = 1 (on)
	West_Orange = 0xFF;
}

void West_Orange_Off(void)
{
	// Pin PB6 = 0 (off)
	West_Orange = 0;
}

void West_Red_On(void)
{
	// Pin PB7 = 1 (on)
	West_Red = 0xFF;
}

void West_Red_Off(void)
{
	// Pin PB7 = 0 (off)
	West_Red = 0;
}

void East_Green_On(void)
{
	// Pin PE0 = 1 (on)
	East_Green = 0xFF;
}

void East_Green_Off(void)
{
	// Pin PE0 = 0 (off)
	East_Green = 0;
}

void East_Orange_On(void)
{
	// Pin PE1 = 1 (on)
	East_Orange = 0xFF;
}

void East_Orange_Off(void)
{
	// Pin PE1 = 0 (off)
	East_Orange = 0;
}

void East_Red_On(void)
{
	// Pin PE2 = 1 (on)
	East_Red = 0xFF;
}

void East_Red_Off(void)
{
	// Pin PE2 = 0 (off)
	East_Red = 0;
}

void South_Green_On(void)
{
	// Pin PE3 = 1 (on)
	South_Green = 0xFF;
}

void South_Green_Off(void)
{
	// Pin PE3 = 0 (off)
	South_Green = 0;
}

void South_Orange_On(void)
{
	// Pin PE4 = 1 (on)
	South_Orange = 0xFF;
}

void South_Orange_Off(void)
{
	// Pin PE4 = 0 (off)
	South_Orange = 0;
}

void South_Red_On(void)
{
	// Pin PE5 = 1 (on)
	South_Red = 0xFF;
}

void South_Red_Off(void)
{
	// Pin PE5 = 0 (off)
	South_Red = 0;
}
