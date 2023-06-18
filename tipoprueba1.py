# tipo prueba 1 
DROP TABLE Vendedor;
DROP TABLE factura;
DROP TABLE detallefactura;
DROP TABLE articulo;
DROP TABLE cliente;
DROP TABLE categoria;
DROP TABLE marca;
DROP TABLE comuna;
DROP TABLE zona;
DROP SEQUENCE seq_comuna;
DROP SEQUENCE seq_zona;

CREATE SEQUENCE seq_comuna START WITH 100 INCREMENT BY 5;
CREATE SEQUENCE seq_zona START WITH 1 INCREMENT BY 1;


CREATE TABLE comuna (
      id_comuna  NUMBER(3) NOT NULL,
      nom_comuna VARCHAR2(60) NOT NULL
);
ALTER TABLE comuna ADD CONSTRAINT pk_comuna PRIMARY KEY (id_comuna);

CREATE TABLE zona (
    id_zona    NUMBER(1) NOT NULL,
    nom_zona   VARCHAR2(10) NOT NULL,
    porcentaje NUMBER
);
ALTER TABLE zona ADD CONSTRAINT pk_zona PRIMARY KEY (id_zona);

CREATE TABLE marca (
    id_marca  NUMBER NOT NULL,
    nom_marca VARCHAR2(25) NOT NULL
);
ALTER TABLE marca ADD CONSTRAINT pk_marca PRIMARY KEY (id_marca);

CREATE TABLE categoria (
    id_categoria  NUMBER(1) NOT NULL,
    nom_categoria VARCHAR2(20) NOT NULL,
    porcentaje    NUMBER NOT NULL
);
ALTER TABLE categoria ADD CONSTRAINT pk_categoria PRIMARY KEY (id_categoria);

CREATE TABLE articulo (
    id_articulo    NUMBER NOT NULL,
    nom_articulo   VARCHAR2(25) NOT NULL,
    precio         NUMBER NOT NULL,
    stock_actual   NUMBER(4) NOT NULL,
    stock_minimo   NUMBER(4),
    id_marca       NUMBER NOT NULL,
    marca_id_marca NUMBER NOT NULL
);

ALTER TABLE articulo ADD CONSTRAINT pk_articulo PRIMARY KEY (id_articulo);


