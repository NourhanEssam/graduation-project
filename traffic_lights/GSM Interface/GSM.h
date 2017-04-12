#include <stdarg.h>
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

//------------GSM_Start_Server------------
// Start TCP Server
// Input: none
// Output: none
void GSM_Start_Server(void);

//------------GSM_Send------------
// Send Data Using an Established TCP Connection
// Input: pointer to a NULL-terminated message string to be sent
// Output: none
void GSM_Send(unsigned char message[]);

//------------GSM_Rcv------------
// Receive Data From an Established TCP Connection
// Input: buffer size, buffer to save the received NULL-terminated string  
// Output: none
void GSM_Rcv(struct Buffer * b);

//------------GSM_Close_Connection------------
// Close The TCP Client Connection
// Input: none
// Output: none
void GSM_Close_Connection(void);

//------------ATCommand------------
// Send AT Command to the GSM module and check the response
// Input: NULL-terminated command strings, response in case of success
// Output: 0 in case of success, 1 otherwise
void ATCommand(int argc, ...);

unsigned int string_compare(struct Buffer * b, unsigned char * s);
