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
        :return: list.
        """
        list_positions = []
        for position_file in all_positions_files:
            with open(f"data/positions/{position_file}") as file:
                for line in file:
                    if line != 'POSADRENA\n':
                        list_positions.append(line.split('\t'))
        return list_positions

    @staticmethod
    def list_positions_to_dict(list_positions):
        """
        Put list_positions elements in a dict with incremental id in key for line,
        and all lines element wih name in key and value in value.
        :param list_positions: list.
        :return: dict.
        """
        id = 0
        dict_positions = {}
        for position in list_positions:
            dict_positions[id] = {}
            list_position = position[0].split(';')

            dict_positions[id]['id_voilier'] = list_position[1]
            dict_positions[id]['latitude'] = list_position[2]
            dict_positions[id]['longitude'] = list_position[3]
            dict_positions[id]['date'] = list_position[4]

            id += 1
            return dict_positions

    @staticmethod
    def clean_dict_positions(dict_positions):
        """

        :param dict_positions: dict.
        :return: dict.
        """
        for id in dict_positions:
            dict_positions[id]['date'] = dict_positions[id]['date'].replace("\n", "")
            dict_positions[id]['latitude'] = float(dict_positions[id]['latitude'].replace("N", ""))
            dict_positions[id]['longitude'] = float(dict_positions[id]['longitude'].replace("W", ""))

        return dict_positions
