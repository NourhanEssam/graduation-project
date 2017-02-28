#include "PLL.h"
#include "GSM.h"
#include "SysTick.h"

int main(void)
{
	PLL_Init();
	SysTick_Init();
	GSM_Init();
	
	while(1)
	{
		GSM_Connect_To("127.0.0.1", "80");
		GSM_Send("HelloGSM");
		GSM_Close_Connection();
		SysTick_Wait10ms(1);
	}
}
