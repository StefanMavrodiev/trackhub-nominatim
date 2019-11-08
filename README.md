# trackhub-nominatim
Get geojson data from nominatim service.

Currently only countries export is supported. Also the only output format is json.

There is list with missing countries. These should be resolved when needed.

## Export

Run the script with:
```python
python3 -m nominatim countries.json
```