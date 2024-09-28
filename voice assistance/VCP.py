import speech_recognition as sr
import pyttsx3
import openai

def listen_for_command():
	recognizer = sr.Recognizer()

	with sr.Microphone() as source : 
		print("listenig for a voice command.......")
		audio = recognizer.listen(source)

	try:
		print("Recognizing......")
		command = recognizer.recognize_google(audio) #speech to text
		print(f"Command: {command}")
		return command  

	except sr.UnknownValueError:
		print("sorry, couldn't understand the command!")
		return None
	except sr.RequestError as e:
		print(f"could not request result form gogole speech recognition service; {e}")
		return None

def get_apt_response(prompt):
	openai.api_key = 'sk-Z42wYXyXNiyCQpw-0Nx38j0BtmsLNCOi-2p5Ubunr4T3BlbkFJjUWCHiDMFLpAz0YA6K7nlKplNF4bDW_lI5BldaiqsA'
	response = openai.ChatCompletion.create(
				model="gpt-4o",
				#prompt = prompt,
				max_tokens=30,
				messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
		)

	return response.choices[0].message["content"].strip()


def speak_response(response):
	#gpt to generate response 
	gpt_response = get_apt_response(response)
	
	#answer on screen
	print(f"Output: {gpt_response}")

	engine = pyttsx3.init() #text to speech engine / speak res.
	engine.say(gpt_response)
	engine.runAndWait() #wait for completion


if __name__=="__main__":
	command = listen_for_command()

	if command:
		#response = "You said : "+command
		speak_response(command)

