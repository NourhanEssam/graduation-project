#include "PLL.h"
#include "GSM.h"

// This is the code that gets called when the processor first starts execution
// following a reset event.
void SystemInit(void)
{
}

int main(void)
{
	PLL_Init();
	GSM_Init();
	
	while(1)
	{
		
	}
}