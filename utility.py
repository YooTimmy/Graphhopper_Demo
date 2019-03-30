import requests
import webbrowser
import json

#Generate the route information based on location pair, and return the routing information as string for output at GUI
def display_route_info(location_pair):
	final_str = []
	url = 'https://graphhopper.com/api/1/route/?point='+str(location_pair[0][0])+','+str(location_pair[0][1])+'&point='+str(location_pair[1][0])+','+str(location_pair[1][1])+'&vehicle=car&locale=eg&points_encoded=false&key=bd4343f9-3ddf-40f9-b743-30c52f9085a9'
	r = requests.get(url).json()['paths'][0]
	print('The total distance between ('+str(location_pair[0][0])+','+str(location_pair[0][1])+') and ('+str(location_pair[1][0])+','+str(location_pair[1][1])+') are {0:.2f} km.'.format(r['distance'] / 1000))
	final_str.append('The total distance between ('+str(location_pair[0][0])+','+str(location_pair[0][1])+') and ('+str(location_pair[1][0])+','+str(location_pair[1][1])+') are {0:.2f} km.'.format(r['distance'] / 1000))
	print('Need around {} min by car.'.format(round(r['time'] / 60000)))
	final_str.append('Need around {} min by car.\n'.format(round(r['time'] / 60000)))
	num_of_route = len(r['instructions'])
	for i in range(num_of_route - 1):
		final_str.append(display_route(r, i))
	print('Arrive at destination')
	final_str.append('Arrive at destination.\n')
	return final_str

#Read in file containing the coordinates for target location, and return them as a list.
#Format is like:
# 52.528992,13.395625
# 52.504173,13.460789
# 52.516883,13.415988
def read_location_data(filename):
	with open(filename) as f:
		content = f.readlines()
	content = [x.strip().split(',') for x in content]
	content = [[float(x[0]),float(x[1])] for x in content]
	return content

##Find out the original coordinates from output.txt file, which is the output for download_route function.
def read_json_output(filename):
	with open(filename) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	final_list = []
	for i in range(len(content)):
		d = json.loads(content[i])
		location_pair = d['paths'][0]['snapped_waypoints']['coordinates']
		location_pair = [[x[1],x[0]] for x in location_pair]
		#print('this is location pair',location_pair)
		generate_map(location_pair)
	return final_list

##Generate Map using /maps API from graphhopper
def generate_map(location_pair):
	url = 'https://graphhopper.com/maps/?point='+str(location_pair[0][0])+','+str(location_pair[0][1])+'&point='+str(location_pair[1][0])+','+str(location_pair[1][1])+'&vehicle=car&locale=eg'
	webbrowser.open(url)

##Download route information as json format and store in the output.txt file in same folder
def download_route(location_pair):
	url = 'https://graphhopper.com/api/1/route/?point='+str(location_pair[0][0])+','+str(location_pair[0][1])+'&point='+str(location_pair[1][0])+','+str(location_pair[1][1])+'&vehicle=car&locale=eg&points_encoded=false&key=bd4343f9-3ddf-40f9-b743-30c52f9085a9'
	r = requests.get(url).json()
	with open('output.txt','a') as outfile:
		json.dump(r,outfile)
		outfile.write("\n")
	return r

##Display the routing information
def display_route(r,num):
	distance = round(r['instructions'][num]['distance'] / 1000, 2)
	time = round(r['instructions'][num]['time'] / 60000)
	string = str(r['instructions'][num]['text']) + ' and drive for {distance} km, expected to take {time} min by car.\n'.format(distance=distance,time=time)
	print(string)
	return string


## For testing purpose
# location_list = [[52.528992,13.395625],[52.504173,13.460789],[52.516883,13.415988]]
# location_list = read_location_data('location_data.txt')
# print('There are total {num} locations in the input file, the list of coordinates are {location_list}'.format(num=len(location_list),location_list=location_list))
# location_pair = list(itertools.combinations(location_list,2))
# for pair in location_pair:
# 	print(pair)
# 	generate_map(pair)
#	download_route(pair)
# read_json_output('output.txt')

