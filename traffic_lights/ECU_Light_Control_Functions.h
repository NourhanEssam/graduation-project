// B 0,1,2 is North 
// B 3,4,5 is West
// E 0,1,2 is East
// E 3,4,5 is South
// Green, Orange and Red respectively

#define North_Port GPIO_PORTB_BASE
#define West_Port GPIO_PORTB_BASE
#define East_Port GPIO_PORTE_BASE
#define South_Port GPIO_PORTE_BASE
#define North_Green GPIO_PIN_0
#define North_Orange GPIO_PIN_1
#define North_Red GPIO_PIN_2
#define West_Green GPIO_PIN_3
#define West_Orange GPIO_PIN_4
#define West_Red GPIO_PIN_5
#define East_Green GPIO_PIN_0
#define East_Orange GPIO_PIN_1
#define East_Red GPIO_PIN_2
#define South_Green GPIO_PIN_3
#define South_Orange GPIO_PIN_4
#define South_Red GPIO_PIN_5

void Lights_Init(void);
void North_Green_On(void);
void North_Green_Off(void);
void North_Orange_On(void);
void North_Orange_Off(void);
void North_Red_On(void);
void North_Red_Off(void);
void West_Green_On(void);
void West_Green_Off(void);
void West_Orange_On(void);
void West_Orange_Off(void);
void West_Red_On(void);
void West_Red_Off(void);
void East_Green_On(void);
void East_Green_Off(void);
void East_Orange_On(void);
void East_Orange_Off(void);
void East_Red_On(void);
void East_Red_Off(void);
void South_Green_On(void);
void South_Green_Off(void);
void South_Orange_On(void);
void South_Orange_Off(void);
void South_Red_On(void);
void South_Red_Off(void);