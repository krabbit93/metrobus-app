# Consulta de alcaldías y unidades de metrobus
## Tabla de contenido
- [Especificación del problema](#especificacion)
- [Diagrama general simplificado de la solución](#diagrama_general)
- [Diagramas de los procesos de la solucion](#procesos_solucion)
    - [Proceso de consulta de datos abiertos y registro de información](#proc_consulta_datos_abiertos)
    - [Procesos de consulta de información via API](#proc_consulta_api)
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


## <span id="especificacion">Especificación del problema</span>

Desarrollar un pipeline de análisis de datos utilizando los datos abiertos de la Ciudad de México
correspondientes a la ubicación de las unidades del metrobús durante la última hora para
obtener un histórico de la posición en la que se encuentra cada unidad que pueda ser
consultado mediante un API Rest (o Graphql) filtrando por unidad o por alcaldía.


## <span id="diagrama_general">Diagrama general simplificado de la solución</span>
![Diagrama general de la solución](/assets/general.png)

*<sub>Diagrama general simplificado de la solución</sub>*
## <span id="procesos_solucion">Diagramas de los procesos de la solucion</span>
### <span id="proc_consulta_datos_abiertos">Proceso de consulta de datos abiertos y registro de información</span>
![Proceso de consulta de datos abiertos](/assets/process_collect_data.png)

*<sub>Diagrama de proceso de consulta de datos abiertos y registro de información</sub>*

### <span id="proc_consulta_api">Procesos de consulta de información via API</span>
![Proceso de consulta via API](/assets/process_api.png)

*<sub>Diagrama de proceso de consulta via API</sub>*

## <span id="modulos">Módulos</span>
### <span id="town_hall_sync">Town hall sync [town_hall_sync]</span>

Este módulo recupera la información del API pública [*"limite de las alcaldias"*](https://datos.cdmx.gob.mx/explore/dataset/limite-de-las-alcaldias/information/) y realiza el guardado en la base de datos de la aplicación.

### <span id="domain">Domain [domain]</span>
Contiene la especificación de los objetos que mapean las tablas usando el ORM [SQLAlchemy](https://www.sqlalchemy.org/)



### <span id="unit_location_sync">Unit location sync [unit_location_sync]</span>
Determina a que alcaldia pertenece cada ubicacion obtenida de API pública [*"Ubicación de las unidades del Metrobús"*](https://datos.cdmx.gob.mx/explore/dataset/prueba_fetchdata_metrobus/information/) utilizando 
[Matlibplot](https://matplotlib.org/) y [Numpy](https://numpy.org/), posteriormente registra la información en la base de datos.

### <span id="api">API [api]</span>
Define el *Schema* del API Graphql utilizando [Graphene](https://graphene-python.org/) y resuelve cada petición

El script de la base de datos puede ser consultado [aquí](/database_config/database.schema.sql),
el cual genera el siguiente diagrama:

![Diagrama de base de datos](/assets/database.png)

<sub>Diagrama de base de datos</sub>

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

Imagen base utilizada: [python:3.7.8-slim](https://hub.docker.com/layers/python/library/python/3.7.8-slim/images/sha256-fe3f2c2b6ad6bb010426f50cdcc2350eef28f09505c1046f2ca68145c41ff6c6?context=explore) 
### <span id="contenedor-cron">Cron</span>
Dockerfile.cron

Imagen base utilizada: [mysql:8.0.20](https://hub.docker.com/layers/mysql/library/mysql/8.0.20/images/sha256-0ba38ea9c478d1e98b2f0bc0cee5a62345c9f06f78c4b48123bdc70d8d224686?context=explore)
### <span id="contenedor-database">Database</span>
Dockerfile.database

Imagen base utilizada: [python:3.7.8-slim](https://hub.docker.com/layers/python/library/python/3.7.8-slim/images/sha256-fe3f2c2b6ad6bb010426f50cdcc2350eef28f09505c1046f2ca68145c41ff6c6?context=explore)