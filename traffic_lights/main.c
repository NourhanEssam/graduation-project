#include "ECU_Light_Control_Functions.h"

#define ES0 0 // same dir? No -> ES1, Yes -> ES4
#define ES1 1 // orange 5 seconds & turn off counter -> ES2
#define ES2 2 // open direction - wait for car -> ES3
#define ES3 3 // back to original state
#define ES4 4 // orange 5 seconds in all directions except emergency direction - > ES5
#define ES5 5 // turn off counter - wait for car -> ES6
#define ES6 6 // State = Next

void EmergencyHandler(void);

unsigned char emergency_dir, lights_dir;
unsigned int Current_EState, Next_EState;

int main(void){
	Lights_Init();
	Next_EState = ES0;
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
	}
}

void EmergencyHandler()
{
	Current_EState = Next_EState;
	switch(Current_EState)
	{
		case ES0:
			if(emergency_dir == lights_dir)
			{
				Next_EState = ES4;
			}
			else
			{
				Next_EState = ES1;
			}
			// call the FSM again
			break;
		case ES1:
			Orange_Direction(lights_dir);
			Next_EState = ES2;
			// pause Lights counters
			// run 5 seconds timer
			break;
		case ES2:
			Green_Direction(emergency_dir);
			Next_EState = ES3;
			// wait until a signal from Server is received
			break;
		case ES3:
			Next_EState = ES0;
			// resume Lights counters
			break;
		case ES4:
			Orange_Except(emergency_dir);
			Next_EState = ES5;
			// pause Lights counters
			// run 5 seconds timer
			break;
		case ES5:
			Green_Direction(emergency_dir);
			Next_EState = ES3;
			// wait until a signal from Server is received
			break;
		case ES6:
			Next_EState = ES0;
			// reset counters and call Lights FSM
			break;
	}
}
