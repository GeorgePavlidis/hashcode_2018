import argparse
from operator import itemgetter
import sys
import copy as copy

car_ride = []


def read_data(infile):
	with open(infile, 'r') as fin:
		rows, columns, vehicles, num_rides, bonus, steps = [int(num) for num in fin.readline().split()]

		rides = []
		for i in range(num_rides):
			ride = [int(num) for num in fin.readline().split()]
			distance = calc_distance(ride[0], ride[1], ride[2], ride[3])
			ride.append(distance)
			ride.append(i)
			rides.append(ride)

		return rows, columns, vehicles, num_rides, bonus, steps, rides


def algorithm(data, info_cars):
	rides = copy.copy(data[6])
	rides = sorted(rides, key=lambda eval: [eval[5]-eval[6]])
	# for every ride
	for r in rides:
		total_dis = []
		vehicle = -1
		# for every car
		for car_id in range(0, data[2]):
			total_dis.append(start_of_ride(r, car_id, info_cars))
		# which car will take the ride
		vehicle = total_dis.index(min(total_dis))
		# print (total_dis)
		if (r[5] > total_dis[vehicle]):
			step_car(vehicle, r, info_cars, r[7])


def init_cars(cars):
	global car_ride
	info_cars = []

	for i in range(0, cars):
		car = [0, 0, 0]
		car_ride.append([])
		info_cars.append(car)
	return info_cars


def step_car(car, ride, info_cars, ride_id):
	distance = calc_distance(info_cars[car][0], info_cars[car][1], ride[0], ride[1])
	time = max(ride[4], info_cars[car][2] + distance)
	total = time + ride[6]
	info_cars[car][2] = total
	info_cars[car][0] = ride[2]
	info_cars[car][1] = ride[3]
	car_ride[car].append(ride_id)


def start_of_ride(ride, car, info_cars):
	distance = calc_distance(info_cars[car][0], info_cars[car][1], ride[0], ride[1])
	time = max(ride[4], info_cars[car][2] + distance)
	if (time + ride[6] < ride[5]):
		return time + ride[6]
	else:
		return sys.maxsize


def calc_distance(x1, y1, x2, y2):
	if x1 == x2 and y1 == y2:
		return 0
	d = abs(x2 - x1) + abs(y2 - y1)
	return d


def printData(info_cars):
	for i in car_ride:
		print(str(len(i)), *i)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('input', type=str, help='input file')
	infile = parser.parse_args().input
	data = read_data(infile)
	info_cars = init_cars(data[2])
	algorithm(data, info_cars)
	printData(info_cars)

















