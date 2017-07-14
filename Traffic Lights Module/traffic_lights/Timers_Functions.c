#include "Timers_Functions.h"

void SysTick_Init(void){
  NVIC_ST_CTRL_R = 0;
  NVIC_ST_RELOAD_R = NVIC_ST_RELOAD_M;
  NVIC_ST_CURRENT_R = 0;
  NVIC_ST_CTRL_R = NVIC_ST_CTRL_ENABLE+NVIC_ST_CTRL_CLK_SRC;
}

void SysTick_Wait(unsigned long delay){
  volatile unsigned long elapsedTime;
  unsigned long startTime = NVIC_ST_CURRENT_R;
  do{
    elapsedTime = (startTime-NVIC_ST_CURRENT_R)&0x00FFFFFF;
  }
  while(elapsedTime <= delay);
}

void SysTick_delay10MS(unsigned long delay){
  unsigned long i;
  for(i=0; i<delay; i++){
    SysTick_Wait(800000);
  }
}

void timer0A_init(unsigned long clk){
  SYSCTL_RCGCTIMER_R |= 1;
    TIMER0_CTL_R = 0;
    TIMER0_CFG_R = 0;
    TIMER0_TAMR_R = 0x02;
    TIMER0_TAILR_R = clk/1000 - 1;
    TIMER0_ICR_R = 0x1;
    TIMER0_IMR_R = 0x00000001;
    NVIC_PRI4_R = (NVIC_PRI4_R&0x00FFFFFF)|0x80000000; // priority 4
    NVIC_EN0_R = 1<<19;           //enable IRQ 19 in NVIC
    TIMER0_CTL_R |= 0x01;
}

void timer0A_disable(void){
  TIMER0_CTL_R = 0;
  SYSCTL_RCGCTIMER_R &= ~0x01;
}

void timer0A_delayMs(unsigned int ttime){
    int i;
    for(i = 0; i < ttime; i++) { 
      while ((TIMER0_RIS_R & 0x1) == 0);
      TIMER0_ICR_R = TIMER_ICR_TATOCINT;
    }
}

void Timer0A_Handler(void){
  TIMER0_ICR_R = TIMER_ICR_TATOCINT;// acknowledge TIMER0A timeout
  /* Put your code here */
}

void timer1A_init(unsigned long clk){
  SYSCTL_RCGCTIMER_R |= 0x02;
    TIMER1_CTL_R = 0;
    TIMER1_CFG_R = 0;
    TIMER1_TAMR_R = 0x02;
    TIMER1_TAILR_R = clk/1000 - 1;
    TIMER1_ICR_R = 0x1;
    TIMER1_CTL_R |= 0x01;
}

void timer1A_disable(void){
  TIMER1_CTL_R = 0;
  SYSCTL_RCGCTIMER_R &= ~0x02;
}

void timer1A_delayMs(unsigned int ttime){
    int i;
    for(i = 0; i < ttime; i++) { 
      while ((TIMER1_RIS_R & 0x1) == 0);
      TIMER1_ICR_R = TIMER_ICR_TATOCINT;
    }
}

void timer2A_init(unsigned long clk){
  SYSCTL_RCGCTIMER_R |= 0x04;
    TIMER2_CTL_R = 0;
    TIMER2_CFG_R = 0;
    TIMER2_TAMR_R = 0x02;
    TIMER2_TAILR_R = clk/1000 - 1;
    TIMER2_ICR_R = 0x1;
    TIMER2_CTL_R |= 0x01;
}

void timer2A_disable(void){
  TIMER2_CTL_R = 0;
  SYSCTL_RCGCTIMER_R &= ~0x04;
}

unsigned int time;

void timer2A_delayMs(unsigned int ttime){
    int i;
		time = ttime;
    for(i = 0; i < time; i++) { 
      while ((TIMER2_RIS_R & 0x1) == 0);
      TIMER2_ICR_R = TIMER_ICR_TATOCINT;
    }
}

void timer3A_init(unsigned long clk){
  SYSCTL_RCGCTIMER_R |= 0x08;
    TIMER3_CTL_R = 0;
    TIMER3_CFG_R = 0;
    TIMER3_TAMR_R = 0x02;
    TIMER3_TAILR_R = clk/1000 - 1;
    TIMER3_ICR_R = 0x1;
    TIMER3_CTL_R |= 0x01;
}

void timer3A_disable(void){
  TIMER3_CTL_R = 0;
  SYSCTL_RCGCTIMER_R &= ~0x08;
}

void timer3A_delayMs(unsigned int ttime){
    int i;
    for(i = 0; i < ttime; i++) { 
      while ((TIMER3_RIS_R & 0x1) == 0);
      TIMER3_ICR_R = TIMER_ICR_TATOCINT;
    }
}
