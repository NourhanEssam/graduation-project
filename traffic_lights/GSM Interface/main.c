#include "PLL.h"
#include "GSM.h"

int main(void)
{
	unsigned char * buffer;
	
	PLL_Init();
	SysTick_Init();
	GSM_Init();
	while(1)
	{
		GSM_Connect_To("127.0.0.1", "80");
		GSM_Send("HelloGSM");
		buffer = GSM_Rcv(10);
		free(buffer);
		GSM_Close_Connection();
		SysTick_Wait10ms(100);
	}
}
