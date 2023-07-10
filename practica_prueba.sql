DROP TABLE empleado;
DROP TABLE producto;
DROP TABLE detalleboleta;
DROP TABLE cliente;
DROP TABLE boleta;
DROP TABLE equipo;
DROP TABLE categorizacion;
DROP TABLE comunas;
DROP TABLE fabrica;
DROP SEQUENCE seq_comunas;
DROP SEQUENCE seq_boleta;


CREATE SEQUENCE seq_comuna START WITH 100 INCREMENT BY 2;
CREATE SEQUENCE seq_boleta START WITH 1010 INCREMENT BY 10;



CREATE TABLE fabrica (
 id_fabrica NUMBER(4) NOT NULL,
 nom_fabrica VARCHAR2(60) NOT NULL
);
ALTER TABLE fabrica ADD CONSTRAINT pk_fabrica PRIMARY KEY ( id_fabrica );

CREATE TABLE comunas (
 id_comuna NUMBER NOT NULL,
 nom_comuna VARCHAR2(25) NOT NULL
);
ALTER TABLE comunas ADD CONSTRAINT pk_comunas PRIMARY KEY ( id_comuna );

CREATE TABLE categorizacion (
 id_categorizacion CHAR(1) NOT NULL,
 nom_categorizacion VARCHAR2(10) NOT NULL,
 porcentaje NUMBER NOT NULL
);
ALTER TABLE categorizacion ADD CONSTRAINT pk_categorizacion PRIMARY KEY ( id_categorizacion );


CREATE TABLE equipo (
 id_equipo VARCHAR2(1) NOT NULL,
 nom_equipo VARCHAR2(10) NOT NULL,
 porc NUMBER(5, 2) NOT NULL
);
ALTER TABLE equipo ADD CONSTRAINT pk_equipo PRIMARY KEY ( id_equipo );



CREATE TABLE boleta (
 id_boleta NUMBER NOT NULL,
 id_cliente NUMBER NOT NULL,
 id_empleado NUMBER(6) NOT NULL,
 fecha_boleta DATE NOT NULL
);
ALTER TABLE boleta ADD CONSTRAINT pk_boleta PRIMARY KEY ( id_boleta );


CREATE TABLE cliente (
 id_cliente NUMBER NOT NULL,
 nombre_cliente VARCHAR2(35) NOT NULL,
 direccion VARCHAR2(50) NOT NULL,
 telefono NUMBER NOT NULL,
 id_comuna NUMBER NOT NULL
);
ALTER TABLE cliente ADD CONSTRAINT pk_cliente PRIMARY KEY ( id_cliente );


CREATE TABLE producto (
 id_producto NUMBER NOT NULL,
 nom_producto VARCHAR2(25) NOT NULL,
 precio NUMBER NOT NULL,
 stock_actual NUMBER(4) NOT NULL,
 stock_minimo NUMBER(4) NOT NULL,
 id_fabrica NUMBER(4) NOT NULL
 );
ALTER TABLE producto ADD CONSTRAINT pk_producto PRIMARY KEY ( id_producto );


CREATE TABLE detalleboleta (
 cantidad NUMBER NOT NULL,
 id_producto NUMBER NOT NULL,
 id_boleta NUMBER NOT NULL
);
ALTER TABLE detalleboleta ADD CONSTRAINT pk_detalleboleta PRIMARY KEY ( id_producto,
 id_boleta );
 
 
 CREATE TABLE empleado (
 id_empleado NUMBER(6) NOT NULL,
 rut_empleado VARCHAR2(10) NOT NULL,
 nombres VARCHAR2(25) NOT NULL,
 paterno VARCHAR2(15) NOT NULL,
 materno VARCHAR2(15),
 fecnac DATE NOT NULL,
 feccontrato DATE NOT NULL,
 sueldo NUMBER NOT NULL,
 comision NUMBER NOT NULL,
 id_equipo VARCHAR2(1) NOT NULL,
 id_categorizacion CHAR(1) NOT NULL
);
ALTER TABLE empleado ADD CONSTRAINT pk_empleado PRIMARY KEY ( id_empleado );
ALTER TABLE empleado ADD CONSTRAINT un_empleado UNIQUE ( rut_empleado );


ALTER TABLE boleta
    ADD CONSTRAINT fk_boleta_cliente FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );
        
ALTER TABLE boleta
    ADD CONSTRAINT fk_boleta_empleado FOREIGN KEY ( id_empleado )
        REFERENCES empleado ( id_empleado );
        
ALTER TABLE cliente
    ADD CONSTRAINT fk_cliente_comunas FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );
        
ALTER TABLE detalleboleta
    ADD CONSTRAINT fk_detalleboleta_boleta FOREIGN KEY ( id_boleta )
        REFERENCES boleta ( id_boleta );
        
ALTER TABLE detalleboleta
    ADD CONSTRAINT fk_detalleboleta_producto FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );
        
ALTER TABLE empleado
    ADD CONSTRAINT fk_empleado_categorizacion FOREIGN KEY ( id_categorizacion )
        REFERENCES categorizacion ( id_categorizacion );
        
