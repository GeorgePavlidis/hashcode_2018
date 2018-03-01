import argparse


def read_data(infile):
	with open(infile, 'r') as fin:
		rows, columns, vehicles, num_rides, bonus, steps = [int(num) for num in fin.readline().split()]

		rides = []
		for _ in range(num_rides):
			ride = [int(num) for num in fin.readline().split()]
			distance = calc_distance(ride[0], ride[1], ride[2], ride[3])
			ride.append(distance)
			rides.append(ride)

		return rows, columns, vehicles, num_rides, bonus, steps, rides


def init_cars(cars):

	info_cars = []
	for i in cars:
		car = [0, 0, 0, []]
		info_cars.append(car)
	return info_cars


def step_car(car, ride, info_cars, ride_id):
	distance = calc_distance(info_cars[car][0], info_cars[car][1], ride[0], ride[1])
	time = max(ride[4], distance)
	total = time + ride[6]
	info_cars[car][3] = total
	info_cars[car][0] = ride[2]
	info_cars[car][1] = ride[3]
	info_cars[3].append(ride_id)


def start_of_ride(ride, car, info_cars):
	distance = calc_distance(info_cars[car][0], info_cars[car][1], ride[0], ride[1])
	time = max(ride[4], distance)
	return time


def calc_distance(x1, y1, x2, y2):
	if x1 == x2 and y1 == y2:
		return 0
	d = abs(x2 - x1) + abs(y2 - y1)
	return d


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('input', type=str, help='input file')
	infile = parser.parse_args().input
	data = read_data(infile)
	info_cars = init_cars(data[2])
	print(data)
