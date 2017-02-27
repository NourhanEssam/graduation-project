#include "UART.h"

//------------GSM_Init------------
// Initialize the GSM Module to use UART0
// Input: none
// Output: none
void GSM_Init(void);

//------------GSM_Init------------
// Start TCP Client Connection
// Input: The Server IP, and Port Number
// Output: none
void GSM_Connect_To(unsigned char Server_IP[], unsigned char Server_Port[]);