#include "PLL.h"
#include "GSM.h"

#define GSM_S0 0		// test communication
#define GSM_S1 1		// check sim connection
#define GSM_S2 2		// check internet access
#define GSM_S3 3		// disable multiple connections
#define GSM_S4 4		// CGATT=1
#define GSM_S5 5		// CSTT
#define GSM_S6 6		// CIICR
#define GSM_S7 7		// get local ip
#define GSM_S8 8		// server connection
#define GSM_S9 9		// idle
#define GSM_S10 10 	// shut down
#define GSM_S11 11 	// initiate send message
#define GSM_S12 12 	// send message
#define GSM_INIT 13 

// global variables
struct Buffer buffer_rcv;

unsigned int Current_State, Next_State;
unsigned char Server_IP[16] = "\"itls.dynu.net\"";
unsigned char Server_Port[8] = "\"31001\"";

// basic functions defined at end of startup.s
void DisableInterrupts(void); // Disable interrupts
void EnableInterrupts(void);  // Enable interrupts
void WaitForInterrupt(void);  // low power mode

void GSM_FSM(void);

// UART1 interrupt handler
void UART1_Handler(void)
{
	UART1_ICR_R |= 0x00000010;
	GSM_Rcv(&buffer_rcv);
	GSM_FSM();
}

int main(void)
{
	Next_State = GSM_INIT;
	PLL_Init();
	SysTick_Init();
	//UART0_Init();
	UART1_Init();
	EnableInterrupts();
	UART1_Interrupt_Enable();
	GSM_FSM();
	while(1)
	{
		//GSM_Connect_To("\"41.233.31.195\"", "\"31001\"");
		//SysTick_Wait10ms(100);
		//GSM_Send("GET / HTTP/1.1\r\n\r\n");
		//SysTick_Wait10ms(1000);
		//GSM_Rcv(buffer, 100);
		//GSM_Close_Connection();
		SysTick_Wait10ms(50);
		//GSM_FSM();
	}
}

//--------------GSM_FSM--------------
void GSM_FSM(void)
{
	Current_State = Next_State;
	switch(Current_State)
	{
		case GSM_INIT:
			ATCommand(1, "ATE0");	// Test Connection and Turn off echo back
			Next_State = GSM_S0;
			break;
		case GSM_S0:
			ATCommand(1, "ATE0");	// Test Connection and Turn off echo back
			Next_State = GSM_S1;
			break;
		case GSM_S1:
			if(string_compare(&buffer_rcv, "\r\nOK\r\n"))
			{
				ATCommand(1, "AT+CREG?"); // Sim is ready and has connected to the network
				Next_State = GSM_S2;
			}
			else
			{
				Next_State = GSM_S0;
			}
			break;
		case GSM_S2:
			if(string_compare(&buffer_rcv, "\r\n+CREG: 0,1\r\n\r\n"))
			{
				ATCommand(1, "AT+CGATT?"); // Check if SIM has internet access
				Next_State = GSM_S3;
			}
			else
			{
				Next_State = GSM_S0;
			}
			break;
		case GSM_S3:			
			if(string_compare(&buffer_rcv, "\r\n+CGATT: 1\r\n\r\nO"))
			{
				ATCommand(1, "AT+CIPMUX=0");
				Next_State = GSM_S4;
			}
			else
			{
				Next_State = GSM_S0;
			}
			break;
		case GSM_S4:			
			if(string_compare(&buffer_rcv, "\r\nOK\r\n"))
			{
				ATCommand(1, "AT+CGATT=1");
				Next_State = GSM_S5;
			}
			else
			{
				ATCommand(1, "ATE0");
				Next_State = GSM_S0;
			}
			break;
		case GSM_S5:			
			if(string_compare(&buffer_rcv, "\r\nOK\r\n"))
			{
				ATCommand(1, "AT+CSTT");
				Next_State = GSM_S6;
			}
			else
			{
				Next_State = GSM_S0;
			}
			break;
		case GSM_S6:			
			if(string_compare(&buffer_rcv, "\r\nOK\r\n"))
			{
				ATCommand(1, "AT+CIICR");
				Next_State = GSM_S7;
			}
			else
			{
				Next_State = GSM_S5;
			}
			break;
		case GSM_S7:			
			if(string_compare(&buffer_rcv, "\r\nOK\r\n"))
			{
				ATCommand(1, "AT+CIFSR");
				Next_State = GSM_S8;
			}
			else
			{
				Next_State = GSM_S5;
			}
			break;
		case GSM_S8:			
			if(string_compare(&buffer_rcv, "Error"))
			{
				Next_State = GSM_S0;
			}
			else
			{
				ATCommand(4, "AT+CIPSTART=\"TCP\",", Server_IP, ",", Server_Port);
				Next_State = GSM_S11;
			}
			break;
		case GSM_S9:
			
			break;
		case GSM_S10:
			ATCommand(1, "AT+CIPSHUT");
			Next_State = GSM_S5;
			break;
		case GSM_S11:
			if(string_compare(&buffer_rcv, "\r\nOK\r\n\r\nCONNECT "))
			{
				ATCommand(1, "AT+CIPSEND");
			}
			Next_State = GSM_S12;
			break;
		case GSM_S12:
			if(string_compare(&buffer_rcv, "\r\n> "))
			{
				UART1_OutString("GET / HTTP/1.1\r\n\r\n");
				UART1_OutChar(0x1A);
				Next_State = GSM_S9;
			}
			else
			{
				Next_State = GSM_S11;
			}
			break;
	}
}
