DROP TABLE EMPLEADO;
DROP SEQUENCE EMPLEADO;
DROP TABLE PROPIEDAD;
DROP SEQUENCE PROPIEDAD;
DROP TABLE CLIENTE;
DROP TABLE PROPIEDAD_ARRENDADA;
DROP TABLE propietario CASCADE CONSTRAINTS;
DROP TABLE categoria_empleado CASCADE CONSTRAINTS;
DROP TABLE comuna CASCADE CONSTRAINTS;
DROP SEQUENCE seq_com;
 
CREATE SEQUENCE seq_com START WITH 80 INCREMENT BY 1;

CREATE TABLE comuna
(id_comuna NUMBER(3) NOT NULL,
 nombre_comuna VARCHAR2(30) NOT NULL,
 CONSTRAINT pk_sucursal PRIMARY KEY (id_comuna));
 
 

CREATE TABLE categoria_empleado
(id_categoria_emp NUMBER(1) GENERATED ALWAYS AS IDENTITY MINVALUE 1 
MAXVALUE 100
INCREMENT BY 1 START WITH 1 NOT NULL,
 desc_categoria_emp VARCHAR2(30) NOT NULL,
 CONSTRAINT pk_categoria_empleado PRIMARY KEY (id_categoria_emp));

CREATE TABLE propietario
(numrut_prop  NUMBER(10) Not Null,
 dvrut_prop  VARCHAR2(1) NOT NULL,
 appaterno_prop VARCHAR2(15) NOT NULL,
 apmaterno_prop VARCHAR2(15) NOT NULL,
 nombre_prop VARCHAR2(25) NOT NULL,
 direccion_prop VARCHAR2(60) NOT NULL,
 id_estcivil   NUMBER(1) NOT NULL,
 fonofijo_prop VARCHAR2(15) NOT NULL,
 celular_prop VARCHAR2(15),
 id_Comuna Number(3),
 CONSTRAINT pk_propietario PRIMARY KEY (numrut_prop));

-- creacion de llaves foraneas 
ALTER TABLE propietario
   ADD CONSTRAINT fk_propietario_comuna FOREIGN KEY (id_comuna)
   REFERENCES comuna (id_comuna);

  CREATE TABLE EMPLEADO(
  NUMRUT_EMP NUMERIC (10) NOT NULL,
  DVRUT_EMP VARCHAR2 (1 BYTE)NOT NULL,
  APPATERNO_EMP VARCHAR2(15 BYTE)NOT NULL,
  APMATERNO_EMP VARCHAR2(15 BYTE)NOT NULL,
  NOMBRE_EMP VARCHAR2 (25 BYTE)NOT NULL,
  DIRECCION_EMP VARCHAR2(60 BYTE)NOT NULL,
  ID_ESTCIVIL NUMERIC NOT NULL,
  FONOFIJO_EMP VARCHAR2(15 BYTE)NOT NULL,
  CELULAR_EMP VARCHAR2(15 BYTE) NULL,
  FECNAC_EMP NUMERIC(10)NULL,
  FECING_EMP NUMERIC (10)NOT NULL,
  SUELDO_EMP NUMERIC (7) NOT NULL, 
  ID_COMUNA NUMERIC NULL,
  ID_CATEGORIA_EMP NUMERIC(1)  
);

CREATE SEQUENCE seq_EMPLEADO
START WITH 1
INCREMENT BY 1;

ALTER TABLE EMPLEADO ADD CONSTRAINT PK_EMPLEADO PRIMARY KEY (NUMRUT_EMP);
ALTER TABLE EMPLEADO
   ADD CONSTRAINT fk_EMPLEADO_CATEGORIA_EMPLEADO FOREIGN KEY (id_categoria_emp)
   REFERENCES categoria_empleado (id_categoria_emp);
   
