#include "ECU_Light_Control_Functions.h"
#include "Timers_Functions.h"
#include "GSM_Interfaces.h"
#include "PLL.h"

#define ES0 0 // same dir? No -> ES1, Yes -> ES4
#define ES1 1 // orange 5 seconds & turn off counter -> ES2
#define ES2 2 // open direction - wait for car -> ES3
#define ES3 3 // back to original state
#define ES4 4 // orange 5 seconds in all directions except emergency direction - > ES5
#define ES5 5 // turn off counter - wait for car -> ES6
#define ES6 6 // State = Next
#define idle 7 // waiting state

void EmergencyHandler(void);

unsigned char emergency_dir, lights_dir;
unsigned int Current_State, Next_State, Saved_State;

int main(void){
	Lights_Init();
	PLL_Init();
	init_gsm_control();
	timer2A_init(80000000);
	timer3A_init(80000000);
	
	Next_State = ES0;
	while(1)
	{
		/*
		// some debugging code
		North_Green_On();
		North_Orange_On();
		North_Red_On();
		North_Off();
		West_Green_On();
		West_Orange_On();
		West_Red_On();
		West_Off();
		East_Green_On();
		East_Orange_On();
		East_Red_On();
		East_Off();
		South_Green_On();
		South_Orange_On();
		South_Red_On();
		South_Off();
		*/
		EmergencyHandler();
	}
}

void EmergencyHandler()
{
	Current_State = Next_State;
	switch(Current_State)
	{
		case ES0:
			if(emergency_dir == lights_dir)
			{
				Next_State = ES4;
			}
			else
			{
				Next_State = ES1;
			}
			break;
		case ES1:
			Orange_Direction(lights_dir);
			Next_State = ES2;
			// pause Lights counters
			timer2A_delayMs(5000);
			break;
		case ES2:
			Green_Direction(emergency_dir);
			Next_State = idle; // wait until a signal from Server is received
			break;
		case ES3:
			Next_State = Saved_State; // return to normal flow (before emergency)
			timer3A_resume();
			break;
		case ES4:
			Orange_Except(emergency_dir);
			Next_State = ES5;
			// pause Lights counters
			timer2A_delayMs(5000);
			break;
		case ES5:
			Green_Direction(emergency_dir);
			Next_State = idle; // wait until a signal from Server is received
			break;
		case ES6:
			Next_State = Saved_State; // return to normal flow
			break;
		case idle:
			timer2A_delayMs(1000); // when the vehical interrupt arrives it should change the next state
			break;
	}
}
