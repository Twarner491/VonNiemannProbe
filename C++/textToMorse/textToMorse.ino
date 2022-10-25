/*
  Morse Code Project
  
  This code will loop through a string of characters and convert these to morse code.  
  It will blink two LED lights and play audio on a speaker.  
 */
 

char stringToMorseCode[] = "sex penis"; //static string to convert

int morseOutput = 13;      //pin of morse output
int led6 = 6;        
int audio8 = 8;     
int note = 1200;   

int dotLen = 1000;  
int dashLen = dotLen * 3;   
int elemPause = dotLen; 
int Spaces = dotLen * 3;     
int wordPause = dotLen * 7;  

int index;
String letters = "abcdefgh";
String numbers = "12345678";
String randomString = ""; //placeholder string to be filled with morse
String morseString = ""; //placeholder for morse converted string


void setup() {                
  pinMode(morseOutput, OUTPUT);
  Serial.begin(9600); //initizalize serial at 9600 baud
  Serial.print("morse code practice");
}


void loop()
{ 
    randomString = "";
    index = random(0, 7); //takes random value between indexes 0 and 7 of numbers and letters strings
    randomString += letters.substring(index, index); //take one char from letters string add to random string
    index = random(0,7);
    randomString += numbers.substring(index, index);
    index = random(0,7);
    randomString += letters.substring(index,index);
    index = random(0,7);
    randomString += letters.substring(index, index);
    Serial.println(randomString);

  // Loop through the string and get each character one at a time until the end is reached
  for (int i = 0; i < sizeof(stringToMorseCode) - 1; i++)
  {
    // Get the character in the current position
	char tmpChar = stringToMorseCode[i];
	// Set the case to lower case
	tmpChar = toLowerCase(tmpChar);
	// Call the subroutine to get the morse code equivalent for this character
	GetChar(tmpChar);
	Serial.print(stringToMorseCode);
  }
  
  // At the end of the string long pause before looping and starting again
  LightsOff(8000);			
}

// DOT
void MorseDot()
{
  digitalWrite(morseOutput, HIGH);  	// turn the LED on 
  delay(dotLen);             	// hold in this position
}

// DASH
void MorseDash()
{
  digitalWrite(morseOutput, HIGH);  	// turn the LED on 
  digitalWrite(led6, HIGH);
  tone(audio8, note, dashLen);	// start playing a tone
  delay(dashLen);               // hold in this position
}

// Turn Off
void LightsOff(int delayTime)
{
  digitalWrite(morseOutput, LOW);    	// turn the LED off  	
  digitalWrite(led6, LOW);
  noTone(audio8);	       	   	// stop playing a tone
  delay(delayTime);            	// hold in this position
}

// *** Characters to Morse Code Conversion *** //
void GetChar(char tmpChar)
{
	// Take the passed character and use a switch case to find the morse code for that character
	switch (tmpChar) {
	  case 'a':	
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'b':
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'c':
	    MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'd':
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'e':
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'f':
	    MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'g':
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'h':
	    MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'i':
	    MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'j':
	    MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
      case 'k':
	    MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'l':
	    MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
      case 'm':
	    MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'n':
	    MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'o':
	    MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'p':
	    MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 'q':
	    MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'r':
	    MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 's':
	    MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  case 't':
	    MorseDash();
		LightsOff(elemPause);
		break;
	  case 'u':
	    MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'v':
	    MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'w':
	    MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'x':
	    MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'y':
	    MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		break;
	  case 'z':
	    MorseDash();
		LightsOff(elemPause);
		MorseDash();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		MorseDot();
		LightsOff(elemPause);
		break;
	  default: 
		// If a matching character was not found it will default to a blank space
		LightsOff(Spaces);			
	}
}
