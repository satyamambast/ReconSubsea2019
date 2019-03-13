/*
 var4 is the avrage value of the inductor output
 var5 is the live value of the inductor
 diff is var5-var4
 var5 value will always be higher than that of var4
 var5 for current setup is 1140-1190
 keep diff value in if statement between 50-80 
 */


#define vinPin A5
#define buz 9
#define pulsePin A4
//int vinPin= A5;
//int pulsePin= A4;
#define led 10
int val5=0,val4=0;
int count=0;
void setup() 
{
  Serial.begin(115200);
  pinMode(pulsePin, OUTPUT); 
  digitalWrite(pulsePin, LOW);
  pinMode(vinPin, INPUT);  
  pinMode(buz, OUTPUT);
  digitalWrite(buz, LOW);
  pinMode(led, OUTPUT);
}

void loop() 
{
  int minval=1023;
  int maxval=0,diff=0;
  long unsigned int sum=0;
  for (int i=0; i<200; i++)
  {
    //reset the capacitor
    pinMode(vinPin,OUTPUT);
        delayMicroseconds(20); 
    digitalWrite(vinPin,LOW);
    delayMicroseconds(20);
    pinMode(vinPin,INPUT);
    applyPulses();

  }
  val5=analogRead(A5)*10;
  delay(20);
  if(count==0)
  { 
    val4=avg()*10;
    count=1;
    }
    diff=val5-val4;
  Serial.println(val5);
  Serial.println(val4);
  if((diff) < 50)     // value between 50-80
  {
    digitalWrite(buz,HIGH);
    digitalWrite(led,HIGH);
  }
  else
  {
    digitalWrite(buz,LOW);
    digitalWrite(led,LOW);
  }
}

int avg()
{
  int avg1=0,avg2=0,avg3=0;
  for (int i=0;i<50;i++)
  {
    avg1=analogRead(A5);
    avg2=avg1+avg2;
  }
  avg3=avg2/50;
  return avg3;
}
void applyPulses()
{
    for (int i=0;i<10;i++) 
    {
      digitalWrite(pulsePin,HIGH); //take 3.5 uS
      delayMicroseconds(3);
      digitalWrite(pulsePin,LOW);  //take 3.5 uS
      delayMicroseconds(3);
    }
} 
