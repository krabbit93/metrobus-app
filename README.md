# Consulta de alcaldías y unidades de metrobus
## Tabla de contenido
- [Especificación del problema](#especificacion)
- [Diagrama general simplificado de la solución](#diagrama_general)
- [Diagramas de los procesos de la solucion](#procesos_solucion)
    - [Proceso de consulta de datos abiertos y registro de información](#proc_consulta_datos_abiertos)
    - [Procesos de consulta de información via API](#proc_consulta_api)
- [Versiones](#versiones)
- [Módulos](#modulos)
    - [Domain](#domain)
    - [Town hall sync](#town_hall_sync)
    - [Unit location sync](#unit_location_sync)
    - [API](#api)
    - [Test](#test)
- [Archivos](#archivos)
- [Contenedores](#contenedores)
    - [API](#contenedor-api)
    - [Cron](#contenedor-cron)
    - [Database](#contenedor-database)
- [Archivos de despliege para Kubernetes](#kubernetes)


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

## <span id="versiones">Versiones</span>

- Python: 3.7.8
- MySQL: 8.0.20
- Docker: 19.03.8
- Kubernetes
    - Major:"1"
    - Minor:"18"

## <span id="modulos">Módulos</span>
### <span id="domain">Domain [domain]</span>
Contiene la especificación de los objetos que mapean las tablas usando el ORM [SQLAlchemy](https://www.sqlalchemy.org/)

El script de la base de datos puede ser consultado [aquí](/database_config/database.schema.sql),
el cual genera el siguiente diagrama:

![Diagrama de base de datos](/assets/database.png)

<sub>Diagrama de base de datos</sub>

### <span id="town_hall_sync">Town hall sync [town_hall_sync]</span>

Este módulo recupera la información del API pública [*"limite de las alcaldias"*](https://datos.cdmx.gob.mx/explore/dataset/limite-de-las-alcaldias/information/) y realiza el guardado en la base de datos de la aplicación.

### <span id="unit_location_sync">Unit location sync [unit_location_sync]</span>
Determina a que alcaldia pertenece cada ubicacion obtenida de API pública [*"Ubicación de las unidades del Metrobús"*](https://datos.cdmx.gob.mx/explore/dataset/prueba_fetchdata_metrobus/information/) utilizando 
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

## <span id="test"></span>Test [test]
Contiene los test unitarios.

## <span id="archivos">Archivos</span>
- **[api.py](/api.py):** Inicia un servidor que expone el endpoint **/api** que corresponde a la API Graphql
- **[unit_location_sync.py](/unit_location_sync.py):** Inicia el proceso de guardar la informacion de las alcaldias si no existe (ver: [Town hall sync](#town_hall_sync)), despues guarda
la información de la ubicacion de las unidades del metrobus(ver:[Unit location sync](#unit_location_sync))
- **[requirements.api.py](/requirements.api.py):** Dependencias del contenedor [API](#contenedor-api)
- **[requirements.cron.py](/requirements.cron.py):** Dependencias del contendor [Cron](#contenedor-cron)
- **[Dockerfile.api](/Dockerfile.api):** Dockerfile para el contenedor [API](#contenedor-api)
- **[Dockerfile.cron](/Dockerfile.cron):** Dockerfile para el contenedor [Cron](#contenedor-cron)
- **[Dockerfile.database](/Dockerfile.database):** Dockerfile para el contenedor [Database](#contenedor-database)

## <span id="contenedores">Contenedores</span>
### <span id="contenedor-api">API</span>
[Dockerfile.api](/Dockerfile.api)

Imagen base utilizada: [python:3.7.8-slim](https://hub.docker.com/layers/python/library/python/3.7.8-slim/images/sha256-fe3f2c2b6ad6bb010426f50cdcc2350eef28f09505c1046f2ca68145c41ff6c6?context=explore)

Construccion: 
```shell script
 docker build -t krabbit1993/metrobus_api:1.0.1 -f Dockerfile.api .
``` 
### <span id="contenedor-cron">Cron</span>
[Dockerfile.cron](/Dockerfile.cron)

Imagen base utilizada: [mysql:8.0.20](https://hub.docker.com/layers/mysql/library/mysql/8.0.20/images/sha256-0ba38ea9c478d1e98b2f0bc0cee5a62345c9f06f78c4b48123bdc70d8d224686?context=explore)

Construccion: 
```shell script
 docker build -t krabbit1993/metrobus_cron:1.0.2 -f Dockerfile.cron .
``` 
### <span id="contenedor-database">Database</span>
[Dockerfile.database](Dockerfile.database)

Imagen base utilizada: [python:3.7.8-slim](https://hub.docker.com/layers/python/library/python/3.7.8-slim/images/sha256-fe3f2c2b6ad6bb010426f50cdcc2350eef28f09505c1046f2ca68145c41ff6c6?context=explore)

Construccion: 
```shell script
 docker build -t krabbit1993/metrobus_database:1.0.0 -f Dockerfile.database .
``` 

## <span id="kubernetes">Archivos de despliege para Kubernetes</span>

- **[/kubeconfig/01-database-pv.yaml](/kubeconfig/01-database-pv.yaml)**: Volumen persistente para la base de datos.
- **[/kubeconfig/02-database-pvc.yaml](/kubeconfig/02-database-pvc.yaml)**: Claims para el volumen persistente.
- **[/kubeconfig/03-database-secret.yaml](/kubeconfig/03-database-secret.yaml)**: Credenciales para la base de datos.
- **[/kubeconfig/04-database-rc.yaml](/kubeconfig/04-database-rc.yaml)**: Replication Controller de la base de datos
- **[/kubeconfig/05-database-svc.yaml](/kubeconfig/05-database-svc.yaml)**: Servicio para exponer la base de datos en la red del cluster
- **[/kubeconfig/06-cron-rc.yaml](/kubeconfig/06-cron-rc.yaml)**: Replication Controller para el contenedor del cron.
- **[/kubeconfig/07-api-rc.yaml](/kubeconfig/07-api-rc.yaml)**: Replication Controller para el contenedor del api.
- **[/kubeconfig/08-api-lb.yaml](/kubeconfig/08-api-lb.yaml)**: Load Balancer para exponer el API.