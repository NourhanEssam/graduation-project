void SysTick_Init(void);
void SysTick_Wait(unsigned long delay);
void SysTick_delay10MS(unsigned long delay);

void timer0A_init(unsigned long clk);
void timer0A_disable(void);
void timer0A_delayMs(int ttime);

void timer1A_init(unsigned long clk);
void timer1A_disable(void);
void timer1A_delayMs(int ttime);

void timer2A_init(unsigned long clk);
void timer2A_disable(void);
void timer2A_delayMs(int ttime);

void timer3A_init(unsigned long clk);
void timer3A_disable(void);
void timer3A_delayMs(int ttime);
