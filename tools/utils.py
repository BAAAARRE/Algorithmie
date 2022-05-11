import os
import datetime
import math


class DataPreparator:
    """
    Class for open, clean and prepare data
    """

    @staticmethod
    def get_all_files(path_folder):
        """
        Get all files names from a folder
        :param path_folder: str. Path to folder
        :return: list.
        """
        all_positions_files = [f for f in os.listdir(path_folder) if os.path.isfile(os.path.join(path_folder, f))]
        return all_positions_files

    @staticmethod
    def open_positions(all_positions_files):
        """
        Open all positions file ant put all lines in a list
        :return: dict.
        """
        raw_data = {}
        for position_file in all_positions_files:
            list_positions = []
            with open(f"data/positions/{position_file}") as file:
                for line in file:
                    if line != 'POSADRENA\n':
                        list_positions.append(line.split('\t'))
            raw_data[position_file] = list_positions
        return raw_data

    @staticmethod
    def raw_positions_to_dict(raw_data):
        """
        Put list_positions elements in a dict with incremental id in key for line,
        and all lines element wih name in key and value in value.
        :param list_positions: list.
        :return: dict.
        """
        data = {}
        for name_file in raw_data:
            new_name_file = name_file[14:-4]
            data[new_name_file] = {}
            for line in raw_data[name_file]:
                list_position = line[0].split(';')
                id = list_position[1]

                data[new_name_file][id] = {}
                data[new_name_file][id]['latitude'] = list_position[2]
                data[new_name_file][id]['longitude'] = list_position[3]
                data[new_name_file][id]['date'] = list_position[4]

        return data

    @staticmethod
    def clean_dict_positions(data):
        """
        Remove useless characters in fields
        :param dict_positions: dict.
        :return: dict.
        """
        for name_file in data:
            for id in data[name_file]:
                data[name_file][id]['date'] = data[name_file][id]['date'].replace("\n", "")
                data[name_file][id]['date'] = datetime.datetime.strptime(data[name_file][id]['date'],
                                                                         '%m/%d/%y %H:%M:%S')
                data[name_file][id]['latitude'] = float(data[name_file][id]['latitude'].replace("N", ""))
                data[name_file][id]['longitude'] = float(data[name_file][id]['longitude'].replace("W", ""))

        return data


class Calculate:
    @staticmethod
    def distance_lat_lon(lat1, lon1, lat2, lon2):
        """
        Calculate distance in km between two coordinates
        :param lat1:
        :param lon1:
        :param lat2:
        :param lon2:
        :return:
        """
        radius = 6373.0

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = round(radius * c, 6)
        return distance

    @staticmethod
    def distance_position_finish(data, lat_fin, lon_fin):
        """
        
        :param data:
        :param lat_fin:
        :param lon_fin:
        :return:
        """
        for name_file in data:
            for id in data[name_file]:
                lat_pos = data[name_file][id]['latitude']
                lon_pos = data[name_file][id]['longitude']
                distance = Calculate.distance_lat_lon(lat_pos, lon_pos, lat_fin, lon_fin)
                data[name_file][id]['distance'] = distance
        return data

    @staticmethod
    def speed_between_two_points(data):
        previous_name_file = list(data.keys())[0]
        for name_file in data:
            for id in data[name_file]:
                previous_distance = data[previous_name_file][id]['distance']
                actual_distance = data[name_file][id]['distance']
                data[name_file][id]['distance_with_previous_point'] = previous_distance - actual_distance

                previous_time = data[previous_name_file][id]['date']
                actual_time = data[name_file][id]['date']
                data[name_file][id]['time_with_previous_point'] = round((actual_time - previous_time).seconds / 3600, 2)

                if data[name_file][id]['time_with_previous_point'] == 0:
                    data[name_file][id]['speed'] = 0
                else:
                    data[name_file][id]['speed'] = round(
                        data[name_file][id]['distance_with_previous_point'] / data[name_file][id][
                            'time_with_previous_point'], 2)

            previous_name_file = name_file
        return data

    @staticmethod
    def ranking_sail_boat(data):
        for name_file in data:
            data[name_file] = dict(sorted(data[name_file].items(), key=lambda item: item[1]['distance']))
            rank = 1
            for id in data[name_file]:
                data[name_file][id]['ranking'] = rank
                rank += 1
        return data


class Visualisation:
    """

    """
    @staticmethod
    def ranking(data):
        for name_file in data:
            print('\n')
            print('----------')
            print(name_file)
            print('----------')
            print('\n')
            print("{:<14} {:<10} {:<8}".format('Classement', 'Id Voilier', 'Vitesse'))
            for id in data[name_file]:
                print("N°{:<12} {:<10} {} km/h".format(data[name_file][id]['ranking'], id, data[name_file][id]['speed']))
