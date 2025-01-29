# Test 1: Python

## Descripción General
Este test consiste en consumir un archivo JSON con información de productos turísticos y procesar dicha información para obtener ciertos datos precalculados. El script interpreta cada producto activo, calcula su valoración promedio, selecciona las URLs de las imágenes más grandes y extrae el punto de encuentro si está disponible en la descripción del producto.

---

## Estructura del Proyecto
- `product_script.py`: Script principal que contiene la clase `Product` y las funciones para procesar los datos.
- `product.json`: Archivo JSON de ejemplo con información de productos turísticos.

---

## Instrucciones de Ejecución

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Situarse en la carpeta `test_1_python`:
   ```bash
   cd test_1_python
   ```
3. Ejecutar el script:

   Para Windows:
   ```bash
   python product_script.py
   ```

   Para macOS o Linux:
   ```bash
   python3 product_script.py
   ```

---

## Descripción del Código
El script está estructurado de la siguiente manera:

### Clase `Product`
Define los siguientes atributos privados:
- `averageRating`: Almacena el promedio de valoraciones del producto.
- `images`: Lista de URLs de las variantes de mayor ancho de las imágenes del producto.
- `meetingPoint`: Punto de encuentro del producto extraído de la descripción.

### Métodos
- `set_averageRating(value)`: Setter para el atributo `averageRating`.
- `set_images(value)`: Setter para el atributo `images`.
- `set_meetingPoint(value)`: Setter para el atributo `meetingPoint`.
- `toJSON()`: Devuelve la representación JSON del objeto `Product`.

### Funciones
- `calculateAverageRating(reviews)`: Calcula el promedio ponderado de valoraciones.
- `extractLargestImages(productImages)`: Obtiene las URLs de las variantes más grandes de cada imagen.
- `extractMeetingPoint(description)`: Extrae el punto de encuentro del atributo `description`.
- `parseProduct(productData)`: Procesa un producto y devuelve una instancia de la clase `Product`.

### Ejecución del Script
1. Carga el archivo JSON `product.json`.
2. Filtra los productos con `status = "ACTIVE"`.
3. Procesa cada producto activo utilizando `parseProduct()`.
4. Imprime la representación JSON de cada producto procesado.

---

## Salida esperada con el JSON presente en el proyecto
```json
{
 "averageRating": 4.17,
 "images": [
  "https://hare-media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/a0/8f/3a.jpg",
  "https://hare-media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/a3/0d/6b.jpg",
  "https://hare-media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/a3/09/56.jpg",
  "https://hare-media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/a3/04/ce.jpg",
  "https://hare-media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/a3/0a/24.jpg"
 ],
 "meetingPoint": "Port gate outside. (inside optional)"
}
```

---

## Notas Importantes
- El script maneja posibles errores de tipo y valores incorrectos mediante validaciones en los setters.
- Se utilizan expresiones regulares para extraer el punto de encuentro de la descripción.
- Las URLs de las imágenes se seleccionan tomando la variante de mayor ancho disponible.

---



# Test 2: MySQL

#### Parte A: Consultas SQL

**1. Obtener los valores “id”, "name", "short\_description" y "long\_description" de los registros de la tabla 'products' que tengan 'shortCode' distinto a 'X12345'.**

**Consulta:**

```sql
SELECT id, name, short_description, long_description
FROM products
WHERE short_code != "X12345";
```

La consulta selecciona las columnas solicitadas de la tabla `products`, filtrando los registros donde el campo `short_code` sea distinto de "X12345" con la condición `!=`.

---

**2. Contar los registros de la tabla 'products' para el supplier ID 1 (campo: supplier\_id) que hayan sido actualizados el día de hoy (campo: updated\_at).**

**Consulta:**

```sql
SELECT COUNT(*)
FROM products
WHERE supplier_id = 1
AND DATE(updated_at) = CURRENT_DATE();
```

La consulta utiliza la función `COUNT(*)` para contar los registros que cumplen con las condiciones dadas: `supplier_id = 1` y que la fecha de `updated_at` coincida con la fecha actual. La función `DATE(updated_at)` permite extraer solo la parte de la fecha, haciendo compatible la comparación con `CURRENT_DATE()`.

---

