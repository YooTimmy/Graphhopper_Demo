import tkinter as tk
import utility
import itertools
##Define Window Size
HEIGHT = 1200
WIDTH = 1600

def format_input_data(location_list):
	try:
		final_str = 'There are total {num} locations in the input file. \nThe list of coordinates are {location_list}'.format(
			num=len(location_list), location_list=location_list)
	except:
		final_str = 'There was a problem retrieving that information'
	return final_str

##generate pair of locations based on input file
def get_input_data_info(filename):
	global input_location_pairs
	location_list = utility.read_location_data(filename)
	label['text'] = format_input_data(location_list)
	input_location_pairs = list(itertools.combinations(location_list, 2))
	return input_location_pairs

def show_map(location_pairs):
	for location_pair in location_pairs:
		#print(location_pair)
		utility.generate_map(location_pair)

def download_route(location_pairs):
	for location_pair in location_pairs:
		utility.download_route(location_pair)

def display_route(location_pairs):
	final_route = []
	for location_pair in location_pairs:
		#print('Between location:',location_pair)
		temp = utility.display_route_info(location_pair)
		temp1 = ''.join([w for w in temp])
		final_route.append(temp1)
	result = ''.join([w for w in final_route])
	label['text'] = result

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.3, relheight=1)

button = tk.Button(frame, text="Check Input", font=40, command=lambda: get_input_data_info(entry.get()))
button.place(relx=0.35, relheight=1, relwidth=0.3)

display_route_button = tk.Button(frame, text="Display Route", font=40, command= lambda: display_route(input_location_pairs))
display_route_button.place(relx=0.7, relheight=1, relwidth=0.3)

second_frame = tk.Frame(root, bg='#80c1ff', bd=5)
second_frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.7, anchor='n')

label = tk.Label(second_frame, wraplength=1000,justify=tk.LEFT)
label.place(relwidth=1, relheight=1)

third_frame = tk.Frame(root, bg='#80c1ff', bd=5)
third_frame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.05, anchor='n')

show_map_button = tk.Button(third_frame, text="Show Map", font=40, command=lambda: show_map(input_location_pairs))
show_map_button.place(relx=0, relheight=1, relwidth=0.3)

download_route_button = tk.Button(third_frame, text="Download Route", font=40, command=lambda: download_route(input_location_pairs))
download_route_button.place(relx=0.35, relheight=1, relwidth=0.3)

upload_route_button = tk.Button(third_frame, text="Upload Route", font=40, command=lambda: utility.read_json_output('output.txt'))
upload_route_button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()