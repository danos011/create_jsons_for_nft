from make_json import MakeJsons


def main():
    data = MakeJsons()
    rows = data.get_info_from_db()
    data.output_result(rows=rows)
    return 0


main()
