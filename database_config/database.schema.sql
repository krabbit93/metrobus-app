create database if not exists metrobus;
use metrobus;

create table if not exists town_halls
(
    id   int auto_increment
        primary key,
    name varchar(100) not null
);

create table if not exists delimiter_points
(
    id           int auto_increment
        primary key,
    latitude     decimal(20, 16) not null,
    longitude    decimal(20, 16) not null,
    town_hall_id int             not null,
    constraint delimiter_points_town_halls_id_fk
        foreign key (town_hall_id) references town_halls (id)
);