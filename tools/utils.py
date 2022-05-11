import os
import math


class DataPreparator:
    """
    Class description
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
            id = 0
            new_name_file = name_file[14:-4]
            data[new_name_file] = {}
            for line in raw_data[name_file]:
                # print(line)
                data[new_name_file][id] = {}
                list_position = line[0].split(';')

                data[new_name_file][id]['id_voilier'] = list_position[1]
                data[new_name_file][id]['latitude'] = list_position[2]
                data[new_name_file][id]['longitude'] = list_position[3]
                data[new_name_file][id]['date'] = list_position[4]

                id += 1
        return data

    @staticmethod
    def clean_dict_positions(data):
        """

        :param dict_positions: dict.
        :return: dict.
        """
        for name_file in data:
            for id in data[name_file]:
                data[name_file][id]['date'] = data[name_file][id]['date'].replace("\n", "")
                data[name_file][id]['latitude'] = float(data[name_file][id]['latitude'].replace("N", ""))
                data[name_file][id]['longitude'] = float(data[name_file][id]['longitude'].replace("W", ""))

        return data


class Calculate:
    @staticmethod
    def distance_lat_lon(lat1, lon1, lat2, lon2):
        """

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
        for name_file in data:
            for id in data[name_file]:
                lat_pos = data[name_file][id]['latitude']
                lon_pos = data[name_file][id]['longitude']
                distance = Calculate.distance_lat_lon(lat_pos, lon_pos, lat_fin, lon_fin)
                data[name_file][id]['distance'] = distance
        return data