CREATE TABLE PROPIEDAD(
   NRO_PROPIEDAD NUMERIC(6)NOT NULL,
   DIRECCION_PROPIEDAD VARCHAR2(60)NOT NULL,
   SUPERFICIE NUMERIC (8,2)NOT NULL,
   NRO_DORMITORIOS NUMERIC(1)NULL,
   NRO_BAÑOS NUMERIC(1)NULL,
   VALOR_ARRIENDO VARCHAR2(7) NOT NULL,
   VALOR_GASTO_COMUN VARCHAR2 (7)NULL,
   ID_TIPO_PROPIEDAD VARCHAR2 (1) NOT NULL,
   ID_COMUNA NUMERIC NOT NULL,
   NUMRUT_PROP NUMERIC(10) NOT NULL,
   NUMRUT_EMP NUMERIC(10)NULL
);
CREATE SEQUENCE seq_PROPIEDAD
START WITH 1
INCREMENT BY 1;

ALTER TABLE PROPIEDAD ADD CONSTRAINT PK_PROPIEDAD PRIMARY KEY (NRO_PROPIEDAD);
ALTER TABLE PROPIEDAD
   ADD CONSTRAINT fk_PROPIEDAD_EMPLEADO FOREIGN KEY (NUMRUT_EMP)
   REFERENCES EMPLEADO(NUMRUT_EMP);
ALTER TABLE PROPIEDAD 
   ADD CONSTRAINT fk_PROPIEDAD_propietario FOREIGN KEY (numrut_prop)
   REFERENCES propietario(numrut_prop);
   
CREATE TABLE CLIENTE(
  NUMRUT_CLI NUMERIC(10)NOT NULL,
  DVRUT_CLI VARCHAR2 (1 BYTE) NOT NULL,
  APPATERNO_CLI VARCHAR2(15 BYTE)NOT NULL,
  APMATERNO_CLI VARCHAR2(15 BYTE)NOT NULL,
  NOMBRE_CLI VARCHAR2(25 BYTE)NOT NULL,
  DIRECCION_CLI VARCHAR2 (60 BYTE)NOT NULL,
  ID_ESTCIVIL NUMERIC NOT NULL,
  FONOFIJO_CLI NUMERIC(15) NOT NULL,
  CELULAR_CLI NUMERIC(15)NULL,
  RENTA_CLI NUMERIC(7)NOT NULL
  
);
ALTER TABLE CLIENTE ADD CONSTRAINT PK_CLIENTE PRIMARY KEY (NUMRUT_CLI);

CREATE TABLE PROPIEDAD_ARRENDADA(
  NRO_PROPIEDAD NUMERIC NOT NULL,
  FECINI_ARRIENDO DATE NOT NULL,
  FECTER_ARRIENDO DATE NULL,
  NUMRUT_CLI NUMERIC(10)NOT NULL
);
ALTER TABLE PROPIEDAD_ARRENDADA ADD CONSTRAINT PK_PROPIEDAD_ARRENDADA PRIMARY KEY (NRO_PROPIEDAD,FECINI_ARRIENDO);
ALTER TABLE PROPIEDAD 
   ADD CONSTRAINT fk_PROPIEDAD_ARRENDADA_CLIENTE FOREIGN KEY (NUMRUT_CLI)
   REFERENCES CLIENTE(NUMRUT_CLI);
   
-- insercion de datos
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Las Condes');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Providencia');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Santiago');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Ñuñoa');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Vitacura');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'La Reina');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'La Florida');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Maipú');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Lo Barnechea');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Macul');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'San Miguel');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Peñalolén');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Puente Alto');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Recoleta');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Estación Central');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'San Bernardo');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Independencia');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'La Cisterna');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Quilicura');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Quinta Normal');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Conchalí');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'San Joaquín');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Huechuraba');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'El Bosque');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Cerrillos');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Cerro Navia');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'La Granja');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'La Pintana');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Lo Espejo');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Lo Prado');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Pedro Aguirre Cerda');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Pudahuel');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Renca');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'San Ramón');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Melipilla');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'San Pedro');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Alhué');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'María Pinto');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Curacaví');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Talagante');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'El Monte');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Buin');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Paine');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Peñaflor');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Isla de Maipo');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Colina');
INSERT INTO comuna VALUES (seq_com.NEXTVAL,'Pirque');

