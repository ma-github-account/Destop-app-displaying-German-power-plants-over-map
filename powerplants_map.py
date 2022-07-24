
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf

fig = plt.figure(figsize=(13, 8))

window=tk.Tk()
window.wm_title("German Powerplants Map")
window.columnconfigure(0, weight=1)

tk.Label(
  window,
  text="German Powerplants Map",
  font=("TkDefaultFont", 16)
).grid()

settings_frame = tk.LabelFrame(window, text='Powerplants types display setting')
settings_frame.grid(sticky=(tk.W + tk.E))

show_nuclear_powerplants_checkbutton_value = tk.BooleanVar(value=False)
tk.Checkbutton(
  settings_frame, variable=show_nuclear_powerplants_checkbutton_value,
  text='Show Nuclear Power Plants'
).grid(row=6, column=0, sticky=tk.W, pady=5)

show_thermal_powerplants_checkbutton_value = tk.BooleanVar(value=False)
tk.Checkbutton(
  settings_frame, variable=show_thermal_powerplants_checkbutton_value,
  text='Show Thermal Power Plants'
).grid(row=7, column=0, sticky=tk.W, pady=5)

show_hydroelectric_powerplants_checkbutton_value = tk.BooleanVar(value=False)
tk.Checkbutton(
  settings_frame, variable=show_hydroelectric_powerplants_checkbutton_value,
  text='Show Hydroelectric Power Plants'
).grid(row=6, column=1, sticky=tk.W, pady=5)

show_wind_powerplants_checkbutton_value = tk.BooleanVar(value=False)
tk.Checkbutton(
  settings_frame, variable=show_wind_powerplants_checkbutton_value,
  text='Show Wind Power Plants'
).grid(row=7, column=1, sticky=tk.W, pady=5)

show_solar_powerplants_checkbutton_value = tk.BooleanVar(value=False)
tk.Checkbutton(
  settings_frame, variable=show_solar_powerplants_checkbutton_value,
  text='Show Solar Power Plants'
).grid(row=6, column=2, sticky=tk.W, pady=5)

reload_button_frame = tk.LabelFrame(window, text='Reload button')
reload_button_frame.grid(sticky=(tk.W + tk.E))

for i in range(3):
  reload_button_frame.columnconfigure(i, weight=1 )

tk.Label(reload_button_frame , text='Click Reload button to refresh the map after setting changes').pack(side=tk.TOP)
Reload_button = tk.Button(reload_button_frame, text='RELOAD')
Reload_button.pack(side=tk.LEFT)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=7, column=0, sticky=(tk.W + tk.E))

latN = 55.5
latS = 47.2
lonW = 5.0
lonE = 15.9
cLat = (latN + latS) / 2
cLon = (lonW + lonE) / 2
projGer = ccrs.LambertConformal(central_longitude=cLon, central_latitude=cLat)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([lonW, lonE, latS, latN], crs=ccrs.PlateCarree())

ax.coastlines()
ax.gridlines()
ax.add_feature(cf.LAND, edgecolor='black')
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.RIVERS)
ax.add_feature(cf.OCEAN)

nuclear_power_plants = [
	["Neckarwestheim", 49.0406, 9.1755],
	["Essenbach", 48.6055, 12.2931],
	["Emsland", 52.4716, 7.3206]
]

def add_nuclear_powerplant_to_the_map(ax, city_name, lat, lon):

	lat_nuclear = lat
	lon_nuclear = lon
	img_nuclear = plt.imread('nuclear-power.png')
	imagebox_nuclear = OffsetImage(img_nuclear, zoom=.03)
	imagebox_nuclear.image.axes = ax
	ab_nuclear = AnnotationBbox(imagebox_nuclear, [lon_nuclear, lat_nuclear], pad=0, frameon=False)
	ax.add_artist(ab_nuclear)
	plt.text(lon_nuclear - 0.2, lat_nuclear, city_name, size=10, color='red', horizontalalignment='right', transform=ccrs.Geodetic())

def add_all_nuclear_power_plants_to_the_map(ax,nuclear_power_plants_list):

	for nuclear_power_plant_list_element in nuclear_power_plants_list:
		add_nuclear_powerplant_to_the_map(ax,nuclear_power_plant_list_element[0], nuclear_power_plant_list_element[1], nuclear_power_plant_list_element[2])

add_all_nuclear_power_plants_to_the_map(ax, nuclear_power_plants)

thermal_power_plants = [
	["Ahrensfelde", 52.3523, 13.3331],
	["Altchemnitz", 50.4754, 12.5527],
	["Altbach", 48.4314, 9.2229]
]

def add_thermal_powerplant_to_the_map(ax, city_name, lat, lon):

	lat_thermal = lat
	lon_thermal = lon
	img_thermal = plt.imread('otec.png')
	imagebox_thermal = OffsetImage(img_thermal, zoom=.03)
	imagebox_thermal.image.axes = ax
	ab_termal = AnnotationBbox(imagebox_thermal, [lon_thermal, lat_thermal], pad=0, frameon=False)
	ax.add_artist(ab_termal)
	plt.text(lon_thermal - 0.2, lat_thermal, city_name, size=10, color='red', horizontalalignment='right', transform=ccrs.Geodetic())

def add_all_thermal_power_plants_to_the_map(ax, thermal_power_plants_list):

	for thermal_power_plant_list_element in thermal_power_plants_list:
		add_thermal_powerplant_to_the_map(ax, thermal_power_plant_list_element[0], thermal_power_plant_list_element[1], thermal_power_plant_list_element[2])

add_all_thermal_power_plants_to_the_map(ax, thermal_power_plants)

hydroelectric_power_plants = [
	["Aufkirchen", 48.3052, 11.8577],
	["Bad Säckingen", 47.5577, 7.9567],
	["Nagold", 48.6008, 8.7371]
]

