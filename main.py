import folium

# Данные для улиц
streets = {
    "Щетинкина": {
        "markers": [
            {"name": " 1", "coords": [53.7252, 91.4428]},
            {"name": " 2", "coords": [53.7199, 91.4444]}
        ],
        "line": [
            [53.726186, 91.44252],
            [53.734935, 91.43993],
            [53.733805, 91.440309],
            [53.727508, 91.442126],
            [53.7248349, 91.442895],
            [53.724819, 91.442882],
            [53.722302, 91.44362],
            [53.717319, 91.445112],
        ]
    },
    "Ленина": {
        "markers": [
            {"name": " 3", "coords": [53.7215, 91.4381]},
            {"name": " 4", "coords": [53.7224, 91.4468]}
        ],
        "line": [
            [53.7211, 91.4333],
            [53.722755, 91.4495],
            [53.723056, 91.4539],
            [53.7234, 91.4565],
        ]
    },
    "Чертыгашева": {
        "markers": [
            {"name": "5", "coords": [53.724500, 91.440000]},
            {"name": "6", "coords": [53.7246, 91.4414]}
        ],
        "line": [
    [53.723808, 91.432518],
    [53.724108, 91.435558],
    [53.724206, 91.436697],
    [53.724223, 91.436802],
    [53.724372, 91.437974],
    [53.724412, 91.438316],
    [53.724660, 91.440872],
    [53.724754, 91.441700],
    [53.724843, 91.442738],
    [53.724854, 91.442893],
    [53.724857, 91.442936],
    [53.725037, 91.445045],
    [53.725465, 91.449354],
    [53.725606, 91.450948],
    [53.725824, 91.453085],
    [53.725840, 91.453251],
    [53.725965, 91.454592],
    [53.726027, 91.455169],

        ]
    },
    "Крылова": {
        "markers": [
            {"name": "Маркер 1", "coords": [53.7352,  91.4429]},
            {"name": "Маркер 2", "coords": [53.7360, 91.4519]}
        ],
        "line": [
            [53.7350, 91.4400],
            [53.7352, 91.4429],
            [53.7353, 91.4441],
            [53.7360, 91.4519],
        ]
    }
}

m = folium.Map(
    location=[53.722279, 91.443704],
    zoom_start = 16,
    tiles=None,
    attribution_control=0
)
# слои карты
folium.TileLayer('CyclOSM', name="CyclOSM").add_to(m)
folium.TileLayer('Esri.WorldImagery', name="Esri World Imagery").add_to(m)
folium.TileLayer('OpenStreetMap', name="OpenStreetMap").add_to(m)

for street_name, data in streets.items():
    # Создаем группу для каждой улицы
    street_group = folium.FeatureGroup(name=street_name)

    # Добавляем маркеры
    for marker in data["markers"]:
        folium.Marker(
            location=marker["coords"],
            popup=f"<b>{marker['name']}</b>",
            icon=folium.Icon(icon="seedling", prefix="fa", color="green"),
        ).add_to(street_group)

    # Добавляем линию
    folium.PolyLine(
        locations=data["line"],
        color="#ff5200",  # Цвет линии
        weight=10,      # Толщина линии
    ).add_to(street_group)

    # Добавляем группу улицы на карту
    street_group.add_to(m)

# Добавляем контроллер слоев для переключения между улицами collapsed=False
folium.LayerControl().add_to(m)

# Сохраняем карту
m.save("map.html")
