from utils import get_data, get_filtered_data


def main():

    data = get_data()
    data = get_filtered_data(data)

if __name__ == "__main__":
    main()