ALTER TABLE empleado
    ADD CONSTRAINT fk_empleado_equipo FOREIGN KEY ( id_equipo )
        REFERENCES equipo ( id_equipo );
        
ALTER TABLE producto
    ADD CONSTRAINT fk_producto_fabrica FOREIGN KEY ( id_fabrica )
        REFERENCES fabrica ( id_fabrica );

INSERT INTO boleta VALUES (1010,1,2,'17-01-22');
INSERT INTO boleta VALUES (1020,2,4,'17-01-22');
INSERT INTO boleta VALUES (1030,4,3,'17-01-22');
INSERT INTO boleta VALUES (1040,3,5,'17-01-22');
INSERT INTO boleta VALUES (1050,2,2,'17-01-22');

INSERT INTO categorizacion VALUES ('A','LISTA A',17.5);
INSERT INTO categorizacion VALUES ('B','LISTA B',17.5);
INSERT INTO categorizacion VALUES ('C','LISTA C',17.5);
INSERT INTO categorizacion VALUES ('D','LISTA D',17.5);
INSERT INTO categorizacion VALUES ('E','LISTA E',17.5);

INSERT INTO equipo VALUES ('A','Equipo A',8.56);
INSERT INTO equipo VALUES ('B','Equipo B',10.48);
INSERT INTO equipo VALUES ('C','Equipo C',11.27);
INSERT INTO equipo VALUES ('D','Equipo D',7.24);

INSERT INTO comunas VALUES(100,'Providencia');
INSERT INTO comunas VALUES(102,'Santiago');
INSERT INTO comunas VALUES(104,'Ñuñoa');
INSERT INTO comunas VALUES(106,'La Florida');
INSERT INTO comunas VALUES(108,'Maipu');
INSERT INTO comunas VALUES(110,'Lo Barnechea');
INSERT INTO comunas VALUES(112,'Macul');
INSERT INTO comunas VALUES(114,'San Miguel');
INSERT INTO comunas VALUES(116,'Recoleta');


INSERT INTO fabrica VALUES(5,'Costa');
INSERT INTO fabrica VALUES(10,'Ambrosoli');
INSERT INTO fabrica VALUES(15,'Nestlé');
INSERT INTO fabrica VALUES(20,'Dos en Uno');
INSERT INTO fabrica VALUES(25,'Arcor');

INSERT INTO cliente VALUES(1,'ALCATRAZ NOVOA MONSERRAT','RUBEN BARRALES 1630',564522114,102);
INSERT INTO cliente VALUES(2,'JIMENEZ LORCA ELENA','AV. BUSTAMANTE 529 DPTOK',5666654434,100);
INSERT INTO cliente VALUES(3,'TORRES ROCA MARIA','DONATELLO 7421',565626134,104);
INSERT INTO cliente VALUES(4,'LOPEZ ROJAS THOMAS','LORCA 2007',562989233,108);


INSERT INTO empleado VALUES(1,11111112-6,'MARY','CULVERT', 'RIVERA', '22-05-63','16/04/85',350000,0.25,'A','C');
INSERT INTO empleado VALUES(2,12222222-3,'JEROME','WOODS', '', '07-08-78','02-07-00',3450000,0.17,'B','B');
INSERT INTO empleado VALUES(3,'13333333-K','NORA','BROMSLER', 'OGAZ', '09-10-79','03-09-01',367400,0.25,'A','A');
INSERT INTO empleado VALUES(4,14444444-5,'FREDERICK','MALLON', 'PAREDES', '08-12-77','03-11-99',373620,0.12,'C','C');
INSERT INTO empleado VALUES(5,15555555-6,'PAZ','GUERRA', '', '08-12-88','03-11-15',373620,0.25,'A','C');


INSERT INTO producto VALUES(1,'BARRITAS',250,150,110,5);
INSERT INTO producto VALUES(2,'LECHEROS',325,50,30,5);
INSERT INTO producto VALUES(3,'ROSENDOS',100,200,50,10);
INSERT INTO producto VALUES(4,'ZIG ZAG',375,50,20,15);
INSERT INTO producto VALUES(5,'PECADOS',400,80,20,20);


INSERT INTO detalleboleta VALUES (10,1,1010);
INSERT INTO detalleboleta VALUES (33,5,1010);
INSERT INTO detalleboleta VALUES (88,3,1020);
INSERT INTO detalleboleta VALUES (33,4,1020);
INSERT INTO detalleboleta VALUES (90,1,1020);
INSERT INTO detalleboleta VALUES (200,4,1030);
INSERT INTO detalleboleta VALUES (500,2,1030);
INSERT INTO detalleboleta VALUES (500,5,1040);
INSERT INTO detalleboleta VALUES (250,2,1040);
INSERT INTO detalleboleta VALUES (300,3,1040);
INSERT INTO detalleboleta VALUES (196,4,1050);
INSERT INTO detalleboleta VALUES (128,5,1050);
INSERT INTO detalleboleta VALUES (181,2,1050);
