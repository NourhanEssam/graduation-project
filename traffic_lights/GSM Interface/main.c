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
	int a = 0;
	//buffer_rcv = GSM_Rcv(100);
}

int main(void)
{
	int i = 0;
	unsigned char buffer[100];
	PLL_Init();
	SysTick_Init();
	GSM_Init();
	EnableInterrupts();
	while(1)
	{
		GSM_Connect_To("\"41.233.31.195\"", "\"31001\"");
		SysTick_Wait10ms(100);
		GSM_Send("GET / HTTP/1.1\r\n\r\n");
		SysTick_Wait10ms(1000);
		GSM_Rcv(buffer, 100);
		GSM_Close_Connection();
		SysTick_Wait10ms(100);
	}
}
