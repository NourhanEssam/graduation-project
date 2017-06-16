#include "ECU_Light_Control_Functions.h"
#include "Timers_Functions.h"
#include "GSM_Interfaces.h"
#include "PLL.h"
#include "UART.h"

#define INTERSECTION_ID '1'
#define NORTH 'N'
#define SOUTH 'S'
#define EAST  'E'
#define WEST  'W'
#define END		'P'

#define goN   0
#define waitN 1
#define goE   2
#define waitE 3
#define goS   4
#define waitS 5
#define goW   6
#define waitW 7
#define ES1 	8  // orange 5 seconds & turn off counter -> ES2
#define ES2 	9 // open direction - wait for car
#define ES3 	10 // orange 5 seconds in all directions except emergency direction - > ES4
#define ES4 	11 // turn off counter - wait for car
#define FINISH 	12


// global variables
unsigned int S, NS;  					// index to the current state 
unsigned char emergency_dir, input;	// emergency direction
unsigned int ES, NES; 				// emergency states
unsigned int emergency = 0;		// emergency flag
unsigned char id;							// TL id

extern unsigned int time; 		// global variable from Timers_Functions.c

// basic functions defined at end of startup.s
void DisableInterrupts(void); // Disable interrupts
void EnableInterrupts(void);  // Enable interrupts
void WaitForInterrupt(void);  // low power mode

// UART1 interrupt handler
void UART1_Handler(void);

// Emergency FSM
void EmergencyHandler(void);

// Linked data structure
struct State {
  mode m; 
	unsigned char dir;
  unsigned long Time;  
  unsigned long Next; // no emergency
};

typedef const struct State STyp;

STyp FSM[8]=
{
 {GREEN, NORTH, 10000, waitN}, 
 {ORANGE, NORTH, 1000, goE},
 {GREEN, EAST, 10000, waitE},
 {ORANGE, EAST, 1000, goS},
 {GREEN, SOUTH, 10000, waitS}, 
 {ORANGE, SOUTH, 1000, goW,},
 {GREEN, WEST, 10000, waitW},
 {ORANGE, WEST, 1000, goN}
};

int main(void){
	Lights_Init();
	PLL_Init();
	SysTick_Init();
	UART1_Init();
	EnableInterrupts();
	UART1_Interrupt_Enable();
	
	timer2A_init(80000000);
	
	NS = goN;
	while(1)
	{
			if(emergency || NES == FINISH)
			{
				EmergencyHandler();
			}
			else
			{
				S = NS;
				Change_Lights(FSM[S].dir, FSM[S].m);
				timer2A_delayMs(FSM[S].Time);
				if(emergency != 1)
				{
					NS = FSM[S].Next;
				}
			}
	}
}

void EmergencyHandler(void)
{
	ES = NES;
	switch(ES)
	{
		case ES1:
			Change_Lights(FSM[S].dir, ORANGE);
			NES = ES2;
			timer2A_delayMs(1000);
			break;
		case ES2:
			Change_Lights(emergency_dir, GREEN);
			NES = ES2; // wait until a signal from Server is received
			timer2A_delayMs(3000);
			break;
		case ES3:
			Change_Lights(emergency_dir, ORANGE_EXCEPT);
			NES = ES4;
			NS = FSM[S].Next;
			timer2A_delayMs(1000);
			break;
		case ES4:
			Change_Lights(emergency_dir, GREEN);
			NES = ES4; // wait until a signal from Server is received
			timer2A_delayMs(3000);
			break;
		case FINISH:
			Change_Lights(emergency_dir, ORANGE);
			NES = ES1;
			timer2A_delayMs(1000);
			break;
	}
}

// UART1 interrupt handler
void UART1_Handler(void)
{
	UART1_ICR_R |= 0x00000010;
	input = UART1_InCharNonBlocking();
	id = UART1_InCharNonBlocking();
	if(id == INTERSECTION_ID)
	{
		time = 0;
		if(input == NORTH || input == SOUTH || input == EAST || input == WEST)
		{
			emergency_dir = input;
			emergency = 1;
			if(S == waitN || S == waitS || S == waitE || S == waitW) // if state is orange
			{
				S--;
				NS--;
			}
			if(emergency_dir == FSM[S].dir)
			{
				if(FSM[S].m == ORANGE)
				{
					NS = FSM[S].Next;
				}
				NES = ES3;
			}
			else
			{
				NES = ES1;
			}
		}
		else if(input == END)
		{
			if(NES == ES2)
			{
				NES = FINISH;
			}
			emergency = 0;
		}
	}
}
