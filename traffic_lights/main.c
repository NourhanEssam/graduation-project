#include "PLL.h"
#include "Timers_Functions.h"
#include "UART.h"

#define INTERSECTION_ID 1
#define NORTH 'N'
#define SOUTH 'S'
#define EAST 	'E'
#define WEST	'W'

// global variables
unsigned char direction;
unsigned char id;

// basic functions defined at end of startup.s
void DisableInterrupts(void); // Disable interrupts
void EnableInterrupts(void);  // Enable interrupts
void WaitForInterrupt(void);  // low power mode

// UART1 interrupt handler
void UART1_Handler(void)
{
	UART1_ICR_R |= 0x00000010;
	direction = UART1_InCharNonBlocking();
	id = UART1_InCharNonBlocking();
	if(id == INTERSECTION_ID && (direction == NORTH || direction == SOUTH || direction == EAST || direction == WEST))
	{
		// change state to an emergency state
	}
}

int main(void)
{
	PLL_Init();
	SysTick_Init();
	UART1_Init();
	EnableInterrupts();
	UART1_Interrupt_Enable();
	while(1)
	{
		
		SysTick_delay10MS(50);
	}
}

