create database if not exists metrobus;
use metrobus;

create table if not exists town_halls
(
    id int auto_increment
        primary key,
    name varchar(100) not null
);

create table if not exists delimiter_points
(
    id int auto_increment
        primary key,
    latitude decimal(20,16) not null,
    longitude decimal(20,16) not null,
    town_hall_id int not null,
    constraint delimiter_points_town_halls_id_fk
        foreign key (town_hall_id) references town_halls (id)
);

create table if not exists units
(
    id int auto_increment
        primary key,
    vehicle_id varchar(20) not null,
    label varchar(80) not null
);

create table if not exists unit_locations
(
    id int auto_increment
        primary key,
    latitude decimal(20,16) not null,
    longitude decimal(20,16) not null,
    town_hall_id int, #Some (lat, lon) registered not found in any town hall
    unit_id int not null,
    date_updated timestamp not null,
    record_id varchar(120) not null,
    constraint unit_location_town_halls_id_fk
        foreign key (town_hall_id) references town_halls (id),
    constraint unit_location_units_id_fk
        foreign key (unit_id) references units (id)
);

