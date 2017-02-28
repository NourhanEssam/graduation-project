#include "UART.h"

//------------GSM_Init------------
// Initialize the GSM Module to use UART0
// Input: none
// Output: none
void GSM_Init(void);

//------------GSM_Connect_To------------
// Start TCP Client Connection
// Input: The Server IP, and Port Number
// Output: none
void GSM_Connect_To(unsigned char Server_IP[], unsigned char Server_Port[]);

//------------GSM_Send------------
// Send Data Using an Established TCP Connection
// Input: pointer to a NULL-terminated message string to be sent
// Output: none
void GSM_Send(unsigned char message[]);

//------------GSM_Rcv------------
// Receive Data From an Established TCP Connection
// Input: none
// Output: pointer to a NULL-terminated message string 
unsigned char * GSM_Rcv(void);

//------------GSM_Close_Connection------------
// Close The TCP Client Connection
// Input: none
// Output: none
void GSM_Close_Connection(void);
