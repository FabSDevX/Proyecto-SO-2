<h1 align="left">Project Description 📝</h1>

<p align="left">
El presente proyecto tiene la finalidad de realizar un sistema capaz de detectar en un video proporcionado por el usuario la aparición de personas y objetos. En específico, se realizó el entrenamiento de dos modelos de detección: Un modelo capaz de detectar a dos famosos, Lionel Messi y John Krasinski, y un modelo capaz de detectar dos objetos: Cuchillos o anteojos.

Para que el sistema realice el análisis y detección de estos objetos, los usuarios serán capaces de proporcionar videos o seleccionar uno de los ya disponibles, subidos en la nube previamente por otros usuarios. Los usuarios podrán seleccionar cuál famoso querrán detectar, y los objetos serán detectados por defecto a modo de simular el procecso de moderación de contenido. Una vez terminado el proceso de detección, el sistema proporcionará una pantalla con los resultados obtenidos, indicando la cantidad de frames detectados de cada uno de los elementos.
</p>

<h2 align="left">Instrucciones de Instalación 📦</h2>

<p align="left">
Sigue los siguientes pasos para instalar el proyecto en tu entorno local:
</p>

<p align="left">
<ol>
  <li>Clona el repositorio:
    <pre><code>git clone https://github.com/usuario/repo.git</code></pre>
  </li>
  <li>Navega al directorio del proyecto:
    <pre><code>cd repo</code></pre>
  </li>
  <li>Instala las dependencias:
    <pre><code>npm install</code></pre>
  </li>
</ol>
</p>

<h2 align="left">Guía de Uso 🚀</h2>

<p align="left">
Para iniciar la aplicación, ejecuta el siguiente comando:
</p>

<p align="left">
<pre><code>npm start</code></pre>
</p>

<p align="left">
Una vez que la aplicación esté en funcionamiento, abre tu navegador y ve a <a href="http://localhost:3000">http://localhost:3000</a> para acceder a la interfaz de usuario.
</p>

<h2 align="left">Documentación de API 📚</h2>

<p align="left">
La API del sistema ofrece varias funcionalidades para gestionar tareas. A continuación se presentan algunos de los endpoints disponibles:
</p>

<h3 align="left">Obtener todas las tareas</h3>

<p align="left">
<pre><code>GET /api/tareas</code></pre>
Devuelve una lista de todas las tareas.
</p>

<h3 align="left">Crear una nueva tarea</h3>

<p align="left">
<pre><code>POST /api/tareas</code></pre>
Crea una nueva tarea. Ejemplo de cuerpo de la solicitud:
<pre><code>
{
  "titulo": "Nueva Tarea",
  "descripcion": "Descripción de la nueva tarea",
  "fecha_vencimiento": "2024-12-31"
}
</code></pre>
</p>

<h3 align="left">Actualizar una tarea</h3>

<p align="left">
<pre><code>PUT /api/tareas/:id</code></pre>
Actualiza una tarea existente. Ejemplo de cuerpo de la solicitud:
<pre><code>
{
  "titulo": "Tarea Actualizada",
  "descripcion": "Descripción actualizada",
  "fecha_vencimiento": "2024-12-31"
}
</code></pre>
</p>

<h3 align="left">Eliminar una tarea</h3>

<p align="left">
<pre><code>DELETE /api/tareas/:id</code></pre>
Elimina una tarea existente.
</p>

<h2 align="left">Créditos</h2>

<p align="left">
Autor: <a href="https://github.com/tuusuario">Tu Nombre</a>
</p>
