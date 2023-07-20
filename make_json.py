import json
import psycopg2
from psycopg2.extras import NamedTupleCursor

JSON_FORMAT = '.json'
FOLDER = f'json_file/'
DB = 'postgresql://localhost:5432/ducks'


class MakeJsons:

    def __init__(self):
        self.conn = psycopg2.connect(DB)
        self.cur = self.conn.cursor()
        self.json_format = JSON_FORMAT
        self.dir1 = FOLDER

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def __create_dict(self, r) -> dict:
        future_json = {
            "name": r[0],
            "image": r[1],
            "attributes": [
                {
                    "trait_type": "background",
                    "value": r[2]
                },
                {
                    "trait_type": "entourage_background",
                    "value": r[3]
                },
                {
                    "trait_type": "paws",
                    "value": r[4]
                },
                {
                    "trait_type": "body_shape",
                    "value": r[5]
                },
                {
                    "trait_type": "body_color",
                    "value": r[6]
                },
                {
                    "trait_type": "pattern",
                    "value": r[7]
                },
                {
                    "trait_type": "plumage",
                    "value": r[8]
                },
                {
                    "trait_type": "element_background",
                    "value": r[9]
                },
                {
                    "trait_type": "hairstyle",
                    "value": r[10]
                },
                {
                    "trait_type": "eye_color",
                    "value": r[11]
                },
                {
                    "trait_type": "eye_shape",
                    "value": r[12]
                },
                {
                    "trait_type": "wings",
                    "value": r[13]
                },
                {
                    "trait_type": "beak",
                    "value": r[14]
                },
                {
                    "trait_type": "entourage_foreground",
                    "value": r[15]
                },
                {
                    "trait_type": "element_foreground",
                    "value": r[16]
                },
                {
                    "trait_type": "TIER",
                    "value": r[19]
                },
            ],
            "collection_name": r[17],
            "description": r[18],
            "url": r[20],

        }
        return future_json

    def get_info_from_db(self):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute(
                "SELECT d.name,d.image,d.background,d.entourage_background,d.paws,d.body_shape,d.body_color,d.pattern,"
                "d.plumage,d.element_background,d.hairstyle,d.eye_color,d.eye_shape,d.wings,d.beak,d.entourage_foreground,"
                "d.element_foreground,d.collection_name,d.description,CASE d.level WHEN 3 THEN 1 WHEN 1 THEN 3 ELSE 2 "
                "END AS Tier, CONCAT('https://app.openducks.com/ducks/', d.code) AS URL FROM ducks AS d")
            rows = curs.fetchall()
            return rows

    def output_result(self, rows):
        name = 1
        folder = 'json_file/'
        type_of_file = '.json'

        for r in rows:
            future_json = self.__create_dict(r)

            json_string = json.dumps(future_json, indent=4)

            with open(folder + str(name) + type_of_file, "w+") as json_file:
                json_file.write(json_string)
            name += 1
