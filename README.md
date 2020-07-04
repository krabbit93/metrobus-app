# Consulta de alcaldías y unidades de metrobus
## Tabla de contenido
- [Introducción](#introduccion)
- [Diagrama general de la solución](#diagrama_general)
- [Módulos](#modulos)
    - [Town hall sync](#mod_town_hall_sync)
    - [Domain](#domain)
    - [Unit location sync](#unit_location_sync)
    - [API](#api)
- [Archivos](#archivos)
- [Contenedores](#contenedores)
    - [API](#contenedor-api)
    - [Cron](#contenedor-cron)
    - [Database](#contenedor-database)


## <span id="introduccion">Introducción</span>


## <span id="diagrama_general">Diagrama general de la solución</span>
![Diagrama general de la solución](/assets/general.png)

## <span id="modulos">Módulos</span>
### <span id="town_hall_sync">Town hall sync [town_hall_sync]</span>

Este módulo recupera la información del API pública *"limite de las alcaldias"* y realiza el guardado en la base de datos de la aplicación.

### <span id="domain">Domain [domain]</span>
Contiene la especificación de los objetos que mapean las tablas usando el ORM [SQLAlchemy](https://www.sqlalchemy.org/)

### <span id="unit_location_sync">Unit location sync [unit_location_sync]</span>
Determina a que alcaldia pertenece cada ubicacion obtenida de API pública *"Ubicación de las unidades del Metrobús"* utilizando 
[Matlibplot](https://matplotlib.org/) y [Numpy](https://numpy.org/), posteriormente registra la información en la base de datos.

### <span id="api">API [api]</span>
Define el *Schema* del API Graphql utilizando [Graphene](https://graphene-python.org/) y resuelve cada petición

A continuación se presenta el [Schema utilizado](/assets/graphql.schema):
````python
type Unit{
	id: Int
	label: String
	vehicleId: String
}

type TownHall{
	id: Int
	name: String
}

type UnitLocation{
	id: Int
	latitude: Float
	longitude: Float
	unit: Unit
	townHall: TownHall
	date: DateTime
}

scalar DateTime

type Query{
    """
    Obtain a list of units that have been within a town hall
    """
    availableUnits: [Unit]
    """
    Get the history of locations/dates of a unit
    """
    unitLocationHistory(
        unitId: Int!
    ): [UnitLocation]
    """
    Get a list of available town halls
    """
    availableTownHalls: [TownHall]
    """
    Get all the units that were in a town hall
    """
    unitsInTownHall(
        townHallId: Int!
    ): [Unit]
}
schema{
    query: Query
}
````

## <span id="archivos">Archivos</span>
- **api.py:** Inicia un servidor que expone el endpoint **/api** que corresponde a la API Graphql
- **unit_location_sync.py:** Inicia el proceso de guardar la informacion de las alcaldias si no existe (ver: [Town hall sync](#town_hall_sync)), despues guarda
la información de la ubicacion de las unidades del metrobus(ver:[Unit location sync](#unit_location_sync))
- **requirements.api.py:** Dependencias del contenedor [API](#contenedor-api)
- **requirements.cron.py:** Dependencias del contendor [CRON](#contenedor-cron)
- **Dockerfile.api:** Dockerfile para el contenedor [API](#contenedor-api)
- **Dockerfile.cron:** Dockerfile para el contenedor [Cron](#contenedor-cron)
- **Dockerfile.database:** Dockerfile para el contenedor [Database](#contenedor-database)

## <span id="contenedores">Contenedores</span>
### <span id="contenedor-api">API</span>
Dockerfile.api
### <span id="contenedor-cron">Cron</span>
Dockerfile.cron
### <span id="contenedor-database">Database</span>
Dockerfile.database