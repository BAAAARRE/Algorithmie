from tools.utils import DataPreparator as Dp


def main():
    all_positions_files = Dp.get_all_files('data/positions/')
    list_positions = Dp.open_positions(all_positions_files)
    dict_positions = Dp.list_positions_to_dict(list_positions)
    dict_positions = Dp.clean_dict_positions(dict_positions)
    print(dict_positions)


if __name__ == '__main__':
    main()
