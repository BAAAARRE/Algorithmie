from tools.utils import DataPreparator, Calculate

lat_finish = 12.056097
lon_finish = 61.748800

def main():
    all_positions_files = DataPreparator.get_all_files('data/positions/')
    raw_data = DataPreparator.open_positions(all_positions_files)
    data = DataPreparator.raw_positions_to_dict(raw_data)
    data_clean = DataPreparator.clean_dict_positions(data)

    data_distance = Calculate.distance_position_finish(data_clean, lat_finish, lon_finish)
    data_speed = Calculate.speed_between_two_points(data_distance)
    data_ranking = Calculate.ranking_sail_boat(data_speed)

    print(data_ranking)


if __name__ == '__main__':
    main()
