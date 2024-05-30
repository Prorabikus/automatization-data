CREATE DATABASE remark_counter;

CREATE TABLE worker (
    ID serial primary key not null ,
    FIO varchar(256) not null ,
    date_of_birth varchar(32),
    passport varchar(16),
    address varchar(256),
    post varchar(128),
    phone varchar(16),
    experience int,
    remarks int default 0
);

CREATE TABLE statements(
    id serial not null primary key ,
    employee_id int not null ,
    type varchar(128)
);