**3. Obtener los valores "duration" únicos (sin repeticiones) de la tabla 'products' para los registros que tengan un promedio de reseñas (reviews\_average\_rating) entre 4.0 y 4.5, y que tengan al menos un registro asociado en la tabla 'product\_option' cuyo 'name' sea igual a 'Adult'.**

**Consulta:**

```sql
SELECT DISTINCT duration
FROM products
WHERE reviews_average_rating BETWEEN 4.0 AND 4.5
AND id IN (SELECT product_id FROM product_option WHERE name = 'Adult');
```

La consulta  `(SELECT product_id FROM product_option WHERE name = 'Adult')` obtiene los `product_id` correspondientes, y la condición `id IN (...)` garantiza que solo se seleccionen productos asociados a esas opciones. El uso de `DISTINCT` elimina valores repetidos de `duration`. La condición `BETWEEN 4.0 AND 4.5` filtra el rango de puntuaciones.

---

**4. Obtener la última fecha de actualización (fetched\_at) para cada uno de los proveedores (campo supplier\_id), considerando todos los productos del mismo.**

**Consulta:**

```sql
SELECT supplier_id, MAX(fetched_at) as last_fetched_at
FROM products
GROUP BY supplier_id;
```

La consulta utiliza la función de agregación `MAX(fetched_at)` para obtener la última fecha de actualización por proveedor. La clausula `GROUP BY supplier_id` agrupa los resultados por cada `supplier_id`, devolviendo una única fila por proveedor con su fecha más reciente.

---

### Nota

Las consultas fueron probadas en una base de datos real creada localmente.

---

# Test 3: ReactJS

## Introducción

Este proyecto consiste en una aplicación web sencilla desarrollada con **Vite + React + JavaScript**, que consume un API REST y muestra un listado de hoteles. Para el diseño de la interfaz se utilizó **Tailwind CSS**, lo que permitió un desarrollo rápido y limpio.

---

## Tecnologías utilizadas

- **React** para la estructura del front-end.
- **Vite** como entorno de desarrollo.
- **JavaScript** para la lógica del proyecto.
- **Tailwind CSS** para el estilizado.
- **Axios** para realizar la petición HTTP.

---

## Requisitos para ejecutar el proyecto

Asumiendo que el repositorio ya está clonado:
1. Situarse en la carpeta `test_3_react_js/hotel_list`.
2. Ejecutar el comando:
   ```bash
   npm install
   ```
   Esto instalará las dependencias necesarias.
3. Ejecutar el proyecto con:
   ```bash
   npm run dev
   ```
4. Abrir el navegador y acceder a la dirección especificada en la terminal (generalmente `http://localhost:<puerto>`).

---

## Estructura del proyecto

El proyecto consta de los siguientes archivos principales:

### 1. **App.jsx**

Este componente principal se encarga de:

- Realizar una petición GET al API proporcionado: `https://wmw3lg8sha.execute-api.us-east-2.amazonaws.com/dev/dummy`.
- Guardar el listado de hoteles en el estado local.
- Renderizar una lista de componentes `HotelCard`, pasando las props necesarias para mostrar cada hotel.


```javascript
componentDidMount() {
  this.fetchHotels();
}

async fetchHotels() {
  try {
    const { data } = await axios.get(
      "https://wmw3lg8sha.execute-api.us-east-2.amazonaws.com/dev/dummy"
    );
    const hotels = data.data.hotels;
    this.setState({ hotels: hotels });
  } catch (error) {
    console.log(error);
  }
}
```

### 2. **HotelCard.jsx**

Este componente es responsable de mostrar la información de cada hotel de acuerdo a la estructura solicitada en la consigna.

#### Props utilizadas:

- `name`: Nombre del hotel.
- `stars`: Cantidad de estrellas.
- `address`: Dirección.
- `boardbases`: Tipos de bases de alimentación.
- `amenities`: Lista de servicios.
- `image`: Imagen del hotel.


```javascript
<div className="flex flex-row justify-between items-center mb-1">
  <div className="text-3xl text-[#003b95] font-[700]">{name}</div>
  <div className="bg-[#003b95] rounded-[10px] p-2">
    {"⭐".repeat(stars)}
  </div>
</div>
```

- Se utiliza el método `map` para listar las `boardbases` y `amenities` del hotel.

```javascript
{boardbases.map((boardbase) => (
  <div className="text-xl">{boardbase}</div>
))}

{amenities.map((amenity) => (
  <div>· {amenity.name}</div>
))}
```
