# AetherArchivist

A simple Python command-line tool for parsing and displaying mock weather data.

## Usage

Run `python main.py` to parse the default mock data.

Run `python main.py <data_string>` to parse a custom weather data string.

## Example Data Format

`City=Exampleville,Temp=25C,Humidity=60%,Wind=15kmh`

## Notes

*   Temperature must include units (C or F).
*   Wind speed must include units (kmh or mph).
*   The order of parameters does not matter.
*   Invalid or missing parameters will result in an error message.
