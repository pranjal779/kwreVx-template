import json

# Function to generate the JSON data


def generate_json_data():
    data = {
        "schema": {
            "fields": [
                {
                    "name": "index",
                    "type": "integer"
                },
                {
                    "name": "station_id",
                    "type": "string"
                },
                {
                    "name": "stn_name",
                    "type": "string"
                },
                {
                    "name": "active",
                    "type": "boolean"
                },
                {
                    "name": "published",
                    "type": "boolean"
                },
                {
                    "name": "update_monthly",
                    "type": "boolean"
                },
                {
                    "name": "station_title",
                    "type": "string"
                },
                {
                    "name": "epoch",
                    "type": "string"
                },
                {
                    "name": "mid_year",
                    "type": "string"
                },
                {
                    "name": "annotation",
                    "type": "string"
                }
            ],
            "primaryKey": ["index"],
            "pandas_version": "1.4.0"
        },
        "data": []
    }

    # Generate 143 objects
    for i in range(144):
        station_id = input(f"Enter station_id for object {i}: ")
        stn_name = input(f"Enter stn_name for object {i}: ")

        data_object = {
            "index": i,
            "station_id": f"{station_id}",
            "stn_name": f"{stn_name}",
            "active": False if i in [13, 17, 26, 47, 49, 52, 64, 85, 91, 95, 98] else True,
            "published": False if i in [4, 13, 17, 29, 34, 36, 38, 39, 44, 46, 50, 54, 55, 63, 65, 73, 74, 75, 78, 79, 81, 86, 88, 90, 99, 103, 106, 107, 108, 110, 113, 137, 138, 139, 140] else True,
            "update_monthly": False if i in [13, 17, 26, 47, 49, 52, 64, 85, 91, 95, 98] else True,
            "station_title": f"{station_id} {stn_name}",
            "epoch": "1983-2001",
            "mid_year": "1992",
            "annotation": None
        }
        data["data"].append(data_object)

    return data


# Generate JSON data and save it to a file
generated_data = generate_json_data()
with open("station.json", "w") as file:
    json.dump(generated_data, file, indent=2)

print("JSON data generated and saved to 'station.json'")