INSERT INTO categoria_empleado(desc_categoria_emp) VALUES('Gerente');
INSERT INTO categoria_empleado(desc_categoria_emp) VALUES('Supervisor');
INSERT INTO categoria_empleado(desc_categoria_emp) VALUES('Ejecutivo de Arriendo');
INSERT INTO categoria_empleado(desc_categoria_emp) VALUES(NEXTVAL,'Auxiliar');

INSERT INTO propietario VALUES(12491094,'3','SAAVEDRA','VILLALOBOS','SERGIO','VIA 7 Nº1000 B/3 D/7',5,'22398244',NULL,82);
INSERT INTO propietario VALUES(12651346,'4','MUÑOZ','PEREZ','CLAUDIA','SANTA ISABEL 463','1','26359178','27412904',83);
INSERT INTO propietario VALUES(12116380,'5','BARAHONA','ORELLANA','JOSE','NTRA. SRA. SANTA GENOVEVA 9508','2','22871051',NULL,82);
INSERT INTO propietario VALUES(13024901,'K','VALENCIA','URBINA','SERGIO','MARIA ELENA 1857 V/LOS NAVIOS',3,'25417284','26211095',85);
INSERT INTO propietario VALUES(12885975,'0','BARRIOS','MUÑOZ','BARBARA','PASAJE PUCON 5940',5,'22215104','26710430',82);
INSERT INTO propietario VALUES(13041308,'1','PARDO','ESPINOSA','RICHARD','PJE.PIRAMIDE 1477 P/BOROA','1','26811939','27740990',87);
INSERT INTO propietario VALUES(11947288,'2','QUEZADA','GOMEZ','MARIO','LAS MALVAS 10470 V/PENSAMIENTO','2','25415191','25410480',88);
INSERT INTO propietario VALUES(12783347,'3','CUBILLOS','FERRADA','JORGE','LAGO RUPANCO 1556 P/LANALHUE',4,'22930493','25377732',89);
INSERT INTO propietario VALUES(13195197,'4','GUERRERO','ROMO','MAURICIO','BROCKMAN 1326 VILLA ITALIA',5,'2232366','28113377',92);
INSERT INTO propietario VALUES(12676073,'5','PIZARRO','TORO','JAIME','FCO.BILBAO 1826 P/SAN RAFAEL','1','25426807',NULL,94);
INSERT INTO propietario VALUES(13471056,'6','MIRANDA','VALENZUELA','PRISCILLA','AV. COLECTOR 4866 P/SANTIAGO','2','27796916','27790195',95);
INSERT INTO propietario VALUES(12064147,'7','ROBLES','VIDAL','LUIS','SEGUNDA TRANSVERSAL PJ.2 C/996',3,'25573796','25268570',87);
INSERT INTO propietario VALUES(14149786,'8','ROBLES','CAMIRUAGA','AQUILES','DIAGONAL PARAGUAY 360 DPTO 116',5,'22227933','25325139',87);
INSERT INTO propietario VALUES(13071695,'9','LOSADA','MALDONADO','LEONARDO','OCTAVA AV.PJE.JOSE READY 6256','1','25222006','25311153',80);
INSERT INTO propietario VALUES(12870395,'K','HERNANDEZ','VALLADARES','JONATHA','PJE.RENE OLIVARES 1294','2','25389883','26413331',106);
INSERT INTO propietario VALUES(14412994,'5','ALARCON','QUIROGA','JOHN','CALLE 1 C/4452 P/SANTIAGO',3,'27789352','25261372',107);
INSERT INTO propietario VALUES(12878526,'6','RIQUELME','CORREA','JOHN','MOISES RIOS Nº1065',5,'27375662','25261372',108);
COMMIT;