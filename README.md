# Big Data Dataset Processing Experiment

The growing number of vehicles in urban areas presents significant challenges for traffic management. Modern cities require effective monitoring systems to reduce congestion, improve safety, and support efficient public mobility. One increasingly used approach is the use of Big Data from traffic sensors that can record vehicle movements in real time.
Big Data itself has key characteristics known as the 3Vs: Volume, Velocity, and Variety. These three aspects are the basis for determining whether a dataset can be categorized as Big Data. The 3Vs of Big Data—volume, velocity, and variety—represent the three key characteristics that distinguish big data from traditional data types. These attributes highlight the differences between big data and conventional data sets, as well as the requirements for managing them effectively.

# How to run the script... (make sure to git clone first)
`cd 'c: users\your_directory'`

`pip install requests`

`python.exe -m pip install --upgrade pip` (optional)

`python bigdata.py`

## Example output:
### Sample Raw Data (First Route)

```json
{
  "type": "Feature",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [149.131, -35.21833],
      [149.130753, -35.2191925],
      [149.13063, -35.2195854],
      [149.130508, -35.21995],
      [149.1303, -35.2204]
    ]
  }
}
```

### Latest traffic statistics for a few routes:
```
📍 Route: (Gungahlin Dr/Sandford St) to Cooyong St/Northbourne Av) via Gungahlin Dr, Belconnen Wy and Barry Dr
   - Current Travel Time: 10 minutes 22 seconds
   - Delay: 9 seconds compared to normal conditions

📍 Route: (Cotter Rd/Tuggeranong Pwy) to (London Cct) via Adelaide Av
   - Current Travel Time: 8 minutes 46 seconds
   - Delay: -14 seconds compared to normal conditions

📍 Route: Drakeford Drive, Tuggeranong Parkway and Parkes Way to City
   - Current Travel Time: 14 minutes 19 seconds
   - Delay: 5 seconds compared to normal conditions

📍 Route: (PVMS1 Barton Hwy) to (Northbourne Av/Cooyong St) via Gungahlin Dr, Belconnen Wy and Barry Dr
   - Current Travel Time: 10 minutes 30 seconds
   - Delay: 7 seconds compared to normal conditions

📍 Route: (Gungahlin Dr/Sandford St) to (Cooyong St) via Ellenborough St and Northbourne Av
   - Current Travel Time: 9 minutes 28 seconds
   - Delay: 4 seconds compared to normal conditions
```

<img width="680" height="510" alt="image" src="https://github.com/user-attachments/assets/ba59368e-9e61-4271-a902-1ffcb796417a" />

wow data. such numbers... 
