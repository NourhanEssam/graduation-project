#pragma once
#include "ECU_Light_Control_Functions.h"


void Lights_Init(void)
{
	
	// Enable the peripherals themselves
	SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOB);
	SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOE);
	
	//Check if B is working (wait till its ready)
	while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOB))
    {
    }
	
	// Check if E is working (wait till its ready)
	while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOE))
    {
    }
}




void North_Green_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(North_Port, North_Green);
	
	// Pin output = 1 (on)
	GPIOPinWrite(North_Port, North_Green, North_Green);

}

void North_Green_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(North_Port, North_Green);
	
	// Pin output = 0 (off)
	GPIOPinWrite(North_Port, North_Green, 0);

}

void North_Orange_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(North_Port, North_Orange);
	
	// Pin output = 1 (on)
	GPIOPinWrite(North_Port, North_Orange, North_Orange);

}

void North_Orange_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(North_Port, North_Orange);
	
	// Pin output = 0 (off)
	GPIOPinWrite(North_Port, North_Orange, 0);

}

void North_Red_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(North_Port, North_Red);
	
	// Pin output = 1 (on)
	GPIOPinWrite(North_Port, North_Red, North_Red);

}

void North_Red_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(North_Port, North_Red);
	
	// Pin output = 0 (off)
	GPIOPinWrite(North_Port, North_Red, 0);

}

void West_Green_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(West_Port, West_Green);
	
	// Pin output = 1 (on)
	GPIOPinWrite(West_Port, West_Green, West_Green);

}

void West_Green_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(West_Port, West_Green);
	
	// Pin output = 0 (off)
	GPIOPinWrite(West_Port, West_Green, 0);

}

void West_Orange_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(West_Port, West_Orange);
	
	// Pin output = 1 (on)
	GPIOPinWrite(West_Port, West_Orange, West_Orange);

}

void West_Orange_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(West_Port, West_Orange);
	
	// Pin output = 0 (off)
	GPIOPinWrite(West_Port, West_Orange, 0);

}

void West_Red_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(West_Port, West_Red);
	
	// Pin output = 1 (on)
	GPIOPinWrite(West_Port, West_Red, West_Red);

}

void West_Red_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(West_Port, West_Red);
	
	// Pin output = 0 (off)
	GPIOPinWrite(West_Port, West_Red, 0);

}

void East_Green_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(East_Port, East_Green);
	
	// Pin output = 1 (on)
	GPIOPinWrite(East_Port, East_Green, East_Green);

}

void East_Green_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(East_Port, East_Green);
	
	// Pin output = 0 (off)
	GPIOPinWrite(East_Port, East_Green, 0);

}

void East_Orange_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(East_Port, East_Orange);
	
	// Pin output = 1 (on)
	GPIOPinWrite(East_Port, East_Orange, East_Orange);

}

void East_Orange_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(East_Port, East_Orange);
	
	// Pin output = 0 (off)
	GPIOPinWrite(East_Port, East_Orange, 0);

}

void East_Red_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(East_Port, East_Red);
	
	// Pin output = 1 (on)
	GPIOPinWrite(East_Port, East_Red, East_Red);

}

void East_Red_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(East_Port, East_Red);
	
	// Pin output = 0 (off)
	GPIOPinWrite(East_Port, East_Red, 0);

}

void South_Green_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(South_Port, South_Green);
	
	// Pin output = 1 (on)
	GPIOPinWrite(South_Port, South_Green, South_Green);

}

void South_Green_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(South_Port, South_Green);
	
	// Pin output = 0 (off)
	GPIOPinWrite(South_Port, South_Green, 0);

}

void South_Orange_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(South_Port, South_Orange);
	
	// Pin output = 1 (on)
	GPIOPinWrite(South_Port, South_Orange, South_Orange);

}

void South_Orange_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(South_Port, South_Orange);
	
	// Pin output = 0 (off)
	GPIOPinWrite(South_Port, South_Orange, 0);

}

void South_Red_On(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(South_Port, South_Red);
	
	// Pin output = 1 (on)
	GPIOPinWrite(South_Port, South_Red, South_Red);

}

void South_Red_Off(void)
{
	// Init it as output bit
	GPIOPinTypeGPIOOutput(South_Port, South_Red);
	
	// Pin output = 0 (off)
	GPIOPinWrite(South_Port, South_Red, 0);

}

