#ifndef __UART__
#define __UART__

#include "tm4c123gh6pm.h"

//------------UART1---------------------

//------------UART_Init------------
// Initialize the UART for 115200 baud rate (assuming 80 MHz UART clock),
// 8 bit word length, no parity bits, one stop bit, FIFOs enabled
// Input: none
// Output: none
void UART1_Init(void);

//------------UART1_InChar------------
// Wait for new serial port input
// Input: none
// Output: ASCII code for key typed
unsigned char UART1_InChar(void);

//------------UART1_InCharNonBlocking------------
// Immediately return input or 0 if no input
// Input: none
// Output: ASCII code for key typed
unsigned char UART1_InCharNonBlocking(void);

//------------UART1_OutChar------------
// Wait for buffer to be not full, then output
// Output 8-bit to serial port
// Input: letter is an 8-bit ASCII character to be transferred
// Output: none
void UART1_OutChar(unsigned char data);

//------------UART1_OutString------------
// Output String (NULL termination)
// Input: pointer to a NULL-terminated string to be transferred
// Output: none
void UART1_OutString(unsigned char buffer[]);

//------------UART1_InString------------
// Read String (NULL termination)
// Input: pointer to a NULL-terminated string, buffer size
// Output: none
void UART1_InString(unsigned char * buffer, unsigned int size);

//------------UART1_Interupt_Enable------------
// Enable UART1 Rx Interrupt
// Input: none
// Output: none
void UART1_Interrupt_Enable(void);

//------------UART1_Interrupt_Disable------------
// Disable UART1 Rx Interrupt
// Input: none
// Output: none
void UART1_Interrupt_Disable(void);

#endif
