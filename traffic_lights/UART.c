#include "UART.h"

//------------UART1---------------------

//------------UART1_Init------------
// Initialize the UART for 115200 baud rate (assuming 80 MHz UART clock),
// 8 bit word length, no parity bits, one stop bit, FIFOs enabled
// Input: none
// Output: none
void UART1_Init(void)
{
	SYSCTL_RCGC1_R |= SYSCTL_RCGC1_UART1; // Activate UART1
	SYSCTL_RCGC2_R |= SYSCTL_RCGC2_GPIOB; // Activate Port B
	
	UART1_CTL_R &= ~UART_CTL_UARTEN;      // Disable UART
	
	UART1_IFLS_R &= ~0x00000038;
	// Baud16/16 = (Bus clock frequency)/(16*divider) where divider is the desired baud rate
	// 80,000,000/(16*115200) = 43.40277778
	// m = int(Baud16/16) = 43
	// n = round(rem(Baud16/16) * 64) = round(0.40277778*64) = 26
	UART1_IBRD_R = 43; 									// IBRD = m
	UART1_FBRD_R = 26;										// FBRD = n
	UART1_LCRH_R = (UART_LCRH_WLEN_8 | UART_LCRH_FEN); // Enable 8 bits frames, and FIFO buffers
	
	UART1_CTL_R |= UART_CTL_UARTEN;				// Enable UART
	
	// Port A initialization for UART0
	GPIO_PORTB_AFSEL_R |= 0x03; 					// Enable Alternative Functions on Port B pins B0, B1
	GPIO_PORTB_DEN_R |= 0x03;							// Enable Digital I/O on Port B pins B0, B1
	GPIO_PORTB_PCTL_R &= 0xFFFFFF00;
	GPIO_PORTB_PCTL_R |= 0x00000011;			// Enable UART0 Rx, Tx on pins B0, B1	
	GPIO_PORTB_AMSEL_R &= ~0x03;					// Disable analog functionality on pins B0, B1
	
	NVIC_EN0_R |= 0x00400000;
}

//------------UART1_InChar------------
// Wait for new serial port input
// Input: none
// Output: ASCII code for key typed
unsigned char UART1_InChar(void)
{
  while((UART1_FR_R&UART_FR_RXFE) != 0);
  return((unsigned char)(UART1_DR_R&0xFF));
}

//------------UART1_InCharNonBlocking------------
// Immediately return input or 0 if no input
// Input: none
// Output: ASCII code for key typed
unsigned char UART1_InCharNonBlocking(void){
  if((UART1_FR_R&UART_FR_RXFE) == 0){
    return((unsigned char)(UART1_DR_R&0xFF));
  } else{
    return 0;
  }
}

//------------UART1_OutChar------------
// Wait for buffer to be not full, then output
// Output 8-bit to serial port
// Input: letter is an 8-bit ASCII character to be transferred
// Output: none
void UART1_OutChar(unsigned char data)
{
  while((UART1_FR_R&UART_FR_TXFF) != 0);
	UART1_DR_R = data;
}

//------------UART1_OutString------------
// Output String (NULL termination)
// Input: pointer to a NULL-terminated string to be transferred
// Output: none
void UART1_OutString(unsigned char buffer[])
{
	int i = 0;
	while(buffer[i] != 0)
	{
		UART1_OutChar(buffer[i]);
		i++;
	}
}

//------------UART1_InString------------
// Read String (NULL termination)
// Input: pointer to a NULL-terminated string, buffer size
// Output: none
void UART1_InString(unsigned char * buffer, unsigned int size)
{
	unsigned int i = 0;
	while(i < size)
	{
		if((buffer[i] = UART1_InCharNonBlocking()) == 0)
		{
			break;
		}
		else
		{
			i++;
		}
	}
	buffer[i] = 0;
}



//--------------------The following methods are not working---------------------- 


//------------UART1_Interupt_Enable------------
// Enable UART1 Rx Interrupt
// Input: none
// Output: none
void UART1_Interrupt_Enable(void)
{
	UART1_IM_R |= 0x00000010;
	NVIC_PRI1_R &= ~0x00E00000;
	NVIC_EN0_R |= 0x00000040;
}

//------------UART1_Interrupt_Disable------------
// Disable UART1 Rx Interrupt
// Input: none
// Output: none
void UART1_Interrupt_Disable(void)
{
	UART1_IM_R &= ~0x00000010;
	NVIC_DIS0_R &= ~0x00000040;
}