CREATE TABLE cliente (
    id_cliente     NUMBER NOT NULL,
    nombre_cliente VARCHAR2(35) NOT NULL,
    direccion      VARCHAR2(50) NOT NULL,
    telefono       NUMBER,
    id_comuna      NUMBER(3) NOT NULL,
    rut            VARCHAR2(12) NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT pk_cliente PRIMARY KEY (id_cliente);

ALTER TABLE cliente ADD CONSTRAINT un_cliente_rut UNIQUE (rut);

CREATE TABLE detallefactura (
    id_factura           NUMBER NOT NULL,
    id_articulo          NUMBER NOT NULL,
    cantidad             VARCHAR2(6) NOT NULL,
    factura_id_factura   NUMBER NOT NULL,
    articulo_id_articulo NUMBER NOT NULL
);

ALTER TABLE detallefactura ADD CONSTRAINT pk_detallefactura PRIMARY KEY (id_factura,id_articulo);

CREATE TABLE factura (
    id_factura           NUMBER NOT NULL,
    id_cliente           NUMBER NOT NULL,
    id_vendedor          NUMBER NOT NULL,
    fecha_factura        DATE NOT NULL,
    vendedor_id_vendedor NUMBER(6) NOT NULL,
    cliente_id_cliente   NUMBER NOT NULL
);

ALTER TABLE factura ADD CONSTRAINT pk_factura PRIMARY KEY (id_factura);

CREATE TABLE vendedor (
    id_vendedor            NUMBER(6) NOT NULL,
    rut_vendedor           VARCHAR2(10) NOT NULL,
    nombres                VARCHAR2(25) NOT NULL,
    paterno                VARCHAR2(15) NOT NULL,
    materno                VARCHAR2(15),
    fecnac                 DATE NOT NULL,
    feccontrato            DATE NOT NULL,
    sueldo                 NUMBER NOT NULL,
    comision               NUMBER NOT NULL,
    id_zona                NUMBER,
    id_categoria           NUMBER(1) NOT NULL,
    categoria_id_categoria NUMBER(1) NOT NULL,
    zona_id_zona           NUMBER(1) NOT NULL
);

ALTER TABLE vendedor ADD CONSTRAINT pk_vendedor PRIMARY KEY (id_vendedor);

ALTER TABLE articulo
    ADD CONSTRAINT fk_articulo_marca FOREIGN KEY (marca_id_marca)
        REFERENCES marca (id_marca);

ALTER TABLE cliente
    ADD CONSTRAINT fk_cliente_comuna FOREIGN KEY (id_comuna)
        REFERENCES comuna (id_comuna);
        
ALTER TABLE detallefactura
    ADD CONSTRAINT fk_detallefactura_factura FOREIGN KEY (id_factura )
        REFERENCES factura (id_factura);

ALTER TABLE factura
    ADD CONSTRAINT fk_factura_cliente FOREIGN KEY (id_cliente)
        REFERENCES cliente (id_cliente);

ALTER TABLE factura
    ADD CONSTRAINT fk_factura_vendedor FOREIGN KEY (id_vendedor)
        REFERENCES vendedor (id_vendedor);
        
ALTER TABLE vendedor
    ADD CONSTRAINT fk_vendedor_categoria FOREIGN KEY (id_categoria)
        REFERENCES categoria (id_categoria);
        
ALTER TABLE vendedor
    ADD CONSTRAINT fk_vendedor_zona FOREIGN KEY ( zona_id_zona )
        REFERENCES zona ( id_zona );
        
INSERT INTO comuna VALUES (100,'Providencia');
INSERT INTO comuna VALUES (105,'Santiago');
INSERT INTO comuna VALUES (110,'Ñuñoa');
INSERT INTO comuna VALUES (115,'La Florida');
INSERT INTO comuna VALUES (120,'Maipu');

INSERT INTO marca VALUES(1000,'Familand');
INSERT INTO marca VALUES(1100,'Nivea');
INSERT INTO marca VALUES(1200,'Dove');
INSERT INTO marca VALUES(1300,'Gillete');
INSERT INTO marca VALUES(1400,'Monterey');

INSERT INTO categoria VALUES(1,'Categoria A',17.5);
INSERT INTO categoria VALUES(2,'Categoria B',12.6);
INSERT INTO categoria VALUES(3,'Categoria C',9.4);
INSERT INTO categoria VALUES(4,'Categoria D',7.2);
INSERT INTO categoria VALUES(5,'Categoria E',5.4);

INSERT INTO zona VALUES(1,'Norte',8.56);
INSERT INTO zona VALUES(2,'Sur',10.48);
INSERT INTO zona VALUES(3,'Oriente C',11.27);
INSERT INTO zona VALUES(4,'Poniente',7.24);
INSERT INTO zona VALUES(5,'Centro',7.24);

INSERT INTO cliente VALUES(1,'ALCARAZ NOVOA MONTSERRAT','BUENVENTURA 160',564522114,100,1234567891);
INSERT INTO cliente VALUES(2,'JIMENEZLORCA ELENA','LAGUNAS 52 DPTO. K',566665443,105,1234555565);
INSERT INTO cliente VALUES(3,'TORRES ROCA MARIA','DONATELLO 7421',565626134,115,444444544);
INSERT INTO cliente VALUES(4,'LOPEZ ROJAS THOMAS','ORDOÑEZ 2007',562989233,120,451264654);

INSERT INTO articulo VALUES(1,'JABON',1250,150,80,1000,1000);
INSERT INTO articulo VALUES(2,'SHAMPOO',2325,50,20,1200,1200);
INSERT INTO articulo VALUES(3,'ACONDICIONADOR',2100,200,50,1200,1200);
INSERT INTO articulo VALUES(4,'CREMA DE AFEITAR',3475,50,20,1300,1300);
INSERT INTO articulo VALUES(5,'CAFE',3500,80,40,1400,1400);

INSERT INTO vendedor VALUES(1,'11111112-6','BENITO','ORDENES','ROMERO','22-05-63','16-04-85',350000,0.13,1,3,0.13,1);
INSERT INTO vendedor VALUES(2,'12222222-3','MARTA','VIVEROS','','07-08-78','02-07-00',345000,0.07,2,2,0.07,2);
INSERT INTO vendedor VALUES(3,'13333333-K','OSCAR','CACERES','LAGOS','09-10-79','03-09-01',367400,0.13,1,1,0.13,1);
INSERT INTO vendedor VALUES(4,'14444444-5','MILENA','MENA','CARTES','08-12-77','03-11-99',373620,0.05,3,3,0.05,3);
INSERT INTO vendedor VALUES(5,'15555555-6','ESTEBAN','ROMERO','','08-12-88','03-11-15',373620,0.8,1,3,0.8,3);

INSERT INTO detallefactura VALUES(10000,1,20,10000,1);
INSERT INTO detallefactura VALUES(10000,5,23,10000,5);
INSERT INTO detallefactura VALUES(10010,3,38,10010,3);
INSERT INTO detallefactura VALUES(10010,4,43,10010,4);
INSERT INTO detallefactura VALUES(10010,1,48,10010,1);
INSERT INTO detallefactura VALUES(10020,4,30,10020,4);
INSERT INTO detallefactura VALUES(10020,2,20,10020,2);
INSERT INTO detallefactura VALUES(10030,5,60,10030,5);
INSERT INTO detallefactura VALUES(10030,2,45,10030,2);
INSERT INTO detallefactura VALUES(10030,3,35,10030,3);
INSERT INTO detallefactura VALUES(10040,4,29,10040,4);
INSERT INTO detallefactura VALUES(10040,5,28,10040,5);
INSERT INTO detallefactura VALUES(10040,2,21,10040,2);

INSERT INTO factura VALUES(10000,1,2,'18-01-22',1,2);
INSERT INTO factura VALUES(10010,2,4,'18-01-22',2,4);
INSERT INTO factura VALUES(10020,4,3,'18-01-22',4,3);
INSERT INTO factura VALUES(10030,3,5,'18-01-22',3,5);
INSERT INTO factura VALUES(10040,2,2,'18-01-22',2,2);

