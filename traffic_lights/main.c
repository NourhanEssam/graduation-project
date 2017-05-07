#include "ECU_Light_Control_Functions.h"
#include "Timers_Functions.h"
#include "GSM_Interfaces.h"
#include "PLL.h"

#define goN   0
#define waitN 1
#define goE   2
#define waitE 3
#define goS   4
#define waitS 5
#define goW   6
#define waitW 7
#define EN1 	8  // orange 5 seconds & turn off counter -> EN2
#define EN2 	9 // open direction - wait for car
#define EN3 	10 // orange 5 seconds in all directions except emergency direction - > EN4
#define EN4 	11 // turn off counter - wait for car 
#define EE1 	12  // orange 5 seconds & turn off counter -> EE2
#define EE2 	13 // open direction - wait for car
#define EE3 	14 // orange 5 seconds in all directions except emergency direction - > EE4
#define EE4 	15 // turn off counter - wait for car
#define ES1 	16  // orange 5 seconds & turn off counter -> ES2
#define ES2 	17 // open direction - wait for car
#define ES3 	18 // orange 5 seconds in all directions except emergency direction - > ES4
#define ES4 	19 // turn off counter - wait for car 
#define EW1 	20  // orange 5 seconds & turn off counter -> EW2
#define EW2 	21 // open direction - wait for car
#define EW3 	22 // orange 5 seconds in all directions except emergency direction - > EW4
#define EW4 	23 // turn off counter - wait for car 

#define GREEN 0
#define ORANGE 1
#define ORANGE_EXCEPT 2

void EmergencyHandler(void);

// Linked data structure
struct State {
  mode m; 
	unsigned char dir;
  unsigned long Time;  
  unsigned long Next[5]; // 0 no emerg, 1 N emerg, 2 E emerg, 3 S emerg, 4 W emerg
};

typedef const struct State STyp;

unsigned int S, NS;  // index to the current state 

unsigned char emergency_dir = 'N';
unsigned int Next_State, Saved_State = goW;
unsigned int emergency = 1;

STyp FSM[8]=
{
 {GREEN, 'N', 3000, {waitN, ES3, ES1, ES1, ES1}}, 
 {ORANGE, 'N', 500, {goE, 	goE, goE, goE, goE}},
 {GREEN, 'E', 3000, {waitE, ES1, ES3, ES1, ES1}},
 {ORANGE, 'E', 500, {goS, 	goS, goS, goS, goS}},
 {GREEN, 'S', 3000, {waitS, ES1, ES1, ES3, ES1}}, 
 {ORANGE, 'S', 500, {goW, 	goW, goW, goW, goW}},
 {GREEN, 'W', 3000, {waitW, ES1, ES1, ES1, ES3}},
 {ORANGE, 'W', 500, {goN, 	goN, goN, goN, goN}}
};

int main(void){
	Lights_Init();
	PLL_Init();
	init_gsm_control();
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

void EmergencyHandler()
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
