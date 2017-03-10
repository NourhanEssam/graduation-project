#include "GSM.h"

//------------GSM_Init------------
// Initialize the GSM Module to use UART0
// Input: none
// Output: none
void GSM_Init(void)
{
	int check = 0;
	UART1_Init();																										// Initialize UART1
	UART0_Init();

	check = ATCommand(2, "ATE0", "\r\nOK\r\n");									// Test GSM communication (Response: OK), turn echo off	
	check = ATCommand(2, "AT+CREG?", "\r\n+CREG: 1,1\r\nOK");		// Sim is ready and has connected to the network
	check = ATCommand(2, "AT+CREG=0", "\r\nOK\r\n");
	check = ATCommand(2, "AT+CGATT?", "\r\n+CGATT: 1\r\n"); 		// Check if SIM has internet access(Response: +CGATT:1)
	check = ATCommand(2, "AT+CGATT=1", "\r\nOK\r\n");
}

//------------GSM_Init------------
// Start TCP Client Connection
// Input: The Server IP, and Port Number
// Output: none
void GSM_Connect_To(unsigned char Server_IP[], unsigned char Server_Port[])
{	
	ATCommand(2, "AT+CIPMUX=0", "\r\nOK\r\n");				// disable multiple connections
	ATCommand(2, "AT+CIPSTATUS", "\r\nOK\r\n");				// get connection status
	ATCommand(5, "AT+CIPSTART=\"TCP\",", Server_IP, ",", Server_Port, "\r\nOK\r\nCONNECT\r\n"); // (Response: OK\r\nCONNECT)
}

// Send Data Using an Established TCP Connection
// Input: pointer to a NULL-terminated message string to be sent
// Output: none
void GSM_Send(unsigned char message[])
{
	ATCommand(2, "AT+CIPSEND\r\n", "\r\n>\r\n");
	UART1_OutString(message);
	UART1_OutChar(0x1A);
}

//------------GSM_Rcv------------
// Receive Data From an Established TCP Connection
// Input: buffer size, buffer to save the received NULL-terminated string  
// Output: none
void GSM_Rcv(unsigned char * buffer, unsigned int BufferSize)
{
	UART1_InString(buffer, BufferSize);
}


//------------GSM_Close_Connection------------
// Close The TCP Client Connection
// Input: none
// Output: none
void GSM_Close_Connection(void)
{
	ATCommand(2, "AT+CIPSHUT\r\n", "\r\nSHUT OK\r\n");
}

//------------ATCommand------------
// Send AT Command to the GSM module and check the response
// Input: NULL-terminated command strings, response in case of success
// Output: 0 in case of success, 1 otherwise
unsigned int ATCommand(int argc, ...)
{
	
	int i;
	va_list valist;
	unsigned char response[30];
	va_start(valist, argc);
	for (i = 0; i < argc - 1; i++) 
	{
		UART1_OutString(va_arg(valist, unsigned char *));
  }
	UART1_OutString("\r\n");
	SysTick_Wait10ms(200);
	UART1_InString(response, 30);
	
	if(string_compare(response, va_arg(valist, unsigned char *)))
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

unsigned int string_compare(unsigned char * s1, unsigned char * s2)
{
	int i = 0;
	while(s1[i] == s2[i])
	{
		if(s1[i] == 0 && s2[i] == 0)
		{
			return 1;
		}
		else if(s1[i] == 0 || s2[i] == 0)
		{
			return 0;
		}
		i++;
	}
	return 0;
}
