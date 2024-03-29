#ifndef __PLL__
#define __PLL__

#include "tm4c123gh6pm.h"

#define SYSDIV2 4
// bus frequency is 400MHz/(SYSDIV2+1) = 400MHz/(4+1) = 80 MHz

// configure the system to get its clock from the PLL
void PLL_Init(void);

#endif
