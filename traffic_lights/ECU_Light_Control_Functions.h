// B 2,3,4 is North 
// B 5,6,7 is West
// E 0,1,2 is East
// E 3,4,5 is South
// Green, Orange and Red respectively

#ifndef __ECU_LIGHT_CONTROL_FUNCTIONS__
#define __ECU_LIGHT_CONTROL_FUNCTIONS__

#include "tm4c123gh6pm.h"

#define North 	(*((volatile unsigned long *)0x40005070)) // PB2, PB3, PB4
#define West		(*((volatile unsigned long *)0x40005380)) // PB5, PB6, PB7
#define East 		(*((volatile unsigned long *)0x4002401C)) // PE0, PE1, PE2
#define South 	(*((volatile unsigned long *)0x400240E0)) // PE3, PE4, PE5
	
typedef enum {GREEN, ORANGE, ORANGE_EXCEPT} mode;

void Lights_Init(void);
void North_Green_On(void);
void North_Orange_On(void);
void North_Red_On(void);
void North_Off(void);
void West_Green_On(void);
void West_Orange_On(void);
void West_Red_On(void);
void West_Off(void);
void East_Green_On(void);
void East_Orange_On(void);
void East_Red_On(void);
void East_Off(void);
void South_Green_On(void);
void South_Orange_On(void);
void South_Red_On(void);
void South_Off(void);

void Change_Lights(unsigned char direction, mode m);

#endif
