#include "ECU_Light_Control_Functions.h"
#include "Timers_Functions.h"
#include "GSM_Interfaces.h"
#include "PLL.h"
#include "UART.h"

#define INTERSECTION_ID 1
#define NORTH 'N'
#define SOUTH 'S'
#define EAST  'E'
#define WEST  'W'

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

#define GREEN 0
#define ORANGE 1
#define ORANGE_EXCEPT 2

// global variables
unsigned int S, NS;  // index to the current state 
unsigned char emergency_dir;
unsigned int Next_State, Saved_State;
unsigned int emergency = 0;
unsigned char id;

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
  unsigned long Next[5]; // 0 no emerg, 1 N emerg, 2 E emerg, 3 S emerg, 4 W emerg
};

typedef const struct State STyp;

STyp FSM[8]=
{
 {GREEN, NORTH, 3000, {waitN, ES3, ES1, ES1, ES1}}, 
 {ORANGE, NORTH, 500, {goE, 	goE, goE, goE, goE}},
 {GREEN, EAST, 3000, {waitE, ES1, ES3, ES1, ES1}},
 {ORANGE, EAST, 500, {goS, 	goS, goS, goS, goS}},
 {GREEN, SOUTH, 3000, {waitS, ES1, ES1, ES3, ES1}}, 
 {ORANGE, SOUTH, 500, {goW, 	goW, goW, goW, goW}},
 {GREEN, WEST, 3000, {waitW, ES1, ES1, ES1, ES3}},
 {ORANGE, WEST, 500, {goN, 	goN, goN, goN, goN}}
};

int main(void){
	Lights_Init();
	PLL_Init();
	SysTick_Init();
	UART1_Init();
	EnableInterrupts();
	UART1_Interrupt_Enable();
	
	timer2A_init(80000000);
	timer3A_init(80000000);
	
	NS = ES3;
	while(1)
	{
			S = NS;
			if(emergency)
			{
				EmergencyHandler();
			}
			else
			{
				Change_Lights(FSM[S].dir, FSM[S].m);
				timer2A_delayMs(FSM[S].Time);
				NS = FSM[S].Next[0];
			}
	}
}

void EmergencyHandler(void)
{
	switch(S)
	{
		case ES1:
			Change_Lights(FSM[Saved_State].dir, ORANGE);
			NS = ES2;
			timer2A_delayMs(5000);
			break;
		case ES2:
			Change_Lights(emergency_dir, GREEN);
			NS = ES2; // wait until a signal from Server is received
			timer2A_delayMs(3000);
			break;
		case ES3:
			Change_Lights(emergency_dir, ORANGE_EXCEPT);
			NS = ES4;
			timer2A_delayMs(5000);
			break;
		case ES4:
			Change_Lights(emergency_dir, GREEN);
			NS = ES4; // wait until a signal from Server is received
			timer2A_delayMs(3000);
			break;
	}
}

// UART1 interrupt handler
void UART1_Handler(void)
{
	UART1_ICR_R |= 0x00000010;
	emergency_dir = UART1_InCharNonBlocking();
	id = UART1_InCharNonBlocking();
	if(id == INTERSECTION_ID && (emergency_dir == NORTH || emergency_dir == SOUTH || emergency_dir == EAST || emergency_dir == WEST))
	{
		// change state to an emergency state
	}
}