def add_hydroelectric_powerplant_to_the_map(ax, city_name, lat, lon):

	lat_hydroelectric = lat
	lon_hydroelectric = lon
	img_hydroelectric = plt.imread('hydro-power.png')
	imagebox_hydroelectric = OffsetImage(img_hydroelectric, zoom=.03)
	imagebox_hydroelectric.image.axes = ax
	ab_hydroelectric = AnnotationBbox(imagebox_hydroelectric, [lon_hydroelectric, lat_hydroelectric], pad=0, frameon=False)
	ax.add_artist(ab_hydroelectric)
	plt.text(lon_hydroelectric - 0.2, lat_hydroelectric, city_name, size=10, color='red', horizontalalignment='right', transform=ccrs.Geodetic())

def add_all_hydroelectric_power_plants_to_the_map(ax, hydroelectric_power_plants_list):

	for hydroelectric_power_plant_list_element in hydroelectric_power_plants_list:
		add_hydroelectric_powerplant_to_the_map(ax, hydroelectric_power_plant_list_element[0], hydroelectric_power_plant_list_element[1], hydroelectric_power_plant_list_element[2])

add_all_hydroelectric_power_plants_to_the_map(ax, hydroelectric_power_plants)

wind_power_plants = [
	["Holtriem", 53.3637, 7.2545],
	["Reußenköge", 54.3640, 8.5413],
	["Stößen-Teuchern", 51.7540, 11.5751]
]

def add_wind_powerplant_to_the_map(ax, city_name, lat, lon):

	lat_wind = lat
	lon_wind = lon	
	img_wind = plt.imread('wind-turbine.png')	
	imagebox_wind = OffsetImage(img_wind, zoom=.03)
	imagebox_wind.image.axes = ax
	ab_wind = AnnotationBbox(imagebox_wind, [lon_wind, lat_wind], pad=0, frameon=False)
	ax.add_artist(ab_wind)
	plt.text(lon_wind - 0.2, lat_wind, city_name, size=10, color='red', horizontalalignment='right', transform=ccrs.Geodetic())

def add_all_wind_power_plants_to_the_map(ax, wind_power_plants_list):

	for wind_power_plant_list_element in wind_power_plants_list:

		add_wind_powerplant_to_the_map(ax, wind_power_plant_list_element[0], wind_power_plant_list_element[1], wind_power_plant_list_element[2])

add_all_wind_power_plants_to_the_map(ax, wind_power_plants)

solar_power_plants = [
	["Arnstein", 50.0100, 9.5515],
	["Pocking", 48.4000, 13.1755],
	["Gottelborn", 49.2100, 7.2000]
]

def add_solar_powerplant_to_the_map(ax, city_name, lat, lon):

	lat_solar = lat
	lon_solar = lon	
	img_solar = plt.imread('solar-panel.png')
	imagebox_solar = OffsetImage(img_solar, zoom=.03)
	imagebox_solar.image.axes = ax
	ab_solar = AnnotationBbox(imagebox_solar, [lon_solar, lat_solar], pad=0, frameon=False)
	ax.add_artist(ab_solar)
	plt.text(lon_solar - 0.2, lat_solar, city_name, size=10, color='red', horizontalalignment='right', transform=ccrs.Geodetic())

def add_all_solar_power_plants_to_the_map(ax, solar_power_plants_list):

	for solar_power_plant_list_element in solar_power_plants_list:

		add_solar_powerplant_to_the_map(ax, solar_power_plant_list_element[0], solar_power_plant_list_element[1], solar_power_plant_list_element[2])

add_all_solar_power_plants_to_the_map(ax, solar_power_plants)

def on_reset():

		show_nuclear_pp_value = show_nuclear_powerplants_checkbutton_value.get()
		show_thermal_pp_value = show_thermal_powerplants_checkbutton_value.get()
		show_hydroelectric_pp_value = show_hydroelectric_powerplants_checkbutton_value.get()
		show_wind_pp_value = show_wind_powerplants_checkbutton_value.get()
		show_solar_pp_value = show_solar_powerplants_checkbutton_value.get()

		canvas = FigureCanvasTkAgg(fig, master=window)
		canvas.draw()
		canvas.get_tk_widget().grid(row=7, column=0, sticky=(tk.W + tk.E))

		latN = 55.5
		latS = 47.2
		lonW = 5.0
		lonE = 15.9
		cLat = (latN + latS) / 2
		cLon = (lonW + lonE) / 2
		projGer = ccrs.LambertConformal(central_longitude=cLon, central_latitude=cLat)

		ax = plt.axes(projection=ccrs.PlateCarree())
		ax.set_extent([lonW, lonE, latS, latN], crs=ccrs.PlateCarree())

		ax.coastlines()
		ax.gridlines()
		ax.add_feature(cf.LAND, edgecolor='black')
		ax.add_feature(cf.BORDERS)
		ax.add_feature(cf.LAKES)
		ax.add_feature(cf.RIVERS)
		ax.add_feature(cf.OCEAN)

		if show_nuclear_pp_value == True:

			add_all_nuclear_power_plants_to_the_map(ax,nuclear_power_plants)

		if show_thermal_pp_value == True:

			add_all_thermal_power_plants_to_the_map(ax,thermal_power_plants)

		if show_hydroelectric_pp_value == True:

			add_all_hydroelectric_power_plants_to_the_map(ax,hydroelectric_power_plants)

		if show_wind_pp_value == True:

			add_all_wind_power_plants_to_the_map(ax,wind_power_plants)

		if show_solar_pp_value == True:

			add_all_solar_power_plants_to_the_map(ax,solar_power_plants)

Reload_button.configure(command=on_reset)

tk.mainloop()