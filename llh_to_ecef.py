# llh_to_eceh.py
#
# Usage: python llh_to_eceh.py lat_deg long_deg hae_km 
#  Converts latitude, height above ellipsoid to ECEF coordinates
# Parameters:
#  lat_deg: lattitude in degrees
#  long_deg: longitude in degrees
#  hae_km: height above ellipsoid in km
# Output:
#  Print the components of radius vector in ECEF
#
# Written by Robert King
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys  # argv
import math # math module

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## calc_denom: Calculates the denominator from the calculations for c_E and s_E
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-ecc**2.0 * math.sin(lat_rad)**2.0)

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  long_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
   'Usage: '\
   'python llh_to_eceh.py lat_deg long_deg hae_km'\
  )
  exit()

lat_rad = math.radians(lat_deg)
long_rad = math.radians(long_deg)
denom = calc_denom(E_E,lat_rad)
c_E = R_E_KM/denom
s_E = R_E_KM*(1.0-E_E**2.0)/denom
r_x_km = (c_E+hae_km)*math.cos(lat_rad)*math.cos(long_rad)
r_y_km = (c_E+hae_km)*math.cos(lat_rad)*math.sin(long_rad)
r_z_km = (s_E+hae_km)*math.sin(lat_rad)
print(r_x_km)
print(r_y_km)
print(r_z_km)