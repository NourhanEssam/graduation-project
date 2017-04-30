// B 2,3,4 is North 
// B 5,6,7 is West
// E 0,1,2 is East
// E 3,4,5 is South
// Green, Orange and Red respectively

#include "tm4c123gh6pm.h"

#define North_Green 	(*((volatile unsigned long *)0x40005010)) // PB2
#define North_Orange 	(*((volatile unsigned long *)0x40005020)) // PB3
#define North_Red 		(*((volatile unsigned long *)0x40005040)) // PB4
#define West_Green 		(*((volatile unsigned long *)0x40005080)) // PB5
#define West_Orange 	(*((volatile unsigned long *)0x40005100)) // PB6
#define West_Red 			(*((volatile unsigned long *)0x40005200)) // PB7
#define East_Green 		(*((volatile unsigned long *)0x40024004)) // PE0
#define East_Orange 	(*((volatile unsigned long *)0x40024008)) // PE1
#define East_Red 			(*((volatile unsigned long *)0x40024010)) // PE2
#define South_Green 	(*((volatile unsigned long *)0x40024020)) // PE3
#define South_Orange 	(*((volatile unsigned long *)0x40024040)) // PE4
#define South_Red 		(*((volatile unsigned long *)0x40024080)) // PE5

void Lights_Init(void);
void North_Green_On(void);
void North_Green_Off(void);
void North_Orange_On(void);
void North_Orange_Off(void);
void North_Red_On(void);
void North_Red_Off(void);
void West_Green_On(void);
void West_Green_Off(void);
void West_Orange_On(void);
void West_Orange_Off(void);
void West_Red_On(void);
void West_Red_Off(void);
void East_Green_On(void);
void East_Green_Off(void);
void East_Orange_On(void);
void East_Orange_Off(void);
void East_Red_On(void);
void East_Red_Off(void);
void South_Green_On(void);
void South_Green_Off(void);
void South_Orange_On(void);
void South_Orange_Off(void);
void South_Red_On(void);
void South_Red_Off(void);
