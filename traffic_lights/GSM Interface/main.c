#include "PLL.h"
#include "GSM.h"

unsigned char * buffer_rcv;

// basic functions defined at end of startup.s
void DisableInterrupts(void); // Disable interrupts
void EnableInterrupts(void);  // Enable interrupts
void WaitForInterrupt(void);  // low power mode

// UART1 interrupt handler
void UART1_Handler(void)
{
	//buffer_rcv = GSM_Rcv(100);
}

int main(void)
{
	unsigned char buffer[10];
	PLL_Init();
	SysTick_Init();
	GSM_Init();
	EnableInterrupts();
	
	while(1)
	{
		GSM_Connect_To("\"127.0.0.1\"", "\"80\"");
		GSM_Send("HelloGSM");
		GSM_Rcv(buffer, 10);
		GSM_Close_Connection();
		SysTick_Wait10ms(1000);
	}
}
