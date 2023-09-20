paragraph_dict = {
	"Welcome" : "Welcome to the typing speed test!",
	"Inspiration" : "You cannot let a fear of failure or a fear of comparison or a fear of judgment stop you from "
					"doing the things that will make you great.You cannot succeed without the risk of failure. "
					"You cannot have a voice without the risk of criticism. You cannot love without the risk of loss."
					" You must take these risks.",
	"Programming" : "Making and learning from mistakes is one of the best ways to improve your skills as a programmer."
					"Only by trying new things, and failing, can you learn what will not work as well as what will.",
	"Literature" : "Literature is a body of written works of a language, period, or culture, produced by scholars and "
				   "researchers specialized in a given field.0 It offers unique insights into human behavior, "
				   "challenges us to think creatively, sparks new ideas and debates, and provides a medium through "
				   "which we can share our experiences and stories.3 Literature makes us what we are, makes us think "
				   "and feel, and helps us to see the world differently, making us more mature and intelligent people."
				   " It connects individuals with larger truths and ideas in a society, creates a way for people to "
				   "record their thoughts and experiences in a way that is accessible to others, and opens our eyes "
				   "and makes us realize the wide world outside, surrounding us.",
    "Automation" : "Automation has several benefits in different industries. In manufacturing, automation can "
				   "streamline repetitive, hazardous, and tedious tasks, allowing one employee to work on several "
				   "machines or other jobs at the same time. Automation in manufacturing can help lower costs, improve"
				   " worker safety, reduce factory lead times, provide faster ROI, allow your operation to become more"
				   " competitive, increase production output, and so much more.0 Automated operations can handle "
				   "complex tasks dynamically and intelligently, based on predefined parameters, relieving operations"
				   " personnel from hours of tedious, boring, and manual tasks.2 Workflow automation software uses"
				   " rule-based logic to handle mundane tasks, freeing up employees for more meaningful work, "
				   "streamlined communication, empowered employees, and higher efficiency and productivity.3 "
				   "Business process automation eliminates bottlenecks that lead to lost time and revenue, improving "
				   "efficiency and control across every facet of the organization, from increased productivity and "
				   "compliance to better customer experience and performance."
	}

def get_paragraph_topic() -> dict:
	'''To get topics name from dictionary'''
	return paragraph_dict.keys()

def get_paragraph_text(para_key) -> str:
	'''To get topic\'s text from dictionary key'''
	return paragraph_dict.get(para_key)

def get_paragraph_topic() -> dict:
	'''To get topics name from dictionary'''
	return paragraph_dict.keys()

def get_paragraph_text(para_key) -> str:
	'''To get topic\'s text from dictionary key'''
	return paragraph_dict.get(para_key)