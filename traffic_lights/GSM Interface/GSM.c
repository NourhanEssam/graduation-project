#include "GSM.h"

//------------GSM_Init------------
// Initialize the GSM Module to use UART0
// Input: none
// Output: none
void GSM_Init(void)
{
	int check = 0;
	UART1_Init();																				// Initialize UART1
	UART0_Init();

	check = ATCommand("ATE0\r\n", "\r\nOK\r\n");								// Test GSM communication (Response: OK), turn echo off	
	check = ATCommand("AT+CREG?\r\n", "\r\n+CREG: 1,1\r\nOK");	// Sim is ready and has connected to the network
	check = ATCommand("AT+CGATT?\r\n", "\r\n+CGATT: 1\r\n"); 		// Check if SIM has internet access(Response: +CGATT:1)
}

//------------GSM_Init------------
// Start TCP Client Connection
// Input: The Server IP, and Port Number
// Output: none
void GSM_Connect_To(unsigned char Server_IP[], unsigned char Server_Port[])
{	
	unsigned char buffer[46];
	string_concatination("AT+CIPSTART=\"TCP\",", Server_IP, ",", Server_Port, "\r\n", buffer);
	ATCommand(buffer, "\r\nOK\r\nCONNECT OK\r\n"); // (Response: OK\r\nCONNECT OK)
}

// Send Data Using an Established TCP Connection
// Input: pointer to a NULL-terminated message string to be sent
// Output: none
void GSM_Send(unsigned char message[])
{
	ATCommand("AT+CIPSEND\r\n", "\r\n>\r\n");
	UART1_OutString(message);
	UART1_OutString("\r\n\r\n");
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
	ATCommand("AT+CIPSHUT\r\n", "\r\nSHUT OK\r\n");
}

//------------ATCommand------------
// Send AT Command to the GSM module and check the response
// Input: NULL-terminated command string, response in case of success
// Output: 0 in case of success, 1 otherwise
unsigned int ATCommand(unsigned char * command, unsigned char * successResponse)
{
	unsigned char response[30];
	UART1_OutString(command);
	UART0_OutString(command);
	SysTick_Wait10ms(200);
	UART1_InString(response, 30);
	
	if(string_compare(response, successResponse))
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

void string_concatination(unsigned char * s1, unsigned char * s2, unsigned char * s3, unsigned char * s4, unsigned char * s5, unsigned char * s6)
{
	int i = 0;
	int size1, size2, size3, size4;
	while(s1[i] != 0)
	{
		s6[i] = s1[i];
		i++;
	}
	size1 = i;
	i = 0;
	while(s2[i] != 0)
	{
		s6[i+size1] = s2[i];
		i++;
	}
	size2 = i + size1;
	i = 0;
	while(s3[i] != 0)
	{
		s6[i+size2] = s3[i];
		i++;
	}
	size3 = i + size2;
	i = 0;
	while(s4[i] != 0)
	{
		s6[i+size3] = s4[i];
		i++;
	}
	size4 = i + size3;
	i = 0;
	while(s5[i] != 0)
	{
		s6[i+size4] = s5[i];
		i++;
	}
	s6[i+size4] = 0;
}
