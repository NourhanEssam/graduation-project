#include "tm4c123gh6pm.h"

//------------UART_Init------------
// Initialize the UART for 115200 baud rate (assuming 80 MHz UART clock),
// 8 bit word length, no parity bits, one stop bit, FIFOs enabled
// Input: none
// Output: none
void UART_Init(void);

//------------UART_InChar------------
// Wait for new serial port input
// Input: none
// Output: ASCII code for key typed
unsigned char UART_InChar(void);

//------------UART_InCharNonBlocking------------
// Immediately return input or 0 if no input
// Input: none
// Output: ASCII code for key typed
unsigned char UART_InCharNonBlocking(void);

//------------UART_OutChar------------
// Wait for buffer to be not full, then output
// Output 8-bit to serial port
// Input: letter is an 8-bit ASCII character to be transferred
// Output: none
void UART_OutChar(unsigned char data);

//------------UART_OutString------------
// Output String (NULL termination)
// Input: pointer to a NULL-terminated string to be transferred
// Output: none
void UART_OutString(unsigned char buffer[]);

//------------UART_InString------------
// Read String (NULL termination)
// Input: none
// Output: pointer to a NULL-terminated string
unsigned char * UART_InString(void);
