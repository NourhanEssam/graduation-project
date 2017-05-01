#include "Timers_Functions.h"

void init_gsm_control(void)
{
	SYSCTL_RCGC2_R |= SYSCTL_RCGC2_GPIOD;
	GPIO_PORTD_DIR_R |= 0x03;
	GPIO_PORTD_AFSEL_R &= ~0x03;
  GPIO_PORTD_DEN_R |= 0x03;
  GPIO_PORTD_PCTL_R &= ~0x000000FF;
  GPIO_PORTD_AMSEL_R &= ~0x03;
	timer1A_init(80000000);
}

void reset_gsm_module(void){
  GPIO_PORTD_DATA_R = GPIO_PORTD_DATA_R^0x1;
  timer1A_delayMs(1000);
  GPIO_PORTD_DATA_R = GPIO_PORTD_DATA_R^0x1;
}

void powerup_gsm_module(void){
  GPIO_PORTD_DATA_R = GPIO_PORTD_DATA_R^0x2;
  timer1A_delayMs(1000);
  GPIO_PORTD_DATA_R = GPIO_PORTD_DATA_R^0x2;
}
