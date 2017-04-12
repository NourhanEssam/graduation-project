#include "GSM.h"

//------------GSM_Init------------
// Initialize the GSM Module to use UART0
// Input: none
// Output: none
void GSM_Init(void)
{
	UART1_Init();																										// Initialize UART1
	UART0_Init();

	ATCommand(1, "ATE0", "\r\nOK\r\n");									// Test GSM communication (Response: OK), turn echo off	
	ATCommand(1, "AT+CREG?", "\r\n+CREG: 0,1\r\nOK");		// Sim is ready and has connected to the network
	ATCommand(1, "AT+CREG=0", "\r\nOK\r\n");
	ATCommand(1, "AT+CGATT?", "\r\n+CGATT: 1\r\n"); 		// Check if SIM has internet access(Response: +CGATT:1)
}

//------------GSM_Start_Server------------
// Start TCP Server
// Input: none
// Output: none
void GSM_Start_Server(void)
{
	ATCommand(2, "AT+CIPSHUT\r\n", "\r\nSHUT OK\r\n");
	ATCommand(2, "AT+CIPMUX=0\r\n", "\r\nOK\r\n");
	ATCommand(2, "AT+CGATT=1", "\r\nOK\r\n");
	//ATCommand(2, "AT+CSTT=\"www\",\"\",\"\"", "\r\nOK\r\n");
	ATCommand(2, "AT+CSTT", "\r\nOK\r\n");
	ATCommand(2, "AT+CIICR", "\r\nOK\r\n");
	ATCommand(2, "AT+CIFSR", "\r\nOK\r\n");
	ATCommand(2, "AT+CIPSERVER=1,32000", "\r\nSERVER OK\r\n");
}

//------------GSM_Connect_To------------
// Start TCP Client Connection
// Input: The Server IP, and Port Number
// Output: none
void GSM_Connect_To(unsigned char Server_IP[], unsigned char Server_Port[])
{	
	ATCommand(2, "AT+CSTT", "\r\nOK\r\n");
	ATCommand(2, "AT+CIICR", "\r\nOK\r\n");
	ATCommand(2, "AT+CIFSR", "\r\n");
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
void GSM_Rcv(struct Buffer * b)
{
	UART1_InBuffer(b);
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
void ATCommand(int argc, ...)
{
	int i;
	va_list valist;
	va_start(valist, argc);
	for (i = 0; i < argc; i++) 
	{
		UART1_OutString(va_arg(valist, unsigned char *));
  }
	UART1_OutString("\r\n");
}

unsigned int string_compare(struct Buffer * b, unsigned char * s)
{
	int i = 0;
	unsigned char buffer[BUFFER_SIZE];
	Read_Buffer(b, buffer);
	while(buffer[i] == s[i])
	{
		if(buffer[i] == 0 && s[i] == 0)
		{
			return 1;
		}
		else if(buffer[i] == 0 || s[i] == 0)
		{
			return 0;
		}
		i++;
	}
	return 0;
}
