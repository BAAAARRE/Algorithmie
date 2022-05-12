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
        Open all positions file ant put all file in a dict and all lines of file in a list
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
    def open_sailboats():
        """
        Open sailboats file and put it in a dict
        :return:
        """
        list_sailboats = []
        with open(f"data/voiliers.tsv") as file:
            for line in file:
                list_sailboats.append(line.split('\t'))

        dict_sailboats = {}
        for sailboat in list_sailboats[1:]:
            dict_sailboats[sailboat[0]] = sailboat[1].replace('\n', '')

        return dict_sailboats

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
    def clean_dict_positions(data, sailboats_name):
        """
        Remove useless characters in fields and put right type, and add sailboat's name
        :param data: dict.
        :param sailboats_name: dict.
        :return: dict.
        """
        for name_file in data:
            for id in data[name_file]:
                data[name_file][id]['date'] = data[name_file][id]['date'].replace("\n", "")
                data[name_file][id]['date'] = datetime.datetime.strptime(data[name_file][id]['date'],
                                                                         '%m/%d/%y %H:%M:%S')
                data[name_file][id]['latitude'] = float(data[name_file][id]['latitude'].replace("N", ""))
                data[name_file][id]['longitude'] = float(data[name_file][id]['longitude'].replace("W", ""))

                data[name_file][id]['name'] = sailboats_name[id]
        return data


class Calculate:
    """
    Calculate indicators for sailboats
    """

    @staticmethod
    def distance_lat_lon(lat1, lon1, lat2, lon2):
        """
        Calculate distance in km between two coordinates
        :param lat1: float/integer. Latitude of first point
        :param lon1: float/integer. Longitude of first point
        :param lat2: float/integer. Latitude of second point
        :param lon2: float/integer. Longitude of second point
        :return: float.
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
        Calculate distance in km between actual position of sailboat and finish point
        :param data: dict.
        :param lat_fin: float. Latitude of finish point
        :param lon_fin: float. Longitude of finish point
        :return: dict
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
        """
        Calculate speed in Km/h for each sailboat between position and previous position
        :param data: dict.
        :return: dict.
        """
        previous_name_file = list(data.keys())[0]
        for name_file in data:
            for id in data[name_file]:
                previous_distance = data[previous_name_file][id]['distance']
                actual_distance = data[name_file][id]['distance']
                data[name_file][id]['distance_with_previous_point'] = round(previous_distance - actual_distance, 4)

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
        """
        Ranking sailboat by their distance to finish point
        :param data: dict.
        :return: dict.
        """
        for name_file in data:
            data[name_file] = dict(sorted(data[name_file].items(), key=lambda item: item[1]['distance']))
            rank = 1
            for id in data[name_file]:
                data[name_file][id]['ranking'] = rank
                rank += 1
        return data


class Visualisation:
    """
    Visualise the data
    """

    @staticmethod
    def ranking(data):
        for name_file in data:
            print('\n')
            print('----------')
            print(name_file)
            print('----------')
            print('\n')
            print("{:<14} {:<22} {:<8} {:<14}".format('Classement', 'Voilier', 'Vitesse', 'Distance'))
            for id in data[name_file]:
                print(
                    "N°{:<12} {:<22} {} km/h {} km".format(
                        data[name_file][id]['ranking'], data[name_file][id]['name'],
                        data[name_file][id]['speed'], data[name_file][id]['distance']))
