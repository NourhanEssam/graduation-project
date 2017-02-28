#include "GSM.h"

//------------GSM_Init------------
// Initialize the GSM Module to use UART0
// Input: none
// Output: none
void GSM_Init(void)
{
	UART_Init();													// Initialize UART0
	UART_OutString("\r\nAT\r\n"); 				// Test GSM communication (Response: OK)
	UART_OutString("\r\nAT+CREG?\r\n"); 	// Check if SIM is connected (Success Result: +CREG:1,1\r\nOK)
	UART_OutString("\r\nAT+CGATT?\r\n"); 	// Check if SIM has internet access(Response: +CGATT:1)
}

//------------GSM_Init------------
// Start TCP Client Connection
// Input: The Server IP, and Port Number
// Output: none
void GSM_Connect_To(unsigned char Server_IP[], unsigned char Server_Port[])
{
	UART_OutString("\r\nAT+CIPSTART='TCP',");	// TCP connection
	UART_OutString(Server_IP);								// Server IP
	UART_OutString(",");											
	UART_OutString(Server_Port);							// Server Port
	UART_OutString("\r\n"); 									// (Response: OK\r\nCONNECT OK)
}

// Send Data Using an Established TCP Connection
// Input: pointer to a NULL-terminated message string to be sent
// Output: none
void GSM_Send(unsigned char message[])
{
	UART_OutString("\r\nAT+CIPSEND\r\n");
	UART_OutString(message);
	UART_OutString("\r\n");
}

//------------GSM_Rcv------------
// Receive Data From an Established TCP Connection
// Input: none
// Output: pointer to a NULL-terminated message string 
/* TODO
unsigned char * GSM_Rcv(void)
{
}
*/

//------------GSM_Close_Connection------------
// Close The TCP Client Connection
// Input: none
// Output: none
void GSM_Close_Connection(void)
{
	UART_OutString("\r\nAT+CIPSHUT\r\n"); // (Response: SHUT OK\r\n);
}
