from .openapi_data_generator.OpenApiDataGenerator import OpenApiDataGenerator
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--generate_responses', nargs='?', const=True, type=bool, default=False)
    parser.add_argument('--generate_invalid', nargs='?', const=True, type=bool, default=False)
    parser.add_argument('--use_cache', nargs='?', const=True, type=bool, default=False)
    parser.add_argument('--restart_cache', nargs='?', const=True, type=bool, default=False)
    args = parser.parse_args()

    if not (args.path and os.path.isfile(args.path)):
        print("Please insert path correctly")
    else:
        generator = OpenApiDataGenerator(args.path, args.generate_responses, args.generate_invalid,
                                         args.use_cache, args.restart_cache)
        print(generator)
