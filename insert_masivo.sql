--MARCA
INSERT INTO FERME.MARCA (ID, NOMBRE) VALUES (101, 'Redline');
INSERT INTO FERME.MARCA (ID, NOMBRE) VALUES (102, 'Holztek');
INSERT INTO FERME.MARCA (ID, NOMBRE) VALUES (103, 'Bauker');

--PRODUCTO
INSERT INTO FERME.PRODUCTO (PRODUCTO_ID, SKU, NOMBRE, COLOR, DESCRIPCION, STOCK, STOCK_CRITICO, DISPONIBILIDAD, PRECIO_NORMAL, PRECIO_OFERTA, URL_IMG, MARCA_ID) VALUES ('2984646413121', '2998814752605', 'Martillo carpintero', NULL, 'Martillo carpintero 20 Oz acero', 100, 50, 'S', 5000, 4790, 'img/producto/2984646413121.jpg', 101);
INSERT INTO FERME.PRODUCTO (PRODUCTO_ID, SKU, NOMBRE, COLOR, DESCRIPCION, STOCK, STOCK_CRITICO, DISPONIBILIDAD, PRECIO_NORMAL, PRECIO_OFERTA, URL_IMG, MARCA_ID) VALUES ('2984646234234', '2998814755042', 'Piso Flotante', 'Nogal', 'Piso flotante 138x19,3 cm 2,92 m2', 599, 250, 'S', 3890, 2690, 'img/producto/2984646234234.jpg', 102);
INSERT INTO FERME.PRODUCTO (PRODUCTO_ID, SKU, NOMBRE, COLOR, DESCRIPCION, STOCK, STOCK_CRITICO, DISPONIBILIDAD, PRECIO_NORMAL, PRECIO_OFERTA, URL_IMG, MARCA_ID) VALUES ('2984646645334', '2998814750907', 'Sierra circular electrica', NULL, 'Sierra circular electrica 7 1/4 1800W', 960, 350, 'S', 54980, 39890, 'img/producto/2984646645334.jpg', 103);
