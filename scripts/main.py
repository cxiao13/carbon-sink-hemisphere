# basic
import numpy as np
import pandas as pd
import xarray as xr
import math
import argparse

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def spherical_to_cartesian(lat, lon):
    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    return x, y, z

def angle_between_points(lat1, lon1, lat2, lon2):
    lat1_rad = degrees_to_radians(lat1)
    lon1_rad = degrees_to_radians(lon1)
    lat2_rad = degrees_to_radians(lat2)
    lon2_rad = degrees_to_radians(lon2)

    x1, y1, z1 = spherical_to_cartesian(lat1_rad, lon1_rad)
    x2, y2, z2 = spherical_to_cartesian(lat2_rad, lon2_rad)

    dot_product = x1 * x2 + y1 * y2 + z1 * z2
    magnitude1 = math.sqrt(x1**2 + y1**2 + z1**2)
    magnitude2 = math.sqrt(x2**2 + y2**2 + z2**2)

    cos_theta = dot_product / (magnitude1 * magnitude2)
    # for very small error ignore
    if cos_theta > 1:
        cos_theta = 1
    elif cos_theta < -1:
        cos_theta = -1
    try:
        theta = math.acos(cos_theta)
    except:
        print(lat2)
        print(lon2)
        print(cos_theta)

    return theta

def create_lat_lon_nc(nee2021):
    n_lat = nee2021.latitude.values.size
    n_lon = nee2021.longitude.values.size
    lat_nc = nee2021.copy()
    lat_nc.data = np.tile(nee2021.latitude.values.T,(n_lon,1)).T
    lon_nc = nee2021.copy()
    lon_nc.data = np.tile(nee2021.longitude.values,(n_lat,1))
    
    return lat_nc, lon_nc

# def angle_hemisphere()

def angle_hemisphere(nee2021, lat_t, lon_t):
    n_lat = nee2021.latitude.values.size
    n_lon = nee2021.longitude.values.size
    lat_nc, lon_nc = create_lat_lon_nc(nee2021)
    angle_nc = nee2021.copy()
    # angle_nc = angle_nc.stack(pix=('latitude','longitude'))
    # lat_nc = lat_nc.stack(pix=('latitude','longitude'))
    # lon_nc = lon_nc.stack(pix=('latitude','longitude'))
    for i in range(n_lat//2):
        for j in range(n_lon):
            angle = angle_between_points(lat1=lat_t, lon1=lon_t, lat2=lat_nc[i,j], lon2=lon_nc[i,j])
            angle_nc[i,j] = angle
            jc = j+n_lon//2 if j < n_lon//2 else j-n_lon//2
            angle_nc[n_lat-i-1,jc] = math.pi - angle
    
    return angle_nc

# start to calculate for each pixel now take long time
def nee_hemis_calc(nee2021_weighted, n):
    n_lat = nee2021_weighted.latitude.values.size
    n_lon = nee2021_weighted.longitude.values.size
    nee_hemis = xr.full_like(nee2021_weighted, -999)
    for i in (range(n_lat//2)):
        for j in range(n*6, n_lon//60+n*6):
            lat_t = nee_hemis[i,j].latitude.values
            lon_t = nee_hemis[i,j].longitude.values
            angle_nc = angle_hemisphere(nee2021_weighted, lat_t, lon_t)
            nee_hemis[i,j] = nee2021_weighted.where(angle_nc <= 0.5*math.pi).sum()
            jc = j+n_lon//2 if j < n_lon//2 else j-n_lon//2
            nee_hemis[n_lat-i-1,jc] = nee2021_weighted.where(angle_nc >= 0.5*math.pi).sum()

    return nee_hemis

# for parallization by slurm job array
parser = argparse.ArgumentParser()
parser.add_argument('idx', type=int, help='simulation idx')
args = parser.parse_args()

# read the NEE file
nee2021_weighted = xr.load_dataarray(f"../data/interm/nee_2021_weighted.nc")
nee_hemis_test = nee_hemis_calc(nee2021_weighted, args.idx)

nee_hemis_test.to_netcdf(f'../data/interm/nee_hemis.{args.idx}.nc')
