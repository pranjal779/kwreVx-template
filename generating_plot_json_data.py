import json


def generate_json_data():
    data = {
        "schema": {
            "fields": [
                {
                    "name": "index",
                    "type": "integer"
                },
                {
                    "name": "plot_id",
                    "type": "integer"
                },
                {
                    "name": "station_id",
                    "type": "string"
                },
                {
                    "name": "plot_type_id",
                    "type": "integer"
                },
                {
                    "name": "y_axis_lower",
                    "type": "number"
                },
                {
                    "name": "y_axis_upper",
                    "type": "number"
                },
                {
                    "name": "x_axis_start_date",
                    "type": "datetime"
                },
                {
                    "name": "x_axis_end_date",
                    "type": "datetime"
                }
            ],
            "primaryKey": ["index"],
            "pandas_version": "1.4.0"
        },
        "data": []
    }

    # Generate 784 objects
    for i in range(784):
        plot_type_id = (i % 7) + 1
        data_object = {
            "index": i,
            "plot_id": i + 1,
            "station_id": f"Station_{i % 7}",
            "plot_type_id": plot_type_id,
        }

        if plot_type_id == 1:
            data_object["y_axis_lower"] = -0.3
            data_object["y_axis_upper"] = 1.5
            data_object["x_axis_start_date"] = "1920-01-15T00:00:00.000"
            data_object["x_axis_end_date"] = "2025-12-15T00:00:00.000"
        else:
            data_object["y_axis_lower"] = - \
                1.8 if plot_type_id in [2, 4, 6, 7] else 0.0
            data_object["y_axis_upper"] = 1.8 if plot_type_id in [
                2, 5, 6, 7] else 0.3
            data_object["x_axis_start_date"] = None
            data_object["x_axis_end_date"] = None

        data["data"].append(data_object)

    return data


# Generate JSON data and save it to a file
generated_data = generate_json_data()
with open("plot.json", "w") as file:
    json.dump(generated_data, file, indent=2)

print("JSON data generated and saved to 'plot.json'")
