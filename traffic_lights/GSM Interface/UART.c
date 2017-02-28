#include "UART.h"


//------------UART_Init------------
// Initialize the UART for 115200 baud rate (assuming 80 MHz UART clock),
// 8 bit word length, no parity bits, one stop bit, FIFOs enabled
// Input: none
// Output: none
void UART_Init(void)
{
	SYSCTL_RCGC1_R |= SYSCTL_RCGC1_UART0; // Activate UART0
	SYSCTL_RCGC2_R |= SYSCTL_RCGC2_GPIOA; // Activate Port A
	
	UART0_CTL_R &= ~UART_CTL_UARTEN;      // Disable UART
	
	// Baud16/16 = (Bus clock frequency)/(16*divider) where divider is the desired baud rate
	// 80,000,000/(16*115200) = 43.40277778
	// m = int(Baud16/16) = 43
	// n = round(rem(Baud16/16) * 64) = round(0.40277778*64) = 26
	UART0_IBRD_R = 43; 									// IBRD = m
	UART0_FBRD_R = 26;										// FBRD = n
	UART0_LCRH_R = (UART_LCRH_WLEN_8 | UART_LCRH_FEN); // Enable 8 bits frames, and FIFO buffers
	
	UART0_CTL_R |= UART_CTL_UARTEN;				// Enable UART
	
	// Port A initialization for UART0
	GPIO_PORTA_AFSEL_R |= 0x03; 					// Enable Alternative Functions on Port A pins A0, A1
	GPIO_PORTA_DEN_R |= 0x03;							// Enable Digital I/O on Port A pins A0, A1
	GPIO_PORTA_PCTL_R &= 0xFFFFFF00;
	GPIO_PORTA_PCTL_R |= 0x00000011;			// Enable UART0 Rx, Tx on pins A0, A1	
	GPIO_PORTA_AMSEL_R &= ~0x03;					// Disable analog functionality on pins A0, A1
}

//------------UART_InChar------------
// Wait for new serial port input
// Input: none
// Output: ASCII code for key typed
unsigned char UART_InChar(void)
{
  while((UART0_FR_R&UART_FR_RXFE) != 0);
  return((unsigned char)(UART0_DR_R&0xFF));
}

//------------UART_OutChar------------
// Wait for buffer to be not full, then output
// Output 8-bit to serial port
// Input: letter is an 8-bit ASCII character to be transferred
// Output: none
void UART_OutChar(unsigned char data)
{
  while((UART0_FR_R&UART_FR_TXFF) != 0);
	UART0_DR_R = data;
}

//------------UART_OutString------------
// Output String (NULL termination)
// Input: pointer to a NULL-terminated string to be transferred
// Output: none
void UART_OutString(unsigned char buffer[])
{
	int i = 0;
	while(buffer[i] != 0)
	{
		UART_OutChar(buffer[i]);
		i++;
	}
}

//------------UART_InString------------
// Read String (NULL termination)
// Input: none
// Output: pointer to a NULL-terminated string
/* TODO
unsigned char * UART_InString(void)
{
	int size = BufferSize;
	unsigned char buffer[size];
	int i = 0;
	while((buffer[i] = UART_InChar()) != 0)
	{
		i++;
	}
	return buffer;
}
*/